#!/usr/bin/env python3
from __future__ import annotations

import argparse
import io
import json
import os
import re
import shutil
import tempfile
import time
import urllib.error
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import fitz


API_BASE = "https://api.mathpix.com/v3"

DOWNLOAD_ROOT = Path("/Users/gradyclopton/Downloads/Asmar Complex Analysis")
CA_DIR = DOWNLOAD_ROOT / "Asmar Complex Analysis with Partial Differntial Equations"
PDE_DIR = DOWNLOAD_ROOT / "Asmar Partial Differential Equations"
PDE_PDF = PDE_DIR / "asmar.pdf"
PDE_SPLIT_DIR = PDE_DIR / "split chapters"
VAULT_BOOK_DIR = Path(
    "/Users/gradyclopton/ObsidianVaults/complex_analysis/Books/"
    "Asmar Applied Complex Analysis with Applications to Differential Equations"
)
STATE_PATH = VAULT_BOOK_DIR / ".asmar_import_state.json"


@dataclass(frozen=True)
class SplitSpec:
    name: str
    start_page: int
    end_page: int


@dataclass(frozen=True)
class ChapterSpec:
    source_pdf: Path
    final_number: int
    title: str
    source_prefix: str

    @property
    def folder_name(self) -> str:
        return f"Chapter {self.final_number:02d} {self.title}"

    @property
    def chapter_md_name(self) -> str:
        return f"{self.folder_name}.md"

    @property
    def original_pdf_name(self) -> str:
        return f"Chapter {self.final_number} {self.title}.pdf"


PDE_SPLITS: list[SplitSpec] = [
    SplitSpec("Front Matter", 1, 13),
    SplitSpec("Chapter 1 A Preview of Applications and Techniques", 14, 29),
    SplitSpec("Chapter 2 Fourier Series", 30, 111),
    SplitSpec("Chapter 3 Partial Differential Equations in Rectangular Coordinates", 112, 201),
    SplitSpec("Chapter 4 Partial Differential Equations in Polar and Cylindrical Coordinates", 202, 277),
    SplitSpec("Chapter 5 Partial Differential Equations in Spherical Coordinates", 278, 333),
    SplitSpec("Chapter 6 Sturm-Liouville Theory with Engineering Applications", 334, 395),
    SplitSpec("Chapter 7 The Fourier Transform and Its Applications", 396, 485),
    SplitSpec("Chapter 8 The Laplace and Hankel Transforms with Applications", 486, 521),
    SplitSpec("Chapter 9 Finite Difference Numerical Methods", 522, 552),
    SplitSpec(
        "Chapter 10 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations",
        553,
        579,
    ),
    SplitSpec("Chapter 11 An Introduction to Quantum Mechanics", 580, 617),
    SplitSpec("Chapter 12 Green's Functions and Conformal Mappings", 618, 697),
    SplitSpec("Appendix A Ordinary Differential Equations Review of Concepts and Methods", 698, 761),
    SplitSpec("Back Matter", 762, 813),
]


def selected_chapters() -> list[ChapterSpec]:
    return [
        ChapterSpec(CA_DIR / "Chapter 3 Complex Integration.pdf", 3, "Complex Integration", "3"),
        ChapterSpec(CA_DIR / "Chapter 4 Complex Series.pdf", 4, "Complex Series", "4"),
        ChapterSpec(CA_DIR / "Chapter 5 Residue Theory.pdf", 5, "Residue Theory", "5"),
        ChapterSpec(CA_DIR / "Chapter 6 Conformal Mappings.pdf", 6, "Conformal Mappings", "6"),
        ChapterSpec(CA_DIR / "Chapter 7 Fourier Series.pdf", 7, "Fourier Series", "7"),
        ChapterSpec(CA_DIR / "Chapter 11 The Fourier Transform and Its Applications.pdf", 8, "The Fourier Transform and Its Applications", "11"),
        ChapterSpec(
            CA_DIR / "Chapter 12 The Laplace and Hankel Transforms with Applications.pdf",
            9,
            "The Laplace and Hankel Transforms with Applications",
            "12",
        ),
        ChapterSpec(
            PDE_SPLIT_DIR / "Appendix A Ordinary Differential Equations Review of Concepts and Methods.pdf",
            10,
            "Ordinary Differential Equations Review of Concepts and Methods",
            "A",
        ),
        ChapterSpec(
            PDE_SPLIT_DIR / "Chapter 3 Partial Differential Equations in Rectangular Coordinates.pdf",
            11,
            "Partial Differential Equations in Rectangular Coordinates",
            "3",
        ),
        ChapterSpec(
            PDE_SPLIT_DIR / "Chapter 4 Partial Differential Equations in Polar and Cylindrical Coordinates.pdf",
            12,
            "Partial Differential Equations in Polar and Cylindrical Coordinates",
            "4",
        ),
        ChapterSpec(
            PDE_SPLIT_DIR / "Chapter 5 Partial Differential Equations in Spherical Coordinates.pdf",
            13,
            "Partial Differential Equations in Spherical Coordinates",
            "5",
        ),
        ChapterSpec(
            PDE_SPLIT_DIR / "Chapter 6 Sturm-Liouville Theory with Engineering Applications.pdf",
            14,
            "Sturm-Liouville Theory with Engineering Applications",
            "6",
        ),
        ChapterSpec(
            PDE_SPLIT_DIR / "Chapter 11 An Introduction to Quantum Mechanics.pdf",
            15,
            "An Introduction to Quantum Mechanics",
            "11",
        ),
        ChapterSpec(
            PDE_SPLIT_DIR / "Chapter 12 Green's Functions and Conformal Mappings.pdf",
            16,
            "Green's Functions and Conformal Mappings",
            "12",
        ),
        ChapterSpec(
            PDE_SPLIT_DIR
            / "Chapter 10 Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations.pdf",
            17,
            "Sampling and Discrete Fourier Analysis with Applications to Partial Differential Equations",
            "10",
        ),
        ChapterSpec(
            PDE_SPLIT_DIR / "Chapter 9 Finite Difference Numerical Methods.pdf",
            18,
            "Finite Difference Numerical Methods",
            "9",
        ),
    ]


def _headers() -> dict[str, str]:
    app_id = os.environ.get("MATHPIX_APP_ID", "").strip()
    app_key = os.environ.get("MATHPIX_APP_KEY", "").strip()
    if not app_id or not app_key:
        raise RuntimeError("Missing Mathpix credentials: set MATHPIX_APP_ID and MATHPIX_APP_KEY.")
    return {"app_id": app_id, "app_key": app_key}


def _request_json(method: str, url: str, body: bytes | None = None, content_type: str | None = None) -> Any:
    headers = dict(_headers())
    if content_type:
        headers["Content-Type"] = content_type
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=120) as resp:
        raw = resp.read()
    return json.loads(raw.decode("utf-8"))


def _request_bytes(method: str, url: str) -> bytes:
    req = urllib.request.Request(url, headers=_headers(), method=method)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def _multipart_form(fields: dict[str, str], files: dict[str, tuple[str, bytes, str]]) -> tuple[bytes, str]:
    boundary = "----mathpixform-" + str(int(time.time() * 1_000_000))
    crlf = "\r\n"
    parts: list[bytes] = []
    for name, value in fields.items():
        parts.append(f"--{boundary}{crlf}".encode())
        parts.append(f'Content-Disposition: form-data; name="{name}"{crlf}{crlf}'.encode())
        parts.append(value.encode())
        parts.append(crlf.encode())
    for name, (filename, content, mimetype) in files.items():
        parts.append(f"--{boundary}{crlf}".encode())
        parts.append(
            f'Content-Disposition: form-data; name="{name}"; filename="{filename}"{crlf}'.encode()
        )
        parts.append(f"Content-Type: {mimetype}{crlf}{crlf}".encode())
        parts.append(content)
        parts.append(crlf.encode())
    parts.append(f"--{boundary}--{crlf}".encode())
    return b"".join(parts), f"multipart/form-data; boundary={boundary}"


def _load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return {}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def _save_state(state: dict[str, Any]) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")


def _normalize_mathpix_markdown(text: str) -> str:
    return (
        text.replace(r"\(", "$")
        .replace(r"\)", "$")
        .replace(r"\[", "$$")
        .replace(r"\]", "$$")
    )


def _promote_plain_section_headings(text: str, source_prefix: str) -> str:
    pattern = re.compile(
        rf"^(?!#)\s*{re.escape(source_prefix)}\.\s*(\d+(?:\.\d+)*)\s+(.+?)\s*$",
        re.MULTILINE,
    )
    return pattern.sub(lambda m: f"### {source_prefix}.{m.group(1)} {m.group(2)}", text)


def _submit_pdf(pdf_path: Path) -> str:
    pdf_bytes = pdf_path.read_bytes()
    options = {"math_inline_delimiters": ["$", "$"]}
    body, content_type = _multipart_form(
        fields={"options_json": json.dumps(options)},
        files={"file": (pdf_path.name, pdf_bytes, "application/pdf")},
    )
    result = _request_json("POST", f"{API_BASE}/pdf", body=body, content_type=content_type)
    pdf_id = result.get("pdf_id")
    if not isinstance(pdf_id, str) or not pdf_id:
        raise RuntimeError(f"Unexpected submission response for {pdf_path.name}: {result}")
    return pdf_id


def _wait_for_completion(pdf_id: str, *, label: str) -> None:
    attempt = 0
    while True:
        attempt += 1
        status = _request_json("GET", f"{API_BASE}/pdf/{pdf_id}")
        state = status.get("status")
        if state == "completed":
            return
        if state in {"error", "failed"}:
            raise RuntimeError(f"Mathpix conversion failed for {label}: {json.dumps(status)[:500]}")
        percent = status.get("percent_done")
        if isinstance(percent, (int, float)):
            print(f"Converting {label} ... {percent}%")
        else:
            print(f"Converting {label} ... status={state}")
        time.sleep(2 if attempt < 10 else 5)


def _download_markdown_zip(pdf_id: str) -> bytes:
    for ext in ("md.zip", "mmd.zip"):
        try:
            return _request_bytes("GET", f"{API_BASE}/pdf/{pdf_id}.{ext}")
        except urllib.error.HTTPError as exc:
            if exc.code in {400, 404}:
                continue
            raise
    raise RuntimeError(f"No markdown zip available for pdf_id={pdf_id}")


def ensure_pde_split(force: bool) -> None:
    PDE_SPLIT_DIR.mkdir(parents=True, exist_ok=True)
    with fitz.open(PDE_PDF) as doc:
        for spec in PDE_SPLITS:
            out_path = PDE_SPLIT_DIR / f"{spec.name}.pdf"
            if out_path.exists() and not force:
                continue
            new = fitz.open()
            try:
                new.insert_pdf(doc, from_page=spec.start_page - 1, to_page=spec.end_page - 1)
                new.save(out_path)
            finally:
                new.close()
            print(f"Wrote split PDF: {out_path}")


def _replace_heading_number(text: str, source_prefix: str, final_number: int) -> str:
    def repl(match: re.Match[str]) -> str:
        hashes = match.group(1)
        suffix = match.group(2)
        title = match.group(3)
        return f"{hashes} {final_number}.{suffix}{title}"

    pattern = re.compile(
        rf"^(#+)\s+{re.escape(source_prefix)}\.\s*(\d+(?:\.\d+)*)\b(.*)$",
        re.MULTILINE,
    )
    return pattern.sub(repl, text)


def _replace_chapter_heading(text: str, source_prefix: str, final_number: int) -> str:
    pattern = re.compile(rf"^(#+)\s+{re.escape(source_prefix)}\b(?!\.)", re.MULTILINE)
    return pattern.sub(lambda m: f"{m.group(1)} {final_number}", text)


def _replace_inline_self_refs(text: str, source_prefix: str, final_number: int) -> str:
    replacements = [
        (
            re.compile(rf"\bSection\s+{re.escape(source_prefix)}\.\s*(\d+(?:\.\d+)*)\b"),
            lambda m: f"Section {final_number}.{m.group(1)}",
        ),
        (
            re.compile(
                rf"\bSections\s+{re.escape(source_prefix)}\.\s*(\d+(?:\.\d+)*)\s*[-–]\s*{re.escape(source_prefix)}\.\s*(\d+(?:\.\d+)*)\b"
            ),
            lambda m: f"Sections {final_number}.{m.group(1)}-{final_number}.{m.group(2)}",
        ),
        (
            re.compile(
                rf"\bSections\s+{re.escape(source_prefix)}\.\s*(\d+(?:\.\d+)*)\s+and\s+{re.escape(source_prefix)}\.\s*(\d+(?:\.\d+)*)\b"
            ),
            lambda m: f"Sections {final_number}.{m.group(1)} and {final_number}.{m.group(2)}",
        ),
        (
            re.compile(rf"\bChapter\s+{re.escape(source_prefix)}\b"),
            lambda m: f"Chapter {final_number}",
        ),
        (
            re.compile(rf"\bChapters\s+{re.escape(source_prefix)}\s*[-–]\s*{re.escape(source_prefix)}\b"),
            lambda m: f"Chapters {final_number}-{final_number}",
        ),
    ]
    for pattern, repl in replacements:
        text = pattern.sub(repl, text)
    return text


def renumber_markdown(text: str, spec: ChapterSpec) -> str:
    text = _normalize_mathpix_markdown(text)
    text = _promote_plain_section_headings(text, spec.source_prefix)
    text = _replace_heading_number(text, spec.source_prefix, spec.final_number)
    text = _replace_chapter_heading(text, spec.source_prefix, spec.final_number)
    text = _replace_inline_self_refs(text, spec.source_prefix, spec.final_number)
    return text


def split_into_sections(text: str, spec: ChapterSpec) -> list[tuple[str, str]]:
    pattern = re.compile(rf"^#{{1,6}}\s+{spec.final_number}\.(\d+)\s+(.+?)\s*$", re.MULTILINE)
    matches = list(pattern.finditer(text))
    if not matches:
        raise RuntimeError(f"No section headings found for chapter {spec.final_number} ({spec.title})")

    results: list[tuple[str, str]] = []
    for idx, match in enumerate(matches):
        sec_num = match.group(1)
        sec_title = match.group(2).strip()
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        chunk = text[start:end].strip()
        if idx == 0:
            preamble = text[:start].strip()
            if preamble:
                chunk = preamble + "\n\n" + chunk
        file_name = f"{spec.final_number}.{sec_num} {sec_title}.md"
        results.append((file_name, chunk + "\n"))
    return results


def convert_chapter(spec: ChapterSpec, state: dict[str, Any], *, force: bool) -> None:
    folder_path = VAULT_BOOK_DIR / spec.folder_name
    original_copy = folder_path / "original copy"
    images_dir = folder_path / "images"

    if folder_path.exists() and not force:
        expected = [
            folder_path / spec.chapter_md_name,
            original_copy / spec.original_pdf_name,
        ]
        if all(path.exists() for path in expected):
            print(f"Skipping existing chapter: {spec.folder_name}")
            return

    key = str(spec.source_pdf)
    entry = state.setdefault("chapters", {}).setdefault(key, {})
    pdf_id = entry.get("pdf_id")
    if not isinstance(pdf_id, str) or not pdf_id:
        print(f"Submitting {spec.source_pdf.name}")
        pdf_id = _submit_pdf(spec.source_pdf)
        entry["pdf_id"] = pdf_id
        _save_state(state)

    _wait_for_completion(pdf_id, label=spec.source_pdf.name)
    zip_bytes = _download_markdown_zip(pdf_id)

    with tempfile.TemporaryDirectory(prefix="asmar_mathpix_") as tmp:
        tmp_dir = Path(tmp)
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
            zf.extractall(tmp_dir)

        md_files = sorted(tmp_dir.rglob("*.md"))
        if not md_files:
            raise RuntimeError(f"No markdown file extracted for {spec.source_pdf}")
        raw_md_path = md_files[0]
        raw_text = raw_md_path.read_text(encoding="utf-8", errors="replace")
        renumbered = renumber_markdown(raw_text, spec)
        sections = split_into_sections(renumbered, spec)

        if folder_path.exists():
            shutil.rmtree(folder_path)
        folder_path.mkdir(parents=True, exist_ok=True)
        original_copy.mkdir(parents=True, exist_ok=True)

        shutil.copy2(spec.source_pdf, original_copy / spec.original_pdf_name)
        (original_copy / spec.chapter_md_name).write_text(raw_text, encoding="utf-8")
        (folder_path / spec.chapter_md_name).write_text(renumbered, encoding="utf-8")

        extracted_images = list(tmp_dir.rglob("images"))
        if extracted_images:
            shutil.copytree(extracted_images[0], images_dir, dirs_exist_ok=True)
        else:
            images_dir.mkdir(exist_ok=True)

        for file_name, content in sections:
            (folder_path / file_name).write_text(content, encoding="utf-8")

    entry.update(
        {
            "final_folder": str(folder_path),
            "final_number": spec.final_number,
            "title": spec.title,
            "completed_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
    )
    _save_state(state)
    print(f"Wrote chapter: {folder_path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Import Asmar chapters into the complex analysis vault.")
    parser.add_argument("--force-split", action="store_true", help="Rewrite the split PDE chapter PDFs.")
    parser.add_argument("--force-chapters", action="store_true", help="Rewrite existing chapter folders in the vault.")
    args = parser.parse_args()

    VAULT_BOOK_DIR.mkdir(parents=True, exist_ok=True)
    state = _load_state()

    ensure_pde_split(force=args.force_split)
    for spec in selected_chapters():
        if not spec.source_pdf.exists():
            raise FileNotFoundError(f"Missing source PDF: {spec.source_pdf}")
        convert_chapter(spec, state, force=args.force_chapters)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

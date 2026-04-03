#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import statistics
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import fitz


BASE_DIR = Path(
    "/Users/gradyclopton/ObsidianVaults/complex_analysis/Books/"
    "Asmar Applied Complex Analysis with Applications to Differential Equations"
)


@dataclass
class Line:
    page: int
    text: str
    left: float
    top: float
    height: float
    metric: float
    is_ocr: bool
    confidence: float = 100.0
    fonts: tuple[str, ...] = ()


@dataclass
class Heading:
    page: int
    top: float
    text: str


def clean_text(text: str) -> str:
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u2013", "-").replace("\u2014", "-")
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def title_from_filename(path: Path) -> str:
    return clean_text(path.stem)


def chapter_number(path: Path) -> int:
    match = re.search(r"Chapter (\d+)", str(path))
    if not match:
        raise ValueError(f"Cannot parse chapter number from {path}")
    return int(match.group(1))


def looks_like_text_layer(doc: fitz.Document) -> bool:
    lengths = [len(doc[i].get_text("text").strip()) for i in range(min(5, doc.page_count))]
    return sum(lengths) >= 400


def extract_text_lines(doc: fitz.Document) -> list[Line]:
    lines: list[Line] = []
    for page_num in range(doc.page_count):
        page = doc[page_num]
        data = page.get_text("dict")
        for block in data["blocks"]:
            for line in block.get("lines", []):
                spans = line.get("spans", [])
                if not spans:
                    continue
                text = clean_text("".join(span["text"] for span in spans))
                if not text:
                    continue
                x0, y0, _, y1 = line["bbox"]
                fonts = tuple(sorted({span["font"] for span in spans}))
                size = max(span["size"] for span in spans)
                lines.append(
                    Line(
                        page=page_num + 1,
                        text=text,
                        left=x0,
                        top=y0,
                        height=y1 - y0,
                        metric=size,
                        is_ocr=False,
                        confidence=100.0,
                        fonts=fonts,
                    )
                )
    return lines


def extract_ocr_lines(doc: fitz.Document) -> list[Line]:
    lines: list[Line] = []
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        for page_num in range(doc.page_count):
            page = doc[page_num]
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
            image_path = tmpdir_path / f"page-{page_num + 1}.png"
            pix.save(image_path)
            result = subprocess.run(
                ["tesseract", str(image_path), "stdout", "--psm", "6", "tsv"],
                check=True,
                capture_output=True,
                text=True,
            )
            grouped: dict[tuple[int, int, int], list[dict[str, str]]] = {}
            rows = result.stdout.splitlines()
            for row in rows[1:]:
                cols = row.split("\t")
                if len(cols) != 12:
                    continue
                level, _, block, par, line_no, _, left, top, width, height, conf, text = cols
                if level != "5":
                    continue
                text = clean_text(text)
                if not text:
                    continue
                key = (int(block), int(par), int(line_no))
                grouped.setdefault(key, []).append(
                    {
                        "left": left,
                        "top": top,
                        "width": width,
                        "height": height,
                        "conf": conf,
                        "text": text,
                    }
                )
            for words in grouped.values():
                texts = [word["text"] for word in words]
                confs = [float(word["conf"]) for word in words if word["conf"] not in {"-1", ""}]
                if not texts:
                    continue
                line_text = clean_text(" ".join(texts))
                left = min(int(word["left"]) for word in words)
                top = min(int(word["top"]) for word in words)
                height = max(int(word["height"]) for word in words)
                metric = statistics.mean(confs) if confs else 0.0
                lines.append(
                    Line(
                        page=page_num + 1,
                        text=line_text,
                        left=float(left),
                        top=float(top),
                        height=float(height),
                        metric=float(height),
                        is_ocr=True,
                        confidence=float(metric),
                    )
                )
    return lines


def body_metric(lines: Iterable[Line]) -> float:
    metrics = [
        line.metric if not line.is_ocr else line.height
        for line in lines
        if 20 <= len(line.text) <= 140
        and not re.match(r"^(Chapter|Section|Exercises)\b", line.text, re.I)
    ]
    if not metrics:
        return 12.0
    return statistics.median(metrics)


def infer_section_prefix(lines: list[Line], chapter: int) -> str:
    sample = " ".join(line.text for line in lines[:250])
    numeric_re = re.compile(rf"^{chapter}\.\d+\b")
    if any(numeric_re.match(line.text) for line in lines[:400]):
        return str(chapter)
    numeric_prefixes: list[tuple[int, int, float]] = []
    for line in lines[:500]:
        match = re.match(r"^(\d+)\.\d+\b", line.text)
        if match and line.left <= 220 and line.top <= 140:
            numeric_prefixes.append((line.page, int(match.group(1)), line.top))
    if numeric_prefixes:
        numeric_prefixes.sort()
        return str(numeric_prefixes[0][1])
    appendix = re.search(r"\b([A-Z])\.\d+\b", sample)
    if appendix:
        return appendix.group(1)
    return str(chapter)


def is_noise(text: str) -> bool:
    if not text:
        return True
    if len(text) < 3:
        return True
    if re.fullmatch(r"[\W_]+", text):
        return True
    if re.fullmatch(r"[A-Z]?\d+[A-Z]?", text):
        return True
    if re.match(r"^(Chapter|Section)\b", text):
        return True
    if re.match(r"^(Figure|Table)\b", text):
        return True
    return False


def combine_section_heading(lines: list[Line], index: int, prefix: str) -> str:
    line = lines[index]
    section_re = re.compile(rf"^({re.escape(prefix)}\.\d+)\b(.*)$")
    match = section_re.match(line.text)
    if not match:
        return line.text
    label, rest = match.groups()
    rest = clean_text(rest)
    if rest:
        return f"{label} {rest}"
    preferred: list[Line] = []
    fallback: list[Line] = []
    for offset in range(1, 7):
        j = index + offset
        if j >= len(lines) or lines[j].page != line.page:
            break
        candidate = lines[j]
        if candidate.top - line.top > 90:
            break
        if is_noise(candidate.text):
            continue
        if re.match(r"^(THEOREM|DEFINITION|LEMMA|COROLLARY|PROPOSITION|EXAMPLE)\b", candidate.text, re.I):
            continue
        if re.match(r"^[A-Z]?\d+\.", candidate.text):
            continue
        if candidate.left <= 150:
            preferred.append(candidate)
        else:
            fallback.append(candidate)
    if preferred:
        best = sorted(preferred, key=lambda item: (item.top, item.left))[0]
        return f"{label} {best.text}"
    if fallback:
        best = sorted(fallback, key=lambda item: (item.top, item.left))[0]
        return f"{label} {best.text}"
    return label


def extract_sections(lines: list[Line], prefix: str) -> list[Heading]:
    section_re = re.compile(rf"^{re.escape(prefix)}\.\d+\b", re.I)
    seen: set[str] = set()
    sections: list[Heading] = []
    for i, line in enumerate(lines):
        if section_re.match(line.text):
            text = combine_section_heading(lines, i, prefix)
            if text not in seen:
                sections.append(Heading(page=line.page, top=line.top, text=text))
                seen.add(text)
    return sections


def extract_loose_ocr_sections(lines: list[Line], prefix: str) -> list[Heading]:
    if not prefix.isdigit():
        return []
    sections: list[Heading] = []
    for line in lines:
        if not line.is_ocr:
            continue
        if line.top > 120 or line.left > 220:
            continue
        text = line.text
        m = re.match(r"^([1-9])\s+([A-Z][A-Za-z].+)$", text)
        if m:
            sections.append(Heading(page=line.page, top=line.top, text=f"{prefix}.{m.group(1)} {clean_text(m.group(2))}"))
    return sections


def label_of(text: str) -> str:
    match = re.match(r"^([A-Z]?\d+\.\d+)\b", text)
    return match.group(1) if match else text


def readability_score(text: str) -> tuple[int, int, int]:
    alpha = sum(ch.isalpha() for ch in text)
    weird = sum(not (ch.isalnum() or ch.isspace() or ch in ".'-:,()") for ch in text)
    return (alpha - weird * 4, -weird, -len(text))


def merge_sections(*section_lists: list[Heading]) -> list[Heading]:
    by_label: dict[str, Heading] = {}
    for sections in section_lists:
        for heading in sections:
            label = label_of(heading.text)
            current = by_label.get(label)
            if current is None or readability_score(heading.text) > readability_score(current.text):
                by_label[label] = heading
    merged = sorted(by_label.values(), key=lambda item: (item.page, item.top))
    return dedupe_headings(merged)


def normalize_heading_text(text: str) -> str:
    text = clean_text(text)
    text = re.sub(r"\s*\.\s*$", "", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text


def title_word_ratio(text: str) -> float:
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", text)
    if not words:
        return 0.0
    keep_lower = {"of", "and", "the", "with", "to", "for", "by", "in", "on", "at", "or", "part"}
    good = 0
    for word in words:
        if word.lower() in keep_lower or word[0].isupper():
            good += 1
    return good / len(words)


def likely_heading_fragment(line: Line, base_metric: float, prefix: str) -> bool:
    text = line.text
    if is_noise(text):
        return False
    if re.match(rf"^{re.escape(prefix)}\.\d+\b", text, re.I):
        return False
    if re.match(r"^Exercises\s+[A-Z]?\d+\.\d+", text, re.I):
        return True
    if re.match(r"^(THEOREM|DEFINITION|LEMMA|COROLLARY|PROPOSITION|EXAMPLE)\b", text, re.I):
        return False
    if re.match(r"^(Proof|Solution|Suppose|Show that|Evaluate|Derive|Find|Using)\b", text, re.I):
        return False
    if re.match(r"^[A-Z]?\d+\s*=", text):
        return False
    if re.match(r"^\d+\.", text):
        return False
    if line.left > 280:
        return False
    alpha = sum(ch.isalpha() for ch in text)
    digits = sum(ch.isdigit() for ch in text)
    if alpha < 3:
        return False
    if digits > max(2, alpha * 0.18):
        return False
    if any(ch in text for ch in "=<>[]{}|\\"):
        return False
    max_len = 70 if line.is_ocr else 90
    if len(text) > max_len:
        return False
    letters = [ch for ch in text if ch.isalpha()]
    upper_ratio = sum(ch.isupper() for ch in letters) / len(letters) if letters else 0.0
    title_like = title_word_ratio(text) >= 0.75
    all_caps = upper_ratio > 0.7 and len(text.split()) >= 2
    if line.is_ocr:
        if line.confidence < 55:
            return False
        big = line.height >= base_metric * 1.6
        return all_caps or (big and title_like)
    font_bold = any("Bold" in font for font in line.fonts)
    big = line.metric >= max(15.5, base_metric * 1.18)
    return all_caps or (big and font_bold) or (big and title_like)


def merge_heading_fragments(lines: list[Line], base_metric: float, prefix: str) -> list[Heading]:
    headings: list[Heading] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not likely_heading_fragment(line, base_metric, prefix):
            i += 1
            continue
        parts = [line.text]
        start_page = line.page
        start_top = line.top
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            gap = nxt.top - lines[j - 1].top
            if nxt.page != start_page:
                break
            if gap > max(line.height, nxt.height) * 1.8 + 12:
                break
            if abs(nxt.left - line.left) > 60:
                break
            if not likely_heading_fragment(nxt, base_metric, prefix):
                break
            parts.append(nxt.text)
            j += 1
        merged = normalize_heading_text(" ".join(parts))
        if merged and not re.match(r"^(THEOREM|DEFINITION|LEMMA|COROLLARY|PROPOSITION|EXAMPLE)\b", merged, re.I):
            headings.append(Heading(page=start_page, top=start_top, text=merged))
        i = j
    return dedupe_headings(headings)


def dedupe_headings(headings: list[Heading]) -> list[Heading]:
    deduped: list[Heading] = []
    last_key: tuple[int, str] | None = None
    for heading in sorted(headings, key=lambda item: (item.page, item.top)):
        key = (heading.page, heading.text.lower())
        if last_key == key:
            continue
        if deduped and deduped[-1].text.lower() == heading.text.lower() and abs(deduped[-1].page - heading.page) <= 1:
            continue
        deduped.append(heading)
        last_key = key
    return deduped


def fragment_like(text: str) -> bool:
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", text)
    if not words:
        return False
    letters = [ch for ch in text if ch.isalpha()]
    upper_ratio = sum(ch.isupper() for ch in letters) / len(letters) if letters else 0.0
    return len(text) <= 40 or upper_ratio > 0.65 or title_word_ratio(text) >= 0.8


def coalesce_fragmented_headings(headings: list[Heading]) -> list[Heading]:
    if not headings:
        return headings
    merged: list[Heading] = []
    current = headings[0]
    for nxt in headings[1:]:
        if (
            nxt.page == current.page
            and fragment_like(current.text)
            and fragment_like(nxt.text)
            and 0 <= nxt.top - current.top <= 46
        ):
            current = Heading(
                page=current.page,
                top=current.top,
                text=normalize_heading_text(f"{current.text} {nxt.text}"),
            )
            continue
        merged.append(current)
        current = nxt
    merged.append(current)
    return dedupe_headings(merged)


def filter_subsections(
    headings: list[Heading], sections: list[Heading], top_title: str
) -> list[Heading]:
    section_pages = {(section.page, section.text.lower()) for section in sections}
    filtered: list[Heading] = []
    for heading in headings:
        if heading.text.lower() == top_title.lower():
            continue
        if (heading.page, heading.text.lower()) in section_pages:
            continue
        if heading.text.lower().startswith("chapter "):
            continue
        filtered.append(heading)
    return coalesce_fragmented_headings(filtered)


def build_toc(title: str, sections: list[Heading], subsections: list[Heading]) -> list[list[object]]:
    toc: list[list[object]] = [[1, title, 1]]
    sorted_sections = sorted(sections, key=lambda item: (item.page, item.top))
    sorted_subs = sorted(subsections, key=lambda item: (item.page, item.top))
    section_ranges: list[tuple[Heading, int, int]] = []
    for idx, section in enumerate(sorted_sections):
        start_page = section.page
        end_page = sorted_sections[idx + 1].page - 1 if idx + 1 < len(sorted_sections) else 10**9
        section_ranges.append((section, start_page, end_page))
        toc.append([2, section.text, section.page])
        for sub in sorted_subs:
            if start_page <= sub.page <= end_page:
                if sub.page == section.page and sub.top <= section.top + 12:
                    continue
                toc.append([3, sub.text, sub.page])
    return toc


def process_pdf(path: Path) -> tuple[Path, int]:
    doc = fitz.open(path)
    chapter = chapter_number(path)
    title = title_from_filename(path)
    text_lines = extract_text_lines(doc)
    ocr_lines = extract_ocr_lines(doc)
    ocr_lines.sort(key=lambda item: (item.page, item.top, item.left))
    text_lines.sort(key=lambda item: (item.page, item.top, item.left))
    prefix = infer_section_prefix(text_lines or ocr_lines, chapter)
    sections = merge_sections(
        extract_sections(text_lines, prefix),
        extract_sections(ocr_lines, prefix),
        extract_loose_ocr_sections(ocr_lines, prefix),
    )
    metric = body_metric(ocr_lines)
    subsection_candidates = merge_heading_fragments(ocr_lines, metric, prefix)
    subsections = filter_subsections(subsection_candidates, sections, title)
    toc = build_toc(title, sections, subsections)
    out_path = path.with_name(f"{path.stem} - bookmarked.pdf")
    doc.set_toc(toc)
    doc.save(out_path, garbage=3, deflate=True)
    doc.close()
    return out_path, len(toc)


def chapter_pdfs(start: int, end: int) -> list[Path]:
    paths: list[Path] = []
    for chapter in range(start, end + 1):
        matches = sorted(BASE_DIR.glob(f"Chapter {chapter:02d}*/original copy/Chapter *.pdf"))
        for path in matches:
            if "bookmarked" in path.stem.lower():
                continue
            paths.append(path)
    return paths


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=5)
    parser.add_argument("--end", type=int, default=18)
    args = parser.parse_args()

    pdfs = chapter_pdfs(args.start, args.end)
    for path in pdfs:
        out_path, entries = process_pdf(path)
        print(f"{path.name} -> {out_path.name} ({entries} bookmarks)")


if __name__ == "__main__":
    main()

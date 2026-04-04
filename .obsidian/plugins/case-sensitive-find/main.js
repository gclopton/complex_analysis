const { MarkdownView, Notice, Plugin, TextComponent } = require("obsidian");

function isModF(event) {
  return (event.metaKey || event.ctrlKey) && !event.shiftKey && !event.altKey && String(event.key).toLowerCase() === "f";
}

function eventTargetsView(event, view) {
  const target = event.target;
  const activeElement = document.activeElement;

  if (!view?.containerEl) {
    return false;
  }

  if (target?.closest?.(".modal, .suggestion-container, .menu")) {
    return false;
  }

  return Boolean(
    (target && view.containerEl.contains(target)) ||
    (activeElement && view.containerEl.contains(activeElement))
  );
}

function toDisplayCount(index, total) {
  if (!total) {
    return "0 / 0";
  }
  return `${index + 1} / ${total}`;
}

function getEditorText(editor) {
  return editor ? editor.getValue() : "";
}

function posToOffset(editor, pos) {
  if (editor && typeof editor.posToOffset === "function") {
    return editor.posToOffset(pos);
  }

  let offset = 0;
  for (let line = 0; line < pos.line; line += 1) {
    offset += editor.getLine(line).length + 1;
  }
  return offset + pos.ch;
}

function offsetToPos(editor, offset) {
  if (editor && typeof editor.offsetToPos === "function") {
    return editor.offsetToPos(offset);
  }

  let remaining = offset;
  const lastLine = editor.lineCount() - 1;
  for (let line = 0; line <= lastLine; line += 1) {
    const text = editor.getLine(line);
    if (remaining <= text.length) {
      return { line, ch: remaining };
    }
    remaining -= text.length + 1;
  }

  return { line: lastLine, ch: editor.getLine(lastLine).length };
}

function getSelectionOffsets(editor) {
  const from = editor.getCursor("from");
  const to = editor.getCursor("to");
  return {
    from: posToOffset(editor, from),
    to: posToOffset(editor, to),
  };
}

function findAllMatches(text, query, matchCase) {
  const source = String(text || "");
  const needle = String(query || "");
  if (!needle) {
    return [];
  }

  const haystack = matchCase ? source : source.toLocaleLowerCase();
  const searchNeedle = matchCase ? needle : needle.toLocaleLowerCase();
  const matches = [];

  let fromIndex = 0;
  while (fromIndex <= haystack.length - searchNeedle.length) {
    const found = haystack.indexOf(searchNeedle, fromIndex);
    if (found === -1) {
      break;
    }

    matches.push({
      from: found,
      to: found + needle.length,
    });

    fromIndex = found + Math.max(searchNeedle.length, 1);
  }

  return matches;
}

class CaseFindBar {
  constructor(plugin) {
    this.plugin = plugin;
    this.view = null;
    this.editor = null;
    this.matches = [];
    this.currentIndex = -1;
    this.query = "";
    this.matchCase = false;
    this.containerEl = null;
    this.inputComponent = null;
    this.countEl = null;
    this.matchCaseButton = null;
    this.hasCommittedSelection = false;
    this.highlightRoots = [];
  }

  isOpen() {
    return Boolean(this.containerEl);
  }

  open(view) {
    if (!(view instanceof MarkdownView) || !view.editor) {
      new Notice("Open a Markdown note to search.");
      return;
    }

    if (this.view !== view) {
      this.close();
    }

    this.view = view;
    this.editor = view.editor;
    this.setHighlightScope(view);

    if (!this.containerEl) {
      this.build();
      this.view.contentEl.prepend(this.containerEl);
    }

    const selection = this.editor.getSelection();
    if (selection && selection.indexOf("\n") === -1) {
      this.query = selection;
      this.inputComponent.setValue(selection);
    }

    this.refresh(true);
    window.setTimeout(() => {
      this.inputComponent.inputEl.focus();
      this.inputComponent.inputEl.select();
    }, 0);
  }

  close() {
    if (this.containerEl) {
      this.containerEl.detach();
      this.containerEl = null;
    }

    this.clearHighlightScope();

    this.view = null;
    this.editor = null;
    this.matches = [];
    this.currentIndex = -1;
    this.inputComponent = null;
    this.countEl = null;
    this.matchCaseButton = null;
    this.hasCommittedSelection = false;
    this.highlightRoots = [];
  }

  setHighlightScope(view) {
    this.clearHighlightScope();

    const roots = new Set();
    if (view?.containerEl) {
      roots.add(view.containerEl);
    }
    if (view?.contentEl) {
      roots.add(view.contentEl);
      view.contentEl.querySelectorAll(".markdown-source-view.mod-cm6, .cm-editor").forEach((el) => roots.add(el));
    }

    this.highlightRoots = Array.from(roots);
    this.highlightRoots.forEach((el) => {
      el.addClass("case-find-active");
      el.style.setProperty("--text-selection", "var(--text-highlight-bg)");
    });
  }

  clearHighlightScope() {
    this.highlightRoots.forEach((el) => {
      el.removeClass("case-find-active");
      el.style.removeProperty("--text-selection");
    });
    this.highlightRoots = [];
  }

  build() {
    const container = createDiv({ cls: "case-find-bar" });
    this.containerEl = container;

    const inputWrapper = container.createDiv({ cls: "case-find-input" });
    this.inputComponent = new TextComponent(inputWrapper);
    this.inputComponent.inputEl.placeholder = "Find in current note";
    this.inputComponent.onChange((value) => {
      this.query = value;
      this.refresh(true);
    });
    this.inputComponent.inputEl.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        event.preventDefault();
        event.shiftKey ? this.previous() : this.next();
        return;
      }

      if (event.key === "Escape") {
        event.preventDefault();
        this.close();
      }
    });

    this.countEl = container.createDiv({
      cls: "case-find-count",
      text: "0 / 0",
    });

    this.matchCaseButton = container.createEl("button", {
      cls: "case-find-button",
      text: "Aa",
      attr: { type: "button", "aria-label": "Toggle match case" },
    });
    this.matchCaseButton.addEventListener("click", () => {
      this.matchCase = !this.matchCase;
      this.refresh(true);
    });

    const prevButton = container.createEl("button", {
      cls: "case-find-button mod-icon",
      text: "↑",
      attr: { type: "button", "aria-label": "Previous match" },
    });
    prevButton.addEventListener("click", () => this.previous());

    const nextButton = container.createEl("button", {
      cls: "case-find-button mod-icon",
      text: "↓",
      attr: { type: "button", "aria-label": "Next match" },
    });
    nextButton.addEventListener("click", () => this.next());

    const closeButton = container.createEl("button", {
      cls: "case-find-button mod-icon",
      text: "×",
      attr: { type: "button", "aria-label": "Close find bar" },
    });
    closeButton.addEventListener("click", () => this.close());
  }

  refresh(fromQueryChange = false) {
    if (!this.editor || !this.inputComponent) {
      return;
    }

    this.query = this.inputComponent.getValue();
    this.matches = findAllMatches(getEditorText(this.editor), this.query, this.matchCase);
    this.matchCaseButton.toggleClass("is-active", this.matchCase);

    if (this.matches.length === 0) {
      this.currentIndex = -1;
      this.hasCommittedSelection = false;
      this.countEl.setText("0 / 0");
      this.inputComponent.inputEl.parentElement.toggleClass("mod-no-match", Boolean(this.query));
      return;
    }

    this.inputComponent.inputEl.parentElement.removeClass("mod-no-match");

    if (fromQueryChange || this.currentIndex < 0 || this.currentIndex >= this.matches.length) {
      this.currentIndex = this.findNearestMatchIndex();
      this.hasCommittedSelection = false;
    }

    this.countEl.setText(toDisplayCount(this.currentIndex, this.matches.length));
  }

  findNearestMatchIndex() {
    if (!this.editor || this.matches.length === 0) {
      return -1;
    }

    const selection = getSelectionOffsets(this.editor);
    const exactIndex = this.matches.findIndex((match) =>
      match.from === selection.from && match.to === selection.to
    );
    if (exactIndex !== -1) {
      return exactIndex;
    }

    const nextIndex = this.matches.findIndex((match) => match.from >= selection.to);
    return nextIndex !== -1 ? nextIndex : 0;
  }

  selectCurrentMatch() {
    if (!this.editor || this.currentIndex < 0 || this.currentIndex >= this.matches.length) {
      return;
    }

    const match = this.matches[this.currentIndex];
    const from = offsetToPos(this.editor, match.from);
    const to = offsetToPos(this.editor, match.to);

    if (this.view?.editor?.cm) {
      this.view.editor.cm.dispatch({
        selection: { anchor: match.from, head: match.to },
        scrollIntoView: true,
      });
      this.view.editor.cm.focus();
    } else {
      this.editor.setSelection(from, to);
      this.editor.focus();
    }

    this.countEl.setText(toDisplayCount(this.currentIndex, this.matches.length));
    this.hasCommittedSelection = true;
  }

  next() {
    if (this.matches.length === 0) {
      this.refresh(true);
      return;
    }

    if (!this.hasCommittedSelection) {
      this.selectCurrentMatch();
      return;
    }

    this.currentIndex = (this.currentIndex + 1) % this.matches.length;
    this.selectCurrentMatch();
  }

  previous() {
    if (this.matches.length === 0) {
      this.refresh(true);
      return;
    }

    if (!this.hasCommittedSelection) {
      this.selectCurrentMatch();
      return;
    }

    this.currentIndex = (this.currentIndex - 1 + this.matches.length) % this.matches.length;
    this.selectCurrentMatch();
  }
}

module.exports = class CaseSensitiveFindPlugin extends Plugin {
  async onload() {
    this.findBar = new CaseFindBar(this);
    this.originalOpenSearchCommand = null;
    this.patchNativeOpenSearchCommand();

    this.addCommand({
      id: "open-case-sensitive-find",
      name: "Open case-sensitive find",
      hotkeys: [{ modifiers: ["Mod"], key: "f" }],
      checkCallback: (checking) => {
        const view = this.app.workspace.getActiveViewOfType(MarkdownView);
        if (!view || !view.editor) {
          return false;
        }

        if (!checking) {
          this.findBar.open(view);
        }
        return true;
      },
    });

    this.registerEvent(
      this.app.workspace.on("active-leaf-change", (leaf) => {
        if (!(leaf?.view instanceof MarkdownView)) {
          this.findBar.close();
          return;
        }

        if (this.findBar.isOpen()) {
          this.findBar.open(leaf.view);
        }
      })
    );

    this.registerEvent(
      this.app.workspace.on("editor-change", (_editor, info) => {
        if (!this.findBar.isOpen()) {
          return;
        }

        if (info?.file?.path !== this.findBar.view?.file?.path) {
          return;
        }

        this.findBar.refresh(false);
      })
    );
  }

  patchNativeOpenSearchCommand() {
    const commands = this.app?.commands?.commands;
    const openSearchCommand = commands?.["editor:open-search"];

    if (!openSearchCommand || typeof openSearchCommand.checkCallback !== "function") {
      return;
    }

    this.originalOpenSearchCommand = openSearchCommand.checkCallback;
    openSearchCommand.checkCallback = (checking) => {
      const view = this.app.workspace.getActiveViewOfType(MarkdownView);
      if (!view || !view.editor) {
        return this.originalOpenSearchCommand(checking);
      }

      if (!checking) {
        this.findBar.open(view);
      }

      return true;
    };
  }

  onunload() {
    const commands = this.app?.commands?.commands;
    const openSearchCommand = commands?.["editor:open-search"];
    if (openSearchCommand && this.originalOpenSearchCommand) {
      openSearchCommand.checkCallback = this.originalOpenSearchCommand;
    }

    this.findBar.close();
  }
};

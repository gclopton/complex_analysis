# Case Sensitive Find Plugin

This note documents the vault-local `Case Sensitive Find` plugin and the technical details of how it was built, so you can maintain, modify, or promote it to the ObsidianConfig template later.

## Purpose

Obsidian's native in-note `Ctrl+F`/`Cmd+F` find bar does not expose a straightforward match-case toggle. This plugin replaces the in-editor search and replace with a custom find bar that supports case-sensitive searching and case-sensitive replace.

The plugin stays vault-local, hooking Obsidian's `editor:open-search` and `editor:open-search-replace` commands so that `Cmd+F` and `Cmd+Option+F` open the custom UI instead of the native search bar.

## Plugin Files

The plugin lives at `.obsidian/plugins/case-sensitive-find/` and consists of three files:

- `manifest.json` — standard Obsidian plugin manifest (id: `case-sensitive-find`, version 0.1.0)
- `main.js` — all plugin logic in a single plain-JS file (no build step required)
- `styles.css` — styling for the find bar and match highlight decorations

It must also be listed in `.obsidian/community-plugins.json` to be enabled. Note: if the plugin ever fails to load, Obsidian silently removes it from this list, so you'd need to re-add it.

## What It Does

When the active pane is a Markdown editor, pressing `Cmd+F` opens a custom find bar instead of the native search bar. Pressing `Cmd+Option+F` opens the same bar in replace mode.

The custom bar provides: a search input, an optional replace input, a match counter, next/previous navigation, a case-sensitive toggle (`Aa`), Replace and Replace All actions, and a close button (`Escape` also closes it).

If text is selected before opening the bar, that text pre-fills the search query.

All matches are highlighted simultaneously in the editor. The active match is bright yellow and the inactive matches are cyan, making it easy to see all occurrences at a glance while navigating between them.

## Architecture — The Key Pattern

This is the most important section if you ever need to debug or extend this plugin. The highlight system went through five iterations before landing on the approach that works.

### What Works: ViewPlugin.fromClass()

The working approach uses CodeMirror 6's `ViewPlugin.fromClass()` with an explicit decorations accessor. This pattern was discovered by examining the `obsidian-keyword-highlighter` community plugin source code.

The architecture has three pieces:

**1. Shared mutable state (module-level object):**

```js
const highlightState = { matches: [], activeIndex: -1 };
```

The UI code (CaseFindBar) writes match positions into this object whenever the search query changes or the user navigates. The CM6 ViewPlugin reads from it when building decorations.

**2. ViewPlugin that reads from shared state:**

```js
class FindHighlighter {
  constructor(_view) {
    this.decorations = this.buildDecorations();
  }
  update(upd) {
    if (upd.docChanged || upd.viewportChanged) {
      this.decorations = this.buildDecorations();
    }
  }
  buildDecorations() {
    const { matches, activeIndex } = highlightState;
    if (!matches || matches.length === 0) return CmDecoration.none;
    const builder = new CmRangeSetBuilder();
    for (let i = 0; i < matches.length; i++) {
      const m = matches[i];
      builder.add(m.from, m.to,
        i === activeIndex ? activeMatchMark : inactiveMatchMark);
    }
    return builder.finish();
  }
}

findHighlighterExt = CmViewPlugin.fromClass(FindHighlighter, {
  decorations: (v) => v.decorations,
});
```

The `{ decorations: (v) => v.decorations }` option is critical — it tells CM6 how to extract the decoration set from the plugin instance.

**3. Repaint function for external updates:**

```js
function repaintHighlights(cmEditorView) {
  const pluginInstance = cmEditorView.plugin(findHighlighterExt);
  if (pluginInstance) {
    pluginInstance.decorations = pluginInstance.buildDecorations();
    cmEditorView.requestMeasure();
  }
}
```

When the user types in the search box or navigates between matches, the UI code updates `highlightState` and then calls `repaintHighlights()`. This mutates the plugin's decorations directly and calls `requestMeasure()` to trigger a CM6 repaint.

**Registration** uses `this.registerEditorExtension(findHighlighterExt)` in the plugin's `onload()`.

### What Didn't Work (and Why)

Understanding the failed approaches is important for future debugging:

**Attempt 1 — StateField with EditorView.decorations.from():** This is the "textbook" CM6 approach for providing decorations from a StateField. The plugin crashed on load because `EditorView.decorations.from()` is not accessible in this Obsidian build. When the plugin fails to load, Obsidian removes it from `community-plugins.json`, so you have to re-add it.

**Attempt 2 — StateField with safety guards:** Added try-catch around the `EditorView.decorations.from()` call. The plugin loaded, but the StateField was null (correctly guarded), so no inactive-match decorations appeared.

**Attempt 3 — Native search API (setSearchQuery):** Tried dispatching CM6 search state effects to piggyback on Obsidian's native `cm-searchMatch` CSS. The dispatches went through but never produced visible decorations — likely because Obsidian's bundled search extension handles rendering internally in a way that doesn't respond to external state changes.

**Attempt 4 — CSS Custom Highlight API:** Tried `CSS.highlights` and `document.createRange()` with `cmView.domAtPos()`. Either the Electron version doesn't fully support the Highlight API, or the DOM position mapping wasn't working correctly. No highlights appeared.

**Attempt 5 — ViewPlugin.fromClass() (this is the one that works).** The key insight from the keyword-highlighter reference plugin was that `ViewPlugin.fromClass()` with the `decorations` accessor completely bypasses the `EditorView.decorations` facet, which is what all the earlier approaches depended on.

### CM6 Import Pattern

The plugin imports CM6 modules using separate try-catch blocks so that one missing module doesn't prevent the rest of the plugin from loading:

```js
let cmState = null;
let cmView = null;
try { cmState = require("@codemirror/state"); } catch (_e) {}
try { cmView = require("@codemirror/view"); } catch (_e) {}
```

Individual classes are then extracted with null checks. The entire ViewPlugin setup is wrapped in try-catch so the plugin can still function as a basic search bar even if decoration support fails.

## CSS Classes

The plugin defines these decoration classes:

- `.case-find-active-match` — bright yellow background with gold inset border (applied to the currently selected match)
- `.case-find-secondary-match` — cyan background with teal inset border (applied to all other matches)
- `.case-find-active .cm-selectionBackground` — overrides the native selection background to bright yellow while the find bar is open, so the active match stays visible
- `.case-find-active .cm-panel.cm-search` — hides any native search panel that might leak through

The find bar itself uses `.case-find-bar`, `.case-find-row`, `.case-find-input`, `.case-find-count`, and `.case-find-button` classes, all styled to blend with Obsidian's CSS variables.

## Active Match Visibility

While the find bar is open, the plugin sets `--text-selection` on the editor container element to bright yellow so that the CM6 selection (which follows the active match) stays visually prominent. This is cleared when the bar closes.

## Command Interception

The plugin intercepts native search in two ways:

1. **Command patching:** On load, it patches `editor:open-search` and `editor:open-search-replace` via Obsidian's command registry so they open the custom bar instead.

2. **DOM keydown capture:** A capture-phase keydown listener on `document` intercepts `Cmd+F` and `Cmd+Option+F` before Obsidian's own handlers can respond, calling `preventDefault()` and opening the custom bar.

Both paths converge on `openFindBar(replace)`, which creates or shows the `CaseFindBar` component in the active MarkdownView.

## Promoting to ObsidianConfig Template

When you're satisfied the plugin is stable, here's how to add it to your vault formation template at `~/utils/ObsidianConfig`:

1. **Copy the plugin folder:**
   ```
   cp -r ~/ObsidianVaults/real_analysis/.obsidian/plugins/case-sensitive-find \
         ~/utils/ObsidianConfig/plugins/case-sensitive-find
   ```

2. **Add to community-plugins.json:**
   Open `~/utils/ObsidianConfig/community-plugins.json` and add `"case-sensitive-find"` to the JSON array.

3. **That's it.** The plugin has no `data.json` settings file, so there's nothing else to copy. Any new vault created from the template will have it available.

The ObsidianConfig template structure mirrors what goes inside `.obsidian/`: it has `plugins/` with one subfolder per plugin (containing `main.js`, `manifest.json`, and optionally `styles.css` and `data.json`), plus top-level config files like `community-plugins.json`, `hotkeys.json`, `appearance.json`, etc. The `vault-root/` folder contains files that go in the vault root rather than inside `.obsidian/`.

## Verification

The plugin JavaScript passes `node -c` syntax checking. The manifest.json and community-plugins.json are valid JSON. The plugin is currently deployed and working in both the `real_analysis` and `complex_analysis` vaults.

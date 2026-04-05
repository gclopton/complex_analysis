# Callout Tools Plugin

This note documents the vault-local `callout-tools` plugin used in the `complex_analysis` vault.

## Purpose

The plugin provides source-editing commands for callouts. Unlike the `callout-outline` plugin, which mainly adds navigation and render-time labeling, `callout-tools` performs direct Markdown edits in the active note.

The current commands are:

- `Remove current callout wrapper`
- `Move first callout line to title`
- `Number figure callouts`

## Plugin Files

The plugin code lives here:

- `.obsidian/plugins/callout-tools/manifest.json`
- `.obsidian/plugins/callout-tools/main.js`

It is enabled through:

- `.obsidian/community-plugins.json`

## Existing Editing Commands

`Remove current callout wrapper` removes one enclosing callout layer at the cursor and leaves the content behind.

`Move first callout line to title` promotes the first suitable non-empty content line into the callout header title when the callout does not already have a title.

## Figure Numbering Command

`Number figure callouts` works on the active Markdown note and rewrites actual `[!figure]` callout header titles in source order.

This was added after the render-only numbering experiment for figures turned out to be a poor fit. Figure references in the body text need stable handwritten numbering, so figures should be renumbered in the Markdown source rather than only at render time.

### Matching scope

The command only renumbers real `[!figure]` callout headers.

It skips:

- non-figure callout types
- fake callout syntax inside fenced code blocks

### Rewrite rules

The command walks figure callouts in note order and rewrites each header title to match its sequential position.

It handles these cases:

- no title: `> [!figure]` becomes `> [!figure] Figure N`
- plain title: `> [!figure] Contour around poles` becomes `> [!figure] Figure N: Contour around poles`
- existing numbered title: `> [!figure] Figure 12` becomes `> [!figure] Figure N`
- existing numbered title with text: `> [!figure] Figure 12: Contour around poles` becomes `> [!figure] Figure N: Contour around poles`
- subfigure title: `> [!figure] Figure 2(a)` becomes `> [!figure] Figure N(a)`
- alternate subfigure title: `> [!figure] Figure 2a` becomes `> [!figure] Figure N(a)`
- alternate dotted subfigure title: `> [!figure] Figure 2.a` becomes `> [!figure] Figure N(a)`
- subfigure title with text: `> [!figure] Figure 2(a): Contour around poles` becomes `> [!figure] Figure N(a): Contour around poles`
- alternate subfigure title with text: `> [!figure] Figure 2a: Contour around poles` or `> [!figure] Figure 2.a: Contour around poles` becomes `> [!figure] Figure N(a): Contour around poles`

So the command strips an existing `Figure ...` prefix when present, preserves any remaining descriptive title text, and writes the updated numbering back into the header line. Alternate subfigure formats are normalized to the canonical parenthesized form.

## Safety Notes

The implementation only edits header lines. It does not rewrite callout bodies or surrounding prose.

Because it edits the active editor contents directly, ordinary Obsidian undo can revert the change if needed.

## Verification

The plugin file was syntax-checked with `node -c` after the command was added.

## Why This Lives Here

This is still a vault-local experiment. If the command keeps working well in real use, it can later be promoted into the shared vault template and other vaults.

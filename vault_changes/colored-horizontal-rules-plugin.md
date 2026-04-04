# Colored Horizontal Rules Plugin

This note documents the vault-local `Colored Horizontal Rules` plugin added to the `complex_analysis` vault.

## Purpose

The goal is to let horizontal-rule-like separators use different colors based on simple source markers, while still working in the editor where this vault is normally used.

The main motivation was to keep ordinary three-dash rules available for their existing use in notes, while allowing a different visual separator for special cases such as OCR page layout boundaries.

## Behavior

The plugin now distinguishes separators by source syntax:

- `---` keeps the normal Obsidian rule style.
- `+++` is a plugin-owned custom separator with its own color slot.
- `++++` is a plugin-owned custom separator and is the recommended OCR body/margin separator.
- `+++++`, `++++++`, `+++++++`, and `++++++++` can also each have their own colors.

The initial default palette is:

- `+++` very light gray-white
- `++++` bright yellow
- `+++++` orange
- `++++++` red
- `+++++++` green
- `++++++++` blue

All of these are configurable through the plugin settings tab.

## Plugin Files

The vault-local plugin lives here:

- `.obsidian/plugins/colored-horizontal-rules/manifest.json`
- `.obsidian/plugins/colored-horizontal-rules/main.js`
- `.obsidian/plugins/colored-horizontal-rules/styles.css`
- `.obsidian/plugins/colored-horizontal-rules/data.json`

It is enabled in:

- `.obsidian/community-plugins.json`

## Implementation Approach

This was implemented as a vault-local JavaScript plugin rather than a CSS snippet.

That choice was necessary because once Markdown is rendered, both `---` and `----` become the same `<hr>` element in HTML, and theme CSS can override their editor appearance in hard-to-control ways.

The plugin therefore has two pieces:

1. a rendered-Markdown postprocessor that tags native `hr` elements by dash count and converts plus-based separator paragraphs into plugin-owned rule blocks, and
2. a CodeMirror editor extension that decorates source lines made entirely of hyphens or plus signs.

For rendered sections, the plugin:

1. inspects the rendered section for `<hr>` elements,
2. uses Obsidian section source info to read the original Markdown lines,
3. matches each rendered rule to the corresponding source line,
4. tags the rendered rule with a dash-count-specific class such as `colored-horizontal-rule-4`,
5. converts plus-only paragraphs such as `+++` or `++++` into plugin-owned rule blocks,
6. and then lets CSS color those blocks.

For the editor, the plugin:

1. scans visible CodeMirror lines,
2. finds lines that consist only of `---`, `+++`, `++++`, and so on,
3. attaches dash-count and marker-type classes such as `colored-horizontal-rule-source-plus` and `colored-horizontal-rule-source-4`,
4. keeps the plus-based separators on the real source line so they remain editable,
5. suppresses the overlay while a plus-based separator line is active,
6. and draws the colored rule with CSS when the line is inactive.

## Settings

The plugin adds a settings tab:

- `Settings -> Colored Horizontal Rules`

That tab exposes color pickers for counts `3` through `8` and a reset button for the default palette.

## Current Behavior In The Editor

This plugin now targets both rendered Markdown and the CodeMirror editor used by Live Preview and source editing.

The final stable path is the plus-based one, not the dash-based one. In practice:

- use `---` for ordinary native Obsidian rules,
- use `+++` for a configurable neutral divider,
- use `++++` for the bright yellow special separator,
- and use longer plus runs if additional custom colors are useful.

In the editor, plus-based separators remain on the actual source line. When the line is inactive, the rule is visually dominant. When the line is active, the overlay is suppressed so the source markers stay editable.

The only remaining uncertainty is ordinary vault-local plugin behavior in Obsidian itself: after changing the plugin code, the vault may need a plugin reload or an Obsidian restart before all open notes pick up the new editor decorations cleanly.

## Relation to the OCR Workflow

The margin-heavy Mathpix OCR script was originally updated to emit `----` instead of `---`.

After the Blue Topaz conflict, the better long-term plan is to switch that OCR separator to `++++` instead, because the plus-based path is plugin-owned and does not rely on the theme’s native horizontal-rule behavior.

## Verification Performed

The plugin should be checked in four ways before promoting it more broadly:

1. confirm that ordinary `---` rules still render normally,
2. confirm that `+++` and `++++` render correctly in the editor as well as in rendered Markdown,
3. confirm that changing the color pickers updates both editor and rendered styling,
4. and confirm that editing the active plus-based separator line still feels usable.

## Promotion Path Later

If this behaves well in `complex_analysis`, the later rollout path is:

1. copy the plugin folder into the shared vault template,
2. add the plugin id to the shared `community-plugins.json`,
3. copy the plugin `data.json` defaults if the same palette is desired,
4. and then install it in older vaults where colored rule separation is useful.

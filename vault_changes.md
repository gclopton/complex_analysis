# Vault Changes

This note records the Obsidian-vault changes made during this session so they can be ported into the vault generator.

Newer, change-specific documentation now lives in:

- `vault_changes/`

This root note is being left in place for earlier session history.

## Image Alignment Flags

The vault now supports Markdown image alignment flags of the form

```md
![450|left](./images/example.png)
![450|center](./images/example.png)
![450|right](./images/example.png)

![|left](./images/example.png)
![|center](./images/example.png)
![|right](./images/example.png)

![|left|450](./images/example.png)
![|center|450](./images/example.png)
![|right|450](./images/example.png)
```

Both alignment-token orders are now supported:

```md
![450|center](./images/example.png)
![|center|450](./images/example.png)
```

Plain images without an alignment flag still use the normal Obsidian or theme default:

```md
![450](./images/example.png)
![](./images/example.png)
```

### Files changed

The following files were added or updated:

- `.obsidian/snippets/codex-image-align-flags.css`
- `.obsidian/appearance.json`

### What was added

A CSS snippet was added to target image alt text containing the alignment tokens `|left|`, `|center|`, or `|right|`, as well as the alignment-last forms ending in `|left`, `|center`, or `|right`. The snippet intentionally does not affect plain images.

The snippet also targets the surrounding `.image-embed` wrapper, not just the `<img>` element itself. This is necessary because the `image-tools` plugin wraps images in a width-constrained container, and centering the image node alone does not reliably center the rendered figure block.

The enabled snippet list in `.obsidian/appearance.json` was also updated to include:

```json
"codex-image-align-flags"
```

### How it was implemented

There are three moving pieces, and all three matter if this is rolled out to other vaults.

First, the vault-level syntax support is implemented by the CSS snippet

- `.obsidian/snippets/codex-image-align-flags.css`

This is the part that makes rendered Markdown respond to alignment flags in the image alt text. The snippet does two jobs:

1. It matches image alt text that either ends with `|left`, `|center`, `|right` or contains the middle-token forms `|left|`, `|center|`, `|right|`.
2. It styles both the `<img>` element and the surrounding `.image-embed` wrapper.

The wrapper targeting is important because `image-tools` sets `.image-embed { width: fit-content; }`, so centering only the image is not enough to center the whole rendered figure block.

Second, the snippet has to be enabled in

- `.obsidian/appearance.json`

by adding

```json
"codex-image-align-flags"
```

to `enabledCssSnippets`. Without that, the CSS file can exist on disk and still do nothing.

Third, the vault’s installed `image-tools` plugin affects Live Preview behavior:

- `.obsidian/plugins/image-tools/main.js`
- `.obsidian/plugins/image-tools/styles.css`

The plugin already parses alignment tokens for URL-style images from the alt text, including both orders such as

```md
![400|center](...)
![|center|400](...)
```

But the plugin originally left stale `images-tools-text-align-*` classes on the wrapper when the alignment changed. The fix was applied in the plugin’s alignment update path so that on every editor update it:

1. re-parses the current alignment token,
2. removes any old `images-tools-text-align-*` classes from the embed wrapper,
3. adds the correct current class back.

That refresh fix is what makes alignment changes update immediately in Live Preview instead of requiring the note to be reopened.

### Snippet contents

```css
/*
Supports Markdown image flags such as:

![450|left](...)
![450|center](...)
![450|right](...)
![|left](...)
![|center|450](...)
![|right|450](...)

Plain images like ![](...) or ![450](...) keep the theme default.
*/

.markdown-rendered img[alt$="|left"],
.markdown-rendered img[alt*="|left|"],
.markdown-preview-view img[alt$="|left"],
.markdown-preview-view img[alt*="|left|"],
.markdown-source-view.mod-cm6.is-live-preview img[alt$="|left"],
.markdown-source-view.mod-cm6.is-live-preview img[alt*="|left|"] {
  display: block;
  margin-left: 0 !important;
  margin-right: auto !important;
}

.markdown-rendered .image-embed:has(img[alt$="|left"]),
.markdown-rendered .image-embed:has(img[alt*="|left|"]),
.markdown-preview-view .image-embed:has(img[alt$="|left"]),
.markdown-preview-view .image-embed:has(img[alt*="|left|"]),
.markdown-source-view.mod-cm6.is-live-preview .image-embed:has(img[alt$="|left"]),
.markdown-source-view.mod-cm6.is-live-preview .image-embed:has(img[alt*="|left|"]) {
  display: table !important;
  margin-left: 0 !important;
  margin-right: auto !important;
}

.markdown-rendered img[alt$="|center"],
.markdown-rendered img[alt*="|center|"],
.markdown-preview-view img[alt$="|center"],
.markdown-preview-view img[alt*="|center|"],
.markdown-source-view.mod-cm6.is-live-preview img[alt$="|center"],
.markdown-source-view.mod-cm6.is-live-preview img[alt*="|center|"] {
  display: block;
  margin-left: auto !important;
  margin-right: auto !important;
}

.markdown-rendered .image-embed:has(img[alt$="|center"]),
.markdown-rendered .image-embed:has(img[alt*="|center|"]),
.markdown-preview-view .image-embed:has(img[alt$="|center"]),
.markdown-preview-view .image-embed:has(img[alt*="|center|"]),
.markdown-source-view.mod-cm6.is-live-preview .image-embed:has(img[alt$="|center"]),
.markdown-source-view.mod-cm6.is-live-preview .image-embed:has(img[alt*="|center|"]) {
  display: table !important;
  margin-left: auto !important;
  margin-right: auto !important;
}

.markdown-rendered img[alt$="|right"],
.markdown-rendered img[alt*="|right|"],
.markdown-preview-view img[alt$="|right"],
.markdown-preview-view img[alt*="|right|"],
.markdown-source-view.mod-cm6.is-live-preview img[alt$="|right"],
.markdown-source-view.mod-cm6.is-live-preview img[alt*="|right|"] {
  display: block;
  margin-left: auto !important;
  margin-right: 0 !important;
}

.markdown-rendered .image-embed:has(img[alt$="|right"]),
.markdown-rendered .image-embed:has(img[alt*="|right|"]),
.markdown-preview-view .image-embed:has(img[alt$="|right"]),
.markdown-preview-view .image-embed:has(img[alt*="|right|"]),
.markdown-source-view.mod-cm6.is-live-preview .image-embed:has(img[alt$="|right"]),
.markdown-source-view.mod-cm6.is-live-preview .image-embed:has(img[alt*="|right|"]) {
  display: table !important;
  margin-left: auto !important;
  margin-right: 0 !important;
}
```

## Live Preview Alignment Refresh Fix

After the CSS alignment syntax was working, a second issue appeared: changing an image from `|left` to `|right` or `|center` did not update immediately in the note. The alignment only refreshed after closing and reopening the note.

This was traced to the installed plugin:

- `.obsidian/plugins/image-tools/main.js`

The plugin was already watching editor changes, but its alignment logic only added an alignment class if the embed did not already have one. That meant stale classes could remain on an image embed after the Markdown flag changed.

### Fix applied

The plugin’s update logic was changed so that on every editor update it:

1. Reads the current alignment from the Markdown image syntax.
2. Removes any existing `images-tools-text-align-*` class from the embed.
3. Applies the correct current alignment class.

This matters because `image-tools` already understands alignment tokens in either order for URL-style image embeds, for example both

```md
![400|center](./images/example.png)
![|center|400](./images/example.png)
```

but without the refresh fix, stale alignment classes could make the behavior appear inconsistent.

### Implementation note for future vault rollout

To reproduce this feature reliably in another vault, do not treat it as “just a CSS snippet.” The reusable implementation checklist is:

1. Copy `codex-image-align-flags.css` into `.obsidian/snippets/`.
2. Enable it in `.obsidian/appearance.json`.
3. If the vault uses `image-tools`, patch `.obsidian/plugins/image-tools/main.js` with the alignment-refresh fix.
4. If the vault uses `image-tools` or any other wrapper-producing image plugin, make sure the CSS targets the wrapper (`.image-embed`), not only the raw `<img>` tag.

If step 3 or 4 is skipped, the feature can appear to work in one vault and fail or behave inconsistently in another.

### Effect

Alignment changes such as

```md
![450|left](./images/example.png)
```

to

```md
![450|right](./images/example.png)
```

should now update immediately in Live Preview after the plugin is reloaded.

### Important implementation note

The current fix was applied directly to the built plugin file:

- `.obsidian/plugins/image-tools/main.js`

For the generator, the better long-term approach is one of the following:

1. Patch the plugin source before bundling, if the source repository is part of the generator.
2. Apply a post-install patch to the built plugin file.
3. Replace this behavior with a small custom vault plugin dedicated to image alignment refresh.

If the generator installs `image-tools`, it should also include this alignment-refresh fix or an equivalent custom watcher.

## Figure Generation Example

One note also received a generated polar-coordinate figure plus the Python source used to make it:

- `Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 01 Complex Numbers and Functions/1.3 Polar Form.md`
- `Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 01 Complex Numbers and Functions/images/review-1-6-polar-figure.png`

This was content-level note editing, not a vault-wide feature, so it probably does not belong in the generator unless you want automatic figure-generation helpers in your template.

## Recommended Generator Changes

For the generator template, the useful vault-wide changes are:

1. Create `.obsidian/snippets/codex-image-align-flags.css`.
2. Ensure `.obsidian/appearance.json` enables the snippet.
3. If the template includes `image-tools`, also include the alignment-refresh fix.
4. Document the supported image syntax for note authors.

## Reload Requirement

After changing plugin code in `.obsidian/plugins/image-tools/main.js`, Obsidian must reload the plugin once. In practice this means either:

- run `Reload app`, or
- disable and re-enable the plugin.

## Generic Callout Removal Command

This vault now includes a small custom plugin that adds a command-palette action for removing the wrapper from the callout at the current cursor position without deleting the callout contents.

The command is generic. It does not depend on the callout being a `figure` callout. It works with any Obsidian callout whose header uses the normal syntax

```md
> [!type] Optional title
> content
```

including custom callout types created by Callout Manager or other plugins.

### Files added

- `.obsidian/plugins/callout-tools/manifest.json`
- `.obsidian/plugins/callout-tools/main.js`
- `.obsidian/community-plugins.json`

The shared vault template under `~/utils/ObsidianConfig/` was also updated with the same plugin files and plugin-list entry so this can be carried into future vault creation.

### Command added

The plugin registers these editor commands:

- `Insert exercise callout`
- `Remove current callout wrapper`
- `Move first callout line to title`
- `Number figure callouts`

The intended workflow is simple: place the cursor anywhere inside a callout and run the desired command from the command palette.

### Exercise callout shortcut

The plugin now also provides a direct insertion command for exercise callouts. The command inserts

```md
> [!exercise]
> 
```

when nothing is selected, and wraps the current selection in an `exercise` callout when text is selected.

The vault hotkeys file binds this command to `Cmd+Shift+2`:

- `.obsidian/hotkeys.json`

This intentionally mirrors the existing built-in generic callout shortcut on `Cmd+Shift+1`, so generic callouts and exercise callouts now have adjacent shortcuts.

### Figure numbering command

The `Number figure callouts` command works on the active Markdown note and rewrites actual figure callout header titles in source order. This is different from the render-only numbering used by the Callout Outline plugin. The goal is to make figure numbering stable in the note text itself so in-text figure references can stay manually consistent.

It only touches real `[!figure]` callout headers and skips fake callout syntax inside fenced code blocks.

The command handles these cases:

- a figure callout with no title becomes `Figure N`
- a figure callout with an unnumbered title such as `Contour around poles` becomes `Figure N: Contour around poles`
- a figure callout already titled `Figure 12` becomes `Figure N`
- a figure callout already titled `Figure 12: Contour around poles` becomes `Figure N: Contour around poles`
- a figure callout titled `Figure 2(a)` becomes `Figure N(a)`
- a figure callout titled `Figure 2a` becomes `Figure N(a)`
- a figure callout titled `Figure 2.a` becomes `Figure N(a)`
- a figure callout titled `Figure 2(a): Contour around poles` becomes `Figure N(a): Contour around poles`
- a figure callout titled `Figure 2a: Contour around poles` or `Figure 2.a: Contour around poles` becomes `Figure N(a): Contour around poles`

Because this command edits the note source directly, the numbering can be undone with normal Obsidian undo if needed.

### What the command does

The plugin scans upward from the cursor to find the nearest enclosing callout header line matching the standard Obsidian form `[!type]`. It then finds the full extent of that callout block by following quoted lines at the same or deeper quote level.

Once found, it unwraps exactly one callout layer:

1. The callout header line is removed.
2. If the callout had a title, the title is preserved as plain text.
3. Each content line has one quote level removed.
4. Nested callouts remain intact, because only one quote layer is stripped.

For example, this

```md
> [!figure] Figure 2
>
> ![](image.png)
> Caption text
```

becomes

```md
Figure 2

![](image.png)
Caption text
```

and a nested callout inside another callout is only unwrapped one level at a time.

## Colored Horizontal Rules Fix

The custom `colored-horizontal-rules` plugin was causing certain notes to fail to open when they contained ordinary Markdown horizontal rules written as

```md
---
```

The bug was that the plugin matched `---` as a custom colored rule, even though normal three-dash rules should remain native Obsidian behavior.

### Files changed

- `complex_analysis/.obsidian/plugins/colored-horizontal-rules/main.js`
- `complex_analysis/.obsidian/plugins/colored-horizontal-rules/styles.css`
- `real_analysis/.obsidian/plugins/colored-horizontal-rules/main.js`
- `real_analysis/.obsidian/plugins/colored-horizontal-rules/styles.css`

### Fix applied

The plugin matcher was narrowed so it now customizes only:

- `+++`
- `----` and longer dash separators

while leaving ordinary `---` untouched.

The rendered CSS was also corrected so plugin-managed horizontal rules are actually drawn with a visible `border-top` instead of being reduced to zero-height hidden elements.

### Effect

This preserves normal Markdown horizontal rules and prevents the plugin from hijacking standard `---` separators in notes. Custom colored separators still work for `+++` and for four-or-more dashes.

### Reload requirement

After editing either plugin copy in `.obsidian/plugins/colored-horizontal-rules/`, Obsidian needs a reload, or the plugin needs to be disabled and re-enabled, before the fix takes effect.

### Title-promotion command

The second command, `Move first callout line to title`, is designed for callouts written like this:

```md
> [!exercise]
> Exercise 1: A complex-valued piecewise continuous function
> Evaluate ...
```

It rewrites them into this form:

```md
> [!exercise] Exercise 1: A complex-valued piecewise continuous function
>
> Evaluate ...
```

The command is intentionally conservative. It only acts when:

1. the current callout header has no title already, and
2. the first non-empty content line is ordinary text.

It refuses to promote the line when the first non-empty content line is structurally sensitive, such as:

- another quoted block,
- a fenced code block marker, or
- a bare `$$` math-fence line.

This is meant to avoid accidentally turning non-title structure into a callout heading.

### Why this was implemented as a plugin

This was intentionally implemented as a small local plugin rather than patching Obsidian core or modifying the Callout Manager plugin. That keeps the feature isolated, easy to port into new vaults, and easy to remove if needed.

The context menu shown when clicking a rendered callout appears to come from Obsidian’s existing callout UI, not from a simple user-editable config file. Adding a command-palette action was therefore the lowest-risk path.

### How to port this into `ocreate`

To make new vaults include this feature automatically, the generator should ensure that the shared config directory contains:

- `ObsidianConfig/plugins/callout-tools/manifest.json`
- `ObsidianConfig/plugins/callout-tools/main.js`

and that `callout-tools` is present in:

- `ObsidianConfig/community-plugins.json`

Because `ocreate` already copies the shared `.obsidian` config into each new vault, this is enough to propagate the feature to newly created vaults.

### Current rollout decision

Even though the shared config directory was updated during implementation, the current intent is to treat this as a vault-local experiment first. The `complex_analysis` vault is the testbed. Only after extended use confirms there are no bugs or undesirable side effects should this be promoted as a default feature for all new vaults created by `ocreate`.

### Reload requirement

After adding or changing `.obsidian/plugins/callout-tools/main.js`, Obsidian must reload before the command appears. In practice:

- run `Reload app`, or
- disable and re-enable the plugin.

## Callout Outline Sidebar

This vault now also includes a second small custom plugin that adds a dedicated sidebar outline for callouts in the active note.

Unlike the built-in outline, this view is not based on headings. It parses Markdown callout headers directly and builds a navigable list of callouts such as `review`, `definition`, `exercise`, `figure`, `theorem`, or any custom callout type created by Callout Manager.

### Files added

- `.obsidian/plugins/callout-outline/manifest.json`
- `.obsidian/plugins/callout-outline/main.js`
- `.obsidian/plugins/callout-outline/styles.css`
- `.obsidian/community-plugins.json`

### Command added

The plugin registers this command:

- `Open callout outline`

Running the command opens a sidebar view named `Callout Outline` in the right sidebar.

### What the plugin does

For the currently active Markdown file, the plugin scans for lines of the form:

```md
> [!type] Optional title
```

and creates an outline entry for each callout it finds.

The entries are generated by callout type and numbered independently per type. For example, if a note contains nine `definition` callouts, the outline will show `Definition 1` through `Definition 9` even if the note itself does not number them consistently.

If a callout already includes a title, the outline keeps that title but avoids duplicating prefixes such as `Review 3` or `Figure 2`. So a header like

```md
> [!exercise] Exercise 1: A complex-valued piecewise continuous function
```

appears in the sidebar as

```text
Exercise 1: A complex-valued piecewise continuous function
```

rather than repeating the number twice.

The parser is intentionally generic:

- it accepts any callout type name that appears in `[!type]`,
- it handles nested callouts,
- it ignores fake callout syntax inside fenced code blocks, and
- it does not require manual registration when a new custom callout type is introduced.

### Filtering

The view includes a type filter dropdown. This allows the outline to be limited to one callout type at a time, such as showing only `definition` callouts or only `figure` callouts in the current note.

### Navigation behavior

Clicking an outline item jumps to the callout using Obsidian’s ephemeral line navigation rather than forcing the editor cursor into the callout body. The goal is to move the document to the correct location while avoiding the usual annoyance where Live Preview de-renders the callout because the cursor enters it.

### Color behavior

The plugin reuses colors from Callout Manager when possible by reading:

- `.obsidian/plugins/callout-manager/data.json`

It looks up the currently configured callout colors there and applies them to the sidebar items for matching callout types.

If a callout type has no Callout Manager color, the plugin generates a stable fallback accent color automatically so that new or ad hoc callout types still remain visually distinguishable.

The plugin also exposes a settings tab with a color picker for each known callout type. These overrides are optional. If no override is set, the plugin falls back to Callout Manager colors first and automatic colors second.

### Reference used during implementation

To study how a custom Obsidian sidebar view is wired, the readable source of Quiet Outline was cloned to:

- `~/Downloads/obsidian-quiet-outline-reference`

That repository was used as a reference for view registration and note-jump behavior. The callout parsing logic itself is custom to this vault plugin.

### Current rollout decision

This should remain a vault-local experiment for now. If it behaves well over time, it could later be copied into the shared `ObsidianConfig` template so that `ocreate` can install it automatically into new vaults.

### Reload requirement

After adding or changing `.obsidian/plugins/callout-outline/main.js`, Obsidian must reload before the new sidebar command appears. In practice:

- run `Reload app`, or
- disable and re-enable the plugin.

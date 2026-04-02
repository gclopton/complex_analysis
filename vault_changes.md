# Vault Changes

This note records the Obsidian-vault changes made during this session so they can be ported into the vault generator.

## Image Alignment Flags

The vault now supports Markdown image alignment flags of the form

```md
![450|left](./images/example.png)
![450|center](./images/example.png)
![450|right](./images/example.png)

![|left](./images/example.png)
![|center](./images/example.png)
![|right](./images/example.png)
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

A CSS snippet was added to target image alt text ending in `|left`, `|center`, or `|right`. The snippet intentionally does not affect plain images.

The enabled snippet list in `.obsidian/appearance.json` was also updated to include:

```json
"codex-image-align-flags"
```

### Snippet contents

```css
/*
Supports Markdown image flags such as:

![450|left](...)
![450|center](...)
![450|right](...)
![|left](...)

Plain images like ![](...) or ![450](...) keep the theme default.
*/

.markdown-rendered img[alt$="|left"],
.markdown-preview-view img[alt$="|left"],
.markdown-source-view.mod-cm6.is-live-preview img[alt$="|left"] {
  display: block;
  margin-left: 0 !important;
  margin-right: auto !important;
}

.markdown-rendered img[alt$="|center"],
.markdown-preview-view img[alt$="|center"],
.markdown-source-view.mod-cm6.is-live-preview img[alt$="|center"] {
  display: block;
  margin-left: auto !important;
  margin-right: auto !important;
}

.markdown-rendered img[alt$="|right"],
.markdown-preview-view img[alt$="|right"],
.markdown-source-view.mod-cm6.is-live-preview img[alt$="|right"] {
  display: block;
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

- `Remove current callout wrapper`
- `Move first callout line to title`

The intended workflow is simple: place the cursor anywhere inside a callout and run the desired command from the command palette.

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

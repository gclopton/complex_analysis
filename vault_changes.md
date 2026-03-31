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

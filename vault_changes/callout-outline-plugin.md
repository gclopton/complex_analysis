# Callout Outline Plugin

This note documents how the `Callout Outline` plugin was created for the `complex_analysis` vault, what it depends on, and where its code can be found.

## Purpose

The plugin adds a dedicated Obsidian sidebar view for callouts in the active Markdown note.

The main goals were:

1. show an outline of all callouts in the current file,
2. number callouts independently by type, even when the note does not number them consistently,
3. support arbitrary custom callout types without manual registration,
4. filter the outline by callout type,
5. reuse Callout Manager colors when possible, and
6. jump to the selected callout without forcing the editor cursor into the callout body.

## Plugin Files

The vault-local plugin code lives here:

- `.obsidian/plugins/callout-outline/manifest.json`
- `.obsidian/plugins/callout-outline/main.js`
- `.obsidian/plugins/callout-outline/styles.css`

The plugin was enabled in:

- `.obsidian/community-plugins.json`

These are the only files required for the plugin itself inside this vault.

## Reference Material Used

Two existing pieces of local context were used while building the plugin.

### Quiet Outline reference

The readable source for Quiet Outline was cloned to:

- `/Users/gradyclopton/Downloads/obsidian-quiet-outline-reference`

This was used as a reference for:

- registering a custom Obsidian sidebar view,
- following the active note,
- and jumping to a location in the current note with ephemeral navigation behavior.

The bundled plugin copy inside the vault was also inspected, but the GitHub source clone was much more useful than the packaged `main.js`.

### Callout Manager settings

The plugin reads callout color information from:

- `.obsidian/plugins/callout-manager/data.json`

That file contains the custom callout types and color settings already configured in this vault. The new outline plugin uses those colors by default so the sidebar stays visually consistent with existing callout styling.

## Implementation Approach

This plugin was implemented as a plain local Obsidian plugin in JavaScript inside `.obsidian/plugins/` rather than as a bundled TypeScript project. That choice kept the vault-local experiment simple to inspect and simple to remove.

The plugin does not patch Obsidian core and does not modify Quiet Outline or Callout Manager. It operates independently.

### Parsing strategy

Obsidian does not provide a built-in callout outline API similar to heading metadata, so the plugin parses callouts directly from Markdown source.

It scans for callout headers of the form:

```md
> [!type] Optional title
```

The parser is intentionally generic and conservative:

- any `[!type]` is accepted,
- callout types are normalized case-insensitively,
- nested callouts are tracked,
- fenced code blocks inside quoted content are ignored,
- fake callout syntax inside code fences is ignored,
- and numbering is generated independently per normalized callout type.

### Sidebar behavior

The plugin registers a right-sidebar view named `Callout Outline`.

Each item in the outline shows:

- the generated type-based label such as `Review 3` or `Exercise 4: ...`,
- the source line number,
- and, when the handwritten title numbering conflicts with the generated numbering, the raw title line underneath so the mismatch is easy to spot.

For example, if the note title says `Review 4` but the generated position is `Review 3`, the sidebar shows `Review 3` as the primary label and the raw title text separately underneath.

### Filtering

The view includes a dropdown that filters the list to a single callout type, such as only `definition` or only `figure`.

### Color handling

Color selection follows this order:

1. plugin-specific override from the Callout Outline settings tab,
2. Callout Manager color for that callout type,
3. stable generated fallback color when no configured color exists.

This allows new or ad hoc callout types to appear immediately even if they were never manually configured ahead of time.

### Navigation

Clicking an outline item jumps to the callout line using Obsidian’s ephemeral navigation state.

This was chosen deliberately so the editor scrolls to the correct location without depending on heading links and without aggressively forcing the cursor into the body of the callout.

## Commands and Settings

The plugin currently provides:

- command: `Open callout outline`
- ribbon button: a custom Callout Outline icon in the Obsidian ribbon that opens the view directly
- settings tab: `Callout Outline`

The settings tab includes:

- a toggle for inheriting Callout Manager colors,
- a toggle for decorating rendered callout titles with generated numbering,
- a reload action for re-reading callout colors,
- and per-type color pickers for optional overrides.

The sidebar view itself also uses the same custom icon rather than the generic list icon, so the view tab is easier to recognize visually.

## Important Design Decisions

### Vault-local first

This plugin is currently a vault-local experiment only. It has not been promoted into the shared `ObsidianConfig` template.

That was intentional. The plugin should be used in this vault long enough to catch parser issues, navigation issues, and display issues before it is copied into the template for `ocreate` or rolled out to other vaults.

### Generated numbering is authoritative

The outline numbers callouts by their actual position within the current note, grouped by type. This means the generated numbering remains correct even when a callout title was manually numbered incorrectly.

At the same time, the raw title is preserved when there is a conflict so mismatches can be seen and corrected manually.

The same numbering logic is also used for optional in-note rendered callout-title decoration. When that setting is enabled, the displayed callout title in the note uses the generated numbering at render time, but the Markdown source is not rewritten.

That feature is currently treated as experimental, because Obsidian may only render part of a long note at once. The current approach therefore tries to map rendered callout widgets back to source lines through CodeMirror rather than matching visible callouts by DOM order. That is much safer than the original DOM-order experiment, but it still needs real vault use before it should be considered fully reliable.

### Manual numbering overrides

The plugin also supports two callout-local override directives for rare numbering edge cases. These are written as hidden Obsidian comments on the first non-empty content line inside the callout.

#### Manual override

Use this when a callout should keep its handwritten title and should not be auto-numbered by the plugin:

```md
> [!figure] Figure 2(a)
> %% callout-outline: manual %%
> ...
```

When this override is present:

- the outline shows the handwritten title as-is,
- the plugin does not auto-number that callout,
- and in-note rendered-title decoration leaves that callout alone.

#### Numbering restart

Use this when automatic numbering needs to resume at a specific number:

```md
> [!figure]
> %% callout-outline: start=3 %%
> ...
```

When this override is present, that callout becomes `Figure 3`, and later callouts of the same type continue counting from there.

This is meant for cases such as:

- separate `Figure 2(a)` and `Figure 2(b)` callouts handled manually, followed by a normal `Figure 3`,
- or rare out-of-order figure placements where handwritten numbering temporarily breaks the automatic sequence.

### Math rendering

Inline LaTeX in callout titles is rendered in the outline using Obsidian’s math rendering hooks when possible, rather than displaying raw `$...$` text.

## Verification Performed During Build

During implementation, the plugin was checked in several ways:

1. `node -c` was used to syntax-check `.obsidian/plugins/callout-outline/main.js`.
2. JSON files were validated after editing.
3. The parser was exercised against a real chapter note:
   - `Books/Asmar Applied Complex Analysis with Applications to Differential Equations/Chapter 03 Complex Integration/3.2 Complex Integration.md`
4. Callout Manager color inheritance was checked against the current vault settings.
5. Nested callout parsing and code-fence skipping were tested with sample inputs.

## Promotion Path Later

If the plugin proves stable, the later rollout path is straightforward:

1. copy the plugin folder into the shared `ObsidianConfig/plugins/` template area,
2. add the plugin id to the shared `community-plugins.json`,
3. document any vault-level prerequisites,
4. and then decide whether to back-port it into existing vaults.

Until then, this note and the plugin source files above are the authoritative reference for how the feature was implemented in `complex_analysis`.

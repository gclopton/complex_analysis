# Case Sensitive Find Plugin

This note documents the vault-local `Case Sensitive Find` plugin added to the `complex_analysis` vault.

## Purpose

Obsidian’s normal in-note `Ctrl+F` find bar does not expose a straightforward match-case toggle. This plugin replaces the Markdown-editor `Ctrl+F` behavior inside this vault with a local find bar that supports case-sensitive searching.

The goal was not to patch Obsidian core. The plugin stays vault-local, but it now hooks the actual in-editor Obsidian command `editor:open-search` so that `Ctrl+F` in a Markdown editor opens the custom find bar instead of the native in-file search bar.

## Plugin Files

The plugin code lives here:

- `.obsidian/plugins/case-sensitive-find/manifest.json`
- `.obsidian/plugins/case-sensitive-find/main.js`
- `.obsidian/plugins/case-sensitive-find/styles.css`

It was enabled in:

- `.obsidian/community-plugins.json`

## What It Does

When the active pane is a Markdown editor, pressing `Ctrl+F` or `Cmd+F` opens a custom find bar instead of the native in-note search bar.

The custom bar provides:

- a search input,
- a match counter,
- next and previous navigation,
- a case-sensitive toggle labeled `Aa`,
- and a close button.

If text is selected before opening the bar, that text is used as the initial query when it is a single line.

Typing in the search box updates the match count without immediately moving the editor cursor. The editor jump happens when you press `Enter` or use the next and previous buttons.

## Search Behavior

The search runs on the actual Markdown source in the active editor.

When match case is off, the plugin searches case-insensitively.

When match case is on, the plugin searches with exact case matching.

The current match is moved into the editor selection, and the editor is scrolled to that match.

While the custom find bar is open, the plugin temporarily sets Obsidian’s own `--text-selection` variable to `var(--text-highlight-bg)` on the active Markdown editor scope. That turned out to be more reliable than trying to guess the exact CodeMirror DOM node that needed a direct color override. A light inset border is still applied through CSS so the active match remains easy to spot.

One implementation detail mattered here: the plugin applies the active search state to several editor-related roots, including the Markdown source view and the underlying CodeMirror editor node, because Obsidian’s editor DOM nesting is not the same in every context. The earlier selector-only approach was too brittle.

## Why This Was Implemented As A Replacement

The native Obsidian find bar is part of Obsidian’s bundled app code and is not a stable plugin API surface.

The first attempt tried to intercept the hotkey directly, but the actual editor pane search is controlled by Obsidian’s internal `editor:open-search` command. The current implementation therefore patches that specific command in this vault so that the command opens the custom bar. That is still easier to reason about and easier to roll back than modifying Obsidian core files.

## Current Scope

This is currently intended for Markdown editing in this vault.

It is not designed as a global Obsidian search replacement, and it does not attempt to modify PDF search, graph search, or other unrelated search UIs.

## Verification Performed

During implementation, the plugin was checked by:

1. syntax-checking the plugin JavaScript with `node -c`,
2. validating the manifest and community plugin JSON,
3. and verifying the vault-local plugin registration path.

## Promotion Path Later

If this works well in real use, it can later be:

1. copied into the shared `ObsidianConfig` template,
2. enabled in other vaults,
3. or refined further to add features such as regex search or a native-find fallback command.

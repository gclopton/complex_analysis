# Vault Changes Folder

This folder is the new home for vault-level change documentation.

The older note

- `vault_changes.md`

still exists at the vault root and contains earlier session notes. Going forward, larger changes should be documented as separate notes here so the change history stays readable.

## Current Notes

- `callout-outline-plugin.md` — how the Callout Outline plugin was designed and where its code lives
- `case-sensitive-find-plugin.md` — how the vault-local Ctrl+F replacement with match-case support was implemented
- `colored-horizontal-rules-plugin.md` — how plugin-owned `+++` / `++++` colored separators were implemented and stabilized for editor use

## Intended Use

This folder is meant to support two later workflows:

1. deciding which vault-local changes are stable enough to promote into the shared vault template, and
2. applying proven changes to other existing vaults without having to reverse-engineer them again.

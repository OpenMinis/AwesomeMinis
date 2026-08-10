# AwesomeMinis Cases — English, Current-Skills Edition

This package contains English-only editions of all Markdown cases from:

https://github.com/OpenMinis/AwesomeMinis/tree/main/cases

## Structure

- `creative/`
- `developer/`
- `finance/`
- `health/`
- `productivity/`
- `research/`
- The English files reuse the repository's root `assets/` directory, so their existing `../../assets/...` screenshot links continue to work.

## Current skills review

The cases were reviewed on 2026-07-27 against:

- Repository: `https://github.com/OpenMinis/MinisSkills`
- Commit: `3993f5ab0a0ff204d774da7a5cf27ea281e7b021`

Updates include current public skill names, current environment-variable names, current authentication workflows, and explicit labeling for custom or external components that are not in the public MinisSkills repository.

Notable corrections:

- `nano-banana-2` → `nano-banana`, using the Nano Banana 2 model
- Spotify variables updated to `SPOTIPY_*`
- Doubao TTS updated to prefer `DOUBAO_TTS_API_KEY`
- qBittorrent workflow updated to `qbt-hub` and `QBT_*`
- Current browser-cookie flows documented for Bilibili, X, and YouTube Music
- Telegram first-login and local-sync workflow documented
- Missing public skills labeled as custom instead of installable public dependencies
- External WeRead, OpenILink, Dida/TickTick, and edge-tts components labeled explicitly

## Validation

- 47 Markdown case files present
- Original category structure preserved
- Existing root screenshot assets are reused; no image files are duplicated
- Every local Markdown image link resolves
- No Chinese/CJK text remains in the Markdown files, except for contributor names kept in their original language
- Public skill references validated against the MinisSkills commit above

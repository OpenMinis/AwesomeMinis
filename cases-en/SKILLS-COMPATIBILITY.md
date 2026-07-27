# MinisSkills Compatibility Notes

Reviewed: 2026-07-27
Repository: `https://github.com/OpenMinis/MinisSkills`
Commit: `3993f5ab0a0ff204d774da7a5cf27ea281e7b021`

## Public skills validated

- `bilibili-hub`
- `codex-image`
- `doubao-tts`
- `exa-search`
- `nano-banana`
- `qbt-hub`
- `spotify-hub`
- `tg-hub`
- `twitter-x-hub`
- `ytmusic-hub`

## Corrections applied

- Updated Spotify configuration to `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI`, including OAuth and active-device requirements.
- Updated Doubao TTS to prefer `DOUBAO_TTS_API_KEY`; legacy AppID + Token is documented as a fallback.
- Replaced the obsolete skill reference `nano-banana-2` with `nano-banana` and documented its Nano Banana 2 default model.
- Added `qbt-hub` and the exact `QBT_HOST`, `QBT_USER`, and `QBT_PASS` variables to the qBittorrent case.
- Updated YouTube Music authentication to the current browser-cookie and `ytmusic_headers.json` workflow.
- Added current Bilibili cookie authentication requirements.
- Added the current Telegram interactive login, `TG_API_ID` / `TG_API_HASH`, and local SQLite synchronization workflow.
- Updated `codex-image` authentication to the automatic ChatGPT browser-session flow.
- Updated X authentication to `TWITTER_AUTH_TOKEN` + `TWITTER_CT0` loaded from browser cookies.
- Corrected the `edge-tts` case: it does not require an API key, but it normally uses an online Microsoft service and is not fully offline.
- Added iOS Shortcuts guidance for scheduled work instead of unreliable background shell loops.

## Custom or external components

The following are not currently in the public MinisSkills repository and are labeled accordingly in their cases:

- `personal-color-analysis`
- `ppt-generator`
- `cardiac-health-monitor`
- `project-case-builder`
- `video-script-writer`
- `project-reviewer`
- `weread-skills`
- `openilink-hub`
- Custom Dida / TickTick integration
- `edge-tts` Python package

Where possible, the cases now explain how to complete the workflow with built-in Minis capabilities instead of claiming a missing public skill is required.

# Changelog

All notable changes to Limina are documented here.

## v0.7.1

### Fixed
- **Pause/resume produced no sound.** Pausing used to suspend the entire `AudioContext`; resuming rebuilt the audio graph immediately afterward without waiting for the context to actually leave its suspended state — on many browsers (especially mobile), audio nodes started against a still-suspended context stay silent. Pause now just fades out and stops the current audio graph while leaving the `AudioContext` running; resume rebuilds the graph the same way switching between programs already did (a path that was already proven reliable).

## v0.7

### Fixed
- Service worker now uses network-first for HTML page loads instead of cache-first — visitors reliably get the latest deployed version instead of a stale cached one. Cache version bumped to force cleanup of previously cached (potentially stale) files.

### Changed
- Reverb impulse response is now generated once per program and cached in memory, instead of being recomputed on every session start, pause/resume, and program switch — reduces unnecessary CPU work, especially noticeable on lower-end mobile devices
- `getAudioContext()` now fails gracefully (returns `null`) instead of throwing if Web Audio API isn't available; `startSession()` checks for this and shows a toast instead of silently breaking

### Added
- `tools/generate_favicon.py` and `tools/generate_silent_wav.py` — the scripts used to generate the embedded favicon and silent audio anchor, committed to the repo for reproducibility

## v0.6

### Added
- Toast notification on natural session completion ("Session complete — sleep well"), distinct from the manual-stop message
- Double-tap confirmation before stopping long (1h+) or infinite sessions — prevents accidental loss of an 8-hour Sleep mode session from a stray tap
- "Remember last session" — on return visits, the last-used program and duration are pre-selected (card highlighted, Now Playing panel populated) without auto-playing; one tap resumes
- System theme detection (`prefers-color-scheme`) on first visit, instead of always defaulting to dark
- Visual fade-in on the waveform icon synced to the 4-second audio fade-in, giving clear feedback that a session is starting
- iOS "Add to Home Screen" hint — a one-time dismissible banner shown only to iOS Safari visitors not already running in standalone/PWA mode

### Fixed
- Duration pill selection now correctly reflects the actual selected duration after a language switch (previously always reset to the first pill regardless of what was selected)

## v0.5

### Added
- Media Session API integration — lock-screen and notification playback controls (play/pause/stop) with program name, "Limina", and "Sentria" as metadata
- Silent audio anchor (inline base64 WAV, no external file) that plays alongside the Web Audio API graph to keep the media session alive when the screen locks or the app is backgrounded
- Defensive `AudioContext` resume on `visibilitychange`, in case the context gets suspended despite the anchor

### Fixed
- Clicking an already-active program card now only toggles its detail view (purpose, textures, tone) instead of restarting the running session

## v0.4

### Fixed
- Pause/resume no longer causes the progress bar to jump forward by the paused duration — playback position is now tracked correctly across pause/resume cycles
- Binaural frequency drift (e.g. 8→6 Hz) now resumes from the correct interpolated point instead of restarting from the beginning after a pause
- Headphone check completed via the header icon (rather than the onboarding banner) now correctly dismisses the banner and removes the highlight
- Rapid switching between programs no longer risks a duplicate/stale session start firing after a newer selection

## v0.3

### Added
- Sticky mini player — appears when scrolling past the main player, with waveform, title, progress, and play/stop controls
- Headphone check — onboarding banner + 3-step stereo test (left / right / both) explaining why headphones are needed for binaural audio
- Version number in footer

### Changed
- Renamed module from PulseLab to **Limina**, kept under the Sentria ecosystem branding
- Intro and footer copy updated to reference Limina directly

## v0.2

### Added
- Full audio engine rewrite: layered ambient drones with amplitude + filter LFOs, stereo panning per layer, synthetic convolution reverb, 12-second stereo noise buffers (up from 4s mono)
- PWA support: inline SVG favicon/icons (16, 32, 180, 192, 512), web manifest embedded as base64 data URI, service worker for offline caching
- `vercel.json` for routing and cache headers

### Fixed
- `AudioContext` autoplay-policy bug causing audio to cut out after 2–3 seconds on first load
- Service worker registration syntax error

## v0.1

### Added
- Initial release: 7 auditory programs (Deep Relaxation, Hypnagogic Drift, Lucid Preparation, Recall Support, Gentle Awakening, Reflective Focus, Dream Descent)
- Bilingual EN/SL interface, fully translatable via a single data object
- Light/dark theme
- Basic binaural beat + drone + filtered noise audio engine
- Player controls: play/pause, restart, stop, seek, volume
- Breathing guide for relevant programs

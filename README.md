# Limina

*Auditory environments for sleep, hypnagogic transition, and reflective awareness — part of the Sentria ecosystem.*

Limina is a minimalist, single-file web app that generates layered ambient soundscapes — binaural beats, filtered noise, evolving drones, and synthetic reverb — entirely in the browser using the Web Audio API. No audio files, no backend, no external dependencies beyond fonts.

🔗 **Live app:** _(add your Vercel URL here)_

---

## What it does

Limina offers seven auditory programs, each tuned for a different state of mind around sleep and dreaming:

| Program | Purpose |
|---|---|
| **Deep Relaxation** | Prepare body and mind for sleep — warm, grounding, unhurried |
| **Hypnagogic Drift** | Support the transition between wakefulness and dream onset |
| **Lucid Preparation** | Enter sleep with clear, open awareness — a foundation for lucid dreaming practice |
| **Recall Support** | A soft morning environment for holding dream memories as they surface |
| **Gentle Awakening** | A slow, calm emergence from sleep — not an alarm, an invitation |
| **Reflective Focus** | A restrained environment for journaling and dream analysis |
| **Dream Descent** | The quietest environment in Limina — deep, slow sleep initiation |

Each program uses its own internal frequency profile (binaural beat range, drone layering, noise color, reverb character) — presented to the user through experiential names, never raw Hz values or technical controls.

## Design philosophy

- Calm, ritualistic, atmospheric — not a neuroscience dashboard
- No "unlock hidden powers" language, no frequency mysticism
- No exposed sliders for Hz, gain, or modulation by default
- Psychologically safe: no guaranteed outcomes, no medical claims

## Features

- **Fully generative audio** — every session is synthesized live via Web Audio API (oscillators, filtered noise buffers, synthetic convolution reverb). Nothing is pre-recorded.
- **Bilingual** — English and Slovene, fully translatable via a single data object (no hardcoded strings)
- **Light / dark theme** — persisted across sessions, defaults to system preference (`prefers-color-scheme`) on first visit
- **Sticky mini player** — stays accessible while scrolling
- **Headphone check** — a short stereo test (left / right / both) since binaural beats require headphones to work; onboarding banner explains why
- **Background playback** — Media Session API integration gives lock-screen and notification controls (play/pause/stop); a silent audio anchor keeps the session alive when the screen locks or the app is backgrounded
- **Remembers your last session** — pre-selects your last-used program and duration on return visits (no auto-play — one tap resumes)
- **PWA-ready** — installable, works offline after first load, custom favicon/icons embedded as inline SVG (no external image assets), one-time "Add to Home Screen" hint for iOS visitors
- **Accessible** — keyboard-operable program cards, `aria-label`s on all icon-only controls, translated screen-reader labels

## Tech stack

- Vanilla HTML / CSS / JavaScript — no framework, no build step
- Web Audio API — `AudioContext`, `OscillatorNode`, `GainNode`, `BiquadFilterNode`, `StereoPannerNode`, `ConvolverNode`, `AudioBufferSourceNode`
- Media Session API — lock-screen / notification playback controls
- `localStorage` for theme, language, headphone-check state, and last session
- Google Fonts (Cormorant Garamond, DM Sans)
- Service worker for offline caching (cache-first, network-first fallback for fonts)

## Project structure

```
limina.html      → the entire app (single file)
sw.js            → service worker for offline support
vercel.json      → routing, cache headers, security headers
```

## Deployment

Deployed on Vercel. To redeploy after changes:

```bash
vercel --prod
```

Make sure `limina.html`, `sw.js`, and `vercel.json` are all present in the deploy directory — the service worker must be served from the same origin as the app.

### Ignoring local-only files

If you keep extra notes, drafts, or sketches in the project folder that shouldn't be deployed, add a `.vercelignore`:

```
*
!limina.html
!sw.js
!vercel.json
```

## Browser support

Requires a modern browser with Web Audio API support (`AudioContext`, `StereoPannerNode`, `ConvolverNode`) — all current versions of Chrome, Edge, Firefox, and Safari. Binaural beats require stereo headphones or earbuds to be effective; the app includes a built-in headphone check to confirm this before starting a session.

Background playback (screen locked / app backgrounded) is supported via the Media Session API and a silent audio anchor, but iOS Safari in particular can still suspend audio more aggressively than desktop browsers or Android — this is a platform limitation, not something fully controllable from a web app without a native wrapper.

## Not a medical device

Limina is designed for reflective and sleep-support use only. It makes no clinical or therapeutic claims and is not a substitute for medical advice.

## Part of Sentria

Limina is one module within **Sentria**, a broader reflective consciousness and dream exploration ecosystem, alongside dream journaling, symbolic dream mapping, and lucid dreaming practice tools.

---

*Version 0.6 — active development*

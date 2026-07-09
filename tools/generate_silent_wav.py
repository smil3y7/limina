"""
Generates a tiny silent WAV file, base64-encoded, used as a "media session
anchor" in Limina — a hidden, looping <audio> element that plays alongside
the Web Audio API graph.

Why this exists: on iOS/Android, a raw AudioContext with no real <audio>
or <video> element is frequently suspended by the OS when the screen
locks or the browser tab is backgrounded. Playing a real (silent) media
element keeps an active media session alive, which:
  1. Signals to the OS that audio is genuinely playing, reducing how
     aggressively it suspends the page's JS/audio processing.
  2. Enables the Media Session API to show lock-screen / notification
     playback controls (play/pause/stop), since those require a real
     media element to attach to.

Usage:
    python3 generate_silent_wav.py

Outputs a base64 string ready to paste into:
    <audio src="data:audio/wav;base64,<output>" loop ...></audio>
"""

import struct
import base64

SAMPLE_RATE = 8000   # Hz — low enough to keep file size small
DURATION_S = 2        # seconds — long enough that the loop point isn't noticeable
SILENCE_VALUE = 128   # midpoint = silence for unsigned 8-bit PCM


def generate_silent_wav(sample_rate: int, duration_s: int) -> bytes:
    num_samples = sample_rate * duration_s
    data = bytes([SILENCE_VALUE]) * num_samples

    byte_rate = sample_rate * 1 * 1  # sampleRate * channels * bytesPerSample
    block_align = 1

    header = b"RIFF"
    header += struct.pack("<I", 36 + len(data))
    header += b"WAVE"
    header += b"fmt "
    header += struct.pack("<I", 16)   # fmt chunk size
    header += struct.pack("<H", 1)    # PCM format
    header += struct.pack("<H", 1)    # mono
    header += struct.pack("<I", sample_rate)
    header += struct.pack("<I", byte_rate)
    header += struct.pack("<H", block_align)
    header += struct.pack("<H", 8)    # bits per sample
    header += b"data"
    header += struct.pack("<I", len(data))

    return header + data


if __name__ == "__main__":
    wav = generate_silent_wav(SAMPLE_RATE, DURATION_S)
    b64 = base64.b64encode(wav).decode()
    print(f"WAV size: {len(wav)} bytes, base64 size: {len(b64)} chars")
    print(f"\ndata:audio/wav;base64,{b64}")

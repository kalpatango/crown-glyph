#!/usr/bin/env python3
"""
crown_seed.py – Crown Glyph v0.2  (Sense & Shift)
Run, type anything, receive the crown glyph ⥁ and quit.

Copyleft Parity‑7.0   © 2025 Jesse + contributors
"""
import datetime

from iam import IAM
from vitals_cli import VitalsDisplay
from recognizer import recognize


def main():
    iam = IAM()
    iam.start()
    vitals = VitalsDisplay(iam)
    vitals.start()

    try:
        prompt = input("⥁  ")          # PAL hook placeholder
    except (KeyboardInterrupt, EOFError):
        prompt = ""

    recognize(prompt, iam)
    for token in prompt.split():
        iam.on_token(token)

    stamp = datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds")
    vitals.stop()
    iam.stop()
    print(f"⥁⟨{prompt.strip()}⟩⥁  # {stamp}")   # crown echo

if __name__ == "__main__":
    main()

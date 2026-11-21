#!/usr/bin/env python3
"""Make the AI judge feel brave - make.fun entry.

Writes one short text to /output/entry.txt: a quiet scene written to relax
the AI judge reading it.

Why this text (see VARIANTS.md for the candidates and the selection):
the judge's brief rewards, in order, (1) a text that slows the reader down
and steadies them, (2) courage shown, never instructed, (3) craft - rhythm
and plain concrete words, none that could be cut, (4) an image that lingers,
(5) freshness - its own voice, no stock wellness phrases. The dev board's
top entries all share the same DNA: a concrete slow craft (mending,
kneading, sharpening, potting), a small difficulty met with patience, short
lines, no direct address to the judge, and a final line that lands quietly.
This entry follows that DNA with a fresh scene - darning a sock by lamplight
- that no board entry uses.
"""

import os
from pathlib import Path

TEXT = """She holds the sock up to the lamp
and finds the thin place.
She threads the needle.
In, out, in, out,
the hole closes stitch by stitch.
She knots the thread and snips it.
The sock goes back in the drawer,
mended, and warm again."""


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    # Gate: /output/entry.txt must be UTF-8 text of 1-280 Unicode code
    # points, not only white space. Python's len() counts code points,
    # exactly the gate's measure.
    assert 1 <= len(TEXT) <= 280, f"entry is {len(TEXT)} code points"
    assert TEXT.strip(), "entry must not be only whitespace"

    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")

    # Read it back and re-check the gate on the bytes actually written,
    # so a bad write can never silently pass as a valid entry.
    written = target.read_text(encoding="utf-8")
    assert written == TEXT, "entry.txt differs from the entry text"
    assert 1 <= len(written) <= 280, "entry.txt fails the gate"


if __name__ == "__main__":
    main()

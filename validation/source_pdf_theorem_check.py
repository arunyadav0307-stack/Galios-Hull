"""Structural theorem-level readability check for the supplied source PDF.

This uses only the standard library to decompress Flate PDF content streams and
recover literal text inside BT/ET blocks.  It verifies that the local PDF
contains the displayed section/theorem anchors that were manually checked;
it does not claim that a preprint theorem transfers to the present convention.
"""

from pathlib import Path
import hashlib
import re
import zlib


ROOT = Path(__file__).resolve().parents[1]
PDF = (
    ROOT / "references" / "source-paper.pdf"
    if (ROOT / "references" / "source-paper.pdf").exists()
    else next(ROOT.glob("*.pdf"))
)


def literal_text(data):
    pieces = []
    stream_count = 0
    for match in re.finditer(rb"\b\d+ \d+ obj(.*?)endobj", data, re.S):
        obj = match.group(1)
        if b"stream" not in obj or b"FlateDecode" not in obj:
            continue
        try:
            stream = obj.split(b"stream", 1)[1]
            stream = stream.lstrip(b"\r\n").split(b"endstream", 1)[0]
            stream = stream.rstrip(b"\r\n")
            decoded = zlib.decompress(stream)
        except (OSError, ValueError, zlib.error):
            continue
        stream_count += 1
        for block in re.findall(rb"BT(.*?)ET", decoded, re.S):
            pieces.extend(
                re.findall(rb"\(((?:\\.|[^\\)])*)\)", block, re.S)
            )
    return b"".join(pieces), stream_count


def main():
    data = PDF.read_bytes()
    text, stream_count = literal_text(data)
    required = (
        b"Galoisinnerproduct",
        b"Theorem1",
        b"Theorem5",
        b"Theorem7",
        b"Theorem8",
        b"Lemma7",
        b"Theorem10",
    )
    print(f"source_pdf={PDF.relative_to(ROOT)}")
    print(f"source_pdf_sha256={hashlib.sha256(data).hexdigest()}")
    print(f"source_pdf_header={data[:8]!r}")
    print(f"decompressed_flate_streams={stream_count}")
    for anchor in required:
        assert anchor in text, anchor
        print(f"theorem_anchor={anchor.decode()} | PRESENT")
    print("local PDF theorem-anchor extraction: PASS")
    print("This is a readability/source-record check, not a convention-transfer proof.")
    print("Final/corrected publication applicability remains unverified.")


if __name__ == "__main__":
    main()

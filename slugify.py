"""String normalization helpers."""

import re


def slugify(text: str) -> str:
    """Lowercase text, collapse non-ASCII-alphanumeric runs, and trim hyphens."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")

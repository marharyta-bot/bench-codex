"""Word frequency helpers."""

from collections import Counter
import re


def word_count(text: str) -> dict[str, int]:
    """Count ASCII-letter words, keeping straight apostrophes between letters.

    Keys are lowercase. Punctuation and whitespace separate words; empty text
    returns an empty dictionary.
    """
    words = (
        match.group().lower()
        for match in re.finditer(r"[A-Za-z]+(?:'[A-Za-z]+)*", text)
    )
    return dict(Counter(words))

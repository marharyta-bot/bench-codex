"""Palindrome checking helpers."""

import unicodedata


def is_palindrome(text: str) -> bool:
    """Return whether text reads the same both ways.

    Comparison ignores case, whitespace, and Unicode punctuation.
    """
    normalized = "".join(
        character.casefold()
        for character in text
        if not character.isspace()
        and not unicodedata.category(character).startswith("P")
    )
    return normalized == normalized[::-1]

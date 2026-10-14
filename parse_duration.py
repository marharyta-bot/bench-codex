"""Duration parsing helpers."""

import re


def parse_duration(text: str) -> int:
    """Parse a positive, compact duration such as '1h30m15s' into seconds.

    Whole-number components use lowercase h, m, s in that order, at most once
    each. Invalid or unsupported strings raise ValueError.
    """
    if not isinstance(text, str):
        raise TypeError("Duration must be a string.")

    message = (
        "Invalid duration: expected a positive whole-number duration using "
        "h, m, s in order (e.g. '1h30m15s')."
    )
    match = re.fullmatch(r"(?:([0-9]+)h)?(?:([0-9]+)m)?(?:([0-9]+)s)?", text)
    if match is None or not text:
        raise ValueError(message)

    hours, minutes, seconds = (int(part or 0) for part in match.groups())
    total = hours * 3600 + minutes * 60 + seconds
    if total == 0:
        raise ValueError(message)
    return total

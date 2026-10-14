# bench-codex
bench-codex

## String utilities

`slugify(text)` converts a string into a lowercase URL-friendly slug:

```python
from slugify import slugify

slugify("Hello, World!")  # "hello-world"
slugify("A...B__12")      # "a-b-12"
slugify(" --Hi-- ")      # "hi"
slugify("")              # ""
slugify("!@#$")          # ""
```

The repository had no established language or test runner, so this helper uses
Python 3 and the standard-library `unittest` runner without external dependencies.

Alphanumeric is currently interpreted as ASCII letters and digits (`a-z`, `0-9`)
after lowercasing. Other character runs become one hyphen, and boundary hyphens
are removed. No transliteration is performed. Whether to preserve Unicode letters
and digits remains an open product decision for human review.

## Duration parsing

`parse_duration(text)` converts compact durations into integer seconds:

```python
from parse_duration import parse_duration

parse_duration("90s")       # 90
parse_duration("2m")        # 120
parse_duration("1h30m")     # 5400
parse_duration("1h30m15s")  # 5415
```

The supported format uses whole-number components with lowercase `h`, `m`, `s`
units, each at most once and in that order, with a positive total. Each component
is optional, but at least one must be present. The entire input must match;
invalid strings such as `""`, `"abc"`, `"5x"`, `"-5m"`, or `"1h30m!"` raise
`ValueError` with a format explanation. Non-string inputs raise `TypeError`.

Whitespace, uppercase units, decimals, repeated or reordered units, and explicit
zero durations remain open product decisions for human review. They are outside
the currently supported format and raise `ValueError` pending clarification.

## Word frequencies

`word_count(text)` returns a dictionary of lowercase words and their counts:

```python
from word_count import word_count

word_count("The the THE")  # {"the": 3}
word_count("Hello, hello!")  # {"hello": 2}
word_count("don't")  # {"don't": 1}
word_count("hello,world")  # {"hello": 1, "world": 1}
word_count("")  # {}
```

Punctuation and whitespace separate words. Straight apostrophes are preserved
only inside words, so quoted text such as `"'don't'"` counts as `"don't"`.
The current tokenizer recognizes ASCII-letter words. Unicode letters, digits,
and curly apostrophes remain open product decisions for human review and are
outside the supported word format.

Run all tests from the repository root:

```sh
python3 -B -m unittest discover -v
```

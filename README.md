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

Run all tests from the repository root:

```sh
python3 -B -m unittest discover -v
```

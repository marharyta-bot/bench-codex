import unittest

from slugify import slugify


class SlugifyTests(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_lowercases_letters(self):
        self.assertEqual(slugify("ABCxyz"), "abcxyz")

    def test_collapses_non_alphanumeric_runs(self):
        for text in ("A...B__12", "A \t\n B---12", "A!?/B+==12"):
            with self.subTest(text=text):
                self.assertEqual(slugify(text), "a-b-12")

    def test_trims_leading_and_trailing_separators(self):
        self.assertEqual(slugify(" --Hi-- "), "hi")

    def test_empty_input(self):
        self.assertEqual(slugify(""), "")

    def test_symbols_only_input(self):
        self.assertEqual(slugify("!@#$"), "")

    def test_whitespace_only_input(self):
        self.assertEqual(slugify(" \t\n "), "")

    def test_preserves_digits(self):
        self.assertEqual(slugify("0123456789"), "0123456789")

    def test_preserves_existing_slug(self):
        self.assertEqual(slugify("already-a-slug-123"), "already-a-slug-123")


if __name__ == "__main__":
    unittest.main()

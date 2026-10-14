import unittest

from word_count import word_count


class WordCountTests(unittest.TestCase):
    def test_case_insensitive(self):
        self.assertEqual(word_count("The the THE"), {"the": 3})

    def test_ignores_punctuation(self):
        self.assertEqual(word_count("Hello, hello!"), {"hello": 2})

    def test_preserves_internal_apostrophes(self):
        self.assertEqual(word_count("don't"), {"don't": 1})
        self.assertEqual(word_count("Don't DON'T don't"), {"don't": 3})

    def test_empty_input(self):
        self.assertEqual(word_count(""), {})

    def test_punctuation_separates_adjacent_words(self):
        for text in ("hello,world", "hello...world", "hello-world", "hello_world"):
            with self.subTest(text=text):
                self.assertEqual(word_count(text), {"hello": 1, "world": 1})

    def test_apostrophes_at_word_boundaries(self):
        self.assertEqual(word_count("'don't' 'hello'"), {"don't": 1, "hello": 1})
        self.assertEqual(word_count("hello''world"), {"hello": 1, "world": 1})

    def test_multiple_internal_apostrophes(self):
        self.assertEqual(word_count("rock'n'roll"), {"rock'n'roll": 1})

    def test_whitespace_only_input(self):
        self.assertEqual(word_count(" \t\n "), {})

    def test_punctuation_only_input(self):
        self.assertEqual(word_count("!@#$,.'"), {})

    def test_counts_multiple_words(self):
        result = word_count("One fish, two fish.\nONE\tfish!")
        self.assertEqual(result, {"one": 2, "fish": 3, "two": 1})
        self.assertIs(type(result), dict)


if __name__ == "__main__":
    unittest.main()

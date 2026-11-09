import unittest

from is_palindrome import is_palindrome


class IsPalindromeTests(unittest.TestCase):
    def test_panama_example(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_non_palindrome(self):
        for text in ("hello", "HELLO", "he llo", "h.e.l.l.o"):
            with self.subTest(text=text):
                self.assertFalse(is_palindrome(text))

    def test_ignores_case_spaces_and_punctuation(self):
        for text in ("RaceCar", "race car", "R.a.c.e.c.a.r"):
            with self.subTest(text=text):
                self.assertTrue(is_palindrome(text))

    def test_preserves_digits(self):
        self.assertFalse(is_palindrome("1aa"))

    def test_preserves_non_punctuation_symbols(self):
        self.assertFalse(is_palindrome("a🙂ba"))

    def test_empty_and_ignored_characters(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome(" ,.! \t\n"))


if __name__ == "__main__":
    unittest.main()

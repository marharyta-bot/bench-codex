import unittest

from parse_duration import parse_duration


class ParseDurationTests(unittest.TestCase):
    def test_specified_conversions(self):
        for text, expected in (
            ("90s", 90),
            ("2m", 120),
            ("1h30m", 5400),
            ("1h30m15s", 5415),
        ):
            with self.subTest(text=text):
                result = parse_duration(text)
                self.assertEqual(result, expected)
                self.assertIsInstance(result, int)

    def test_optional_components(self):
        for text, expected in (("1h", 3600), ("1h15s", 3615), ("2m15s", 135)):
            with self.subTest(text=text):
                self.assertEqual(parse_duration(text), expected)

    def test_specified_invalid_inputs(self):
        for text in ("", "abc", "5x", "-5m"):
            with self.subTest(text=text):
                with self.assertRaisesRegex(ValueError, "Invalid duration.*h, m, s"):
                    parse_duration(text)

    def test_rejects_unsupported_units(self):
        for text in ("1d", "1h30x", "1h30m15ms"):
            with self.subTest(text=text):
                with self.assertRaisesRegex(ValueError, "Invalid duration"):
                    parse_duration(text)

    def test_rejects_partial_matches(self):
        for text in ("abc1h", "1h30", "1h30m15s!", "1h-5m"):
            with self.subTest(text=text):
                with self.assertRaisesRegex(ValueError, "Invalid duration"):
                    parse_duration(text)

    def test_rejects_non_string_inputs(self):
        for value in (None, 90, 1.5, b"90s"):
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError, "Duration must be a string"):
                    parse_duration(value)


if __name__ == "__main__":
    unittest.main()

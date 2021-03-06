import unittest
from ufo_game import word_regex

class TestWordRegex(unittest.TestCase):

    def test_regex_pattern(self):
        test_patterns = [
            "_R___",
            "",
            None,
            ['_', 'R', '_', '_', '_']
        ]
        expected_regex = [
            "^[a-zA-Z]{1}[Rr]{1}[a-zA-Z]{1}[a-zA-Z]{1}[a-zA-Z]{1}$",
            "^$",
            "^$",
            "^[a-zA-Z]{1}[Rr]{1}[a-zA-Z]{1}[a-zA-Z]{1}[a-zA-Z]{1}$"
        ]

        for pattern, expected in zip(test_patterns, expected_regex):
            result = word_regex.buildRegex(pattern)
            self.assertEqual(expected, result, msg=f"Test pattern \"{pattern}\" failed with result \"{result}\".")

    def test_exclude_pattern(self):
        test_letters = [
            None,
            "",
            "A",
            "ZDE",
            ['C','A']
        ]
        expected_regex = [
            "[a-zA-Z]*",
            "[a-zA-Z]*",
            "^((?![Aa]).)*$",
            "^((?![ZzDdEe]).)*$",
            "^((?![CcAa]).)*$"
        ]

        for pattern, expected in zip (test_letters, expected_regex):
            result = word_regex.buildExcludeRegex(pattern)
            self.assertEqual(expected, result, msg=f"Test pattern \"{pattern}\" failed with result \"{result}\".")
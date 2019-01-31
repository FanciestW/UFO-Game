import unittest
import word_regex from ufo_game

class TestWordRegex(unittest.TestCase):

    def test_regex_pattern(self):
        test_patterns = ["_R___"]
        expected_regex = ["^[a-zA-Z]{1}[Rr]{1}[a-zA-Z]{1}[a-zA-Z]{1}[a-zA-Z]{1}$"]

        for pattern, expected in zip(test_patterns, expected_regex):
            result = word_regex.buildRegex(pattern)
            self.assertEqual(expected, result, msg=f"Test pattern {pattern} failed.")

    def test_exclude_pattern(self):
        test_letters = [None, "A", "ZDE", ['C','A']]
        expected_regex = ["[a-zA-Z]*", "^((?![Aa]).)*$", "^((?![ZzDdEe]).)*$", "^((?![CcAa]).)*$"]

        for pattern, expected in zip (test_letters, expected_regex):
            result = word_regex.buildExcludeRegex(pattern)
            self.assertEqual(expected, result, msg=f"Test patter {pattern} failed.")
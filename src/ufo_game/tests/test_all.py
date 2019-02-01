import unittest

from ufo_game.tests import test_base
from ufo_game.tests import test_word_regex

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_base))
suite.addTests(loader.loadTestsFromModule(test_word_regex))

runner = unittest.TextTestRunner()
result = runner.run(suite)
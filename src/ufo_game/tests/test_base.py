import unittest
from ufo_game.base import Game

class TestWordRegex(unittest.TestCase):

    def test_single_session(self):
        game = Game.getInstance()
        game.setNewCodeWord()
        game2 = Game.getInstance()
        self.assertEqual(game._Game__codeword, game._Game__codeword, msg="Singleton Error")
        
    def test_reset_game(self):
        game = Game.getInstance()
        game.incorrent_guesses = ['T', 'D']
        game.resetGame()
        self.assertEqual(game.incorrent_guesses, [])

    def test_guess(self):
        game = Game.getInstance()
        test_words = ["TEST", "ONE", "WORD", "ZIP"]
        test_guesses = ['T', 'D', 'W', 'E']
        expected_results = [1, 0, 1, 0]
        # Expected results 1 means correct guess, 0 incorrect guess.
        for word, letter, expected in zip(test_words, test_guesses, expected_results):
            game.setNewCodeWord(word)
            result = game.guess(letter)
            self.assertEqual(expected, result)

        
    def test_set_random_code_word(self):
        test_code_words = ["Test", "MAKE", "abc"]
        expected_code_words = ["TEST", "MAKE", "ABC"]

        for codeword, expected in zip(test_code_words, expected_code_words):
            game = Game.getInstance()
            game.setNewCodeWord(codeword=codeword)
            self.assertEqual(game._Game__codeword, expected)
            self.assertEqual(len(game._Game__codeword), len(codeword))

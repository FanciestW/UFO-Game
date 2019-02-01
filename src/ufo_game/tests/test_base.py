import os
import unittest
from ufo_game.base import Game

class TestWordRegex(unittest.TestCase):

    def test_single_session(self):
        game = Game.getInstance()
        game.setNewCodeWord()
        game2 = Game.getInstance()
        self.assertEqual(game._Game__codeword, game._Game__codeword, msg="Singleton Error")
        del game

    def test_resetGame(self):
        game = Game.getInstance()
        wordfile = open(f"{os.path.dirname(__file__)}/test_word_list.txt", "r")
        game.words = wordfile.readlines()
        wordfile.close()
        game.incorrent_guesses = ['T', 'D']
        game.resetGame()
        self.assertEqual(game.incorrent_guesses, [])
        del game

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
        del game

        
    def test_setRandomCodeWord(self):
        test_code_words = ["Test", "MAKE", "abc"]
        expected_code_words = ["TEST", "MAKE", "ABC"]

        for codeword, expected in zip(test_code_words, expected_code_words):
            game = Game.getInstance()
            game.setNewCodeWord(codeword=codeword)
            self.assertEqual(game._Game__codeword, expected)
            self.assertEqual(len(game._Game__codeword), len(codeword))
        del game
    
    def test_countDictMatches(self):
        game = Game.getInstance()
        wordfile = open(f"{os.path.dirname(__file__)}/test_word_list.txt", "r")
        game.words = wordfile.readlines()
        wordfile.close()
        print(game.words)
        del game

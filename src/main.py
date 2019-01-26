import string
import random
import os
from ufo_game.base import Game

def main_loop():
    game = Game("nouns.txt")
    game.beginNewGame()
    game.status()
    print(game._Game__codeword)
        

if __name__ == "__main__":
    main_loop()
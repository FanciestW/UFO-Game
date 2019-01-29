from ufo_game.base import Game
from ufo_game import word_regex

def main():
    game = Game()
    # game.startGame()
    print(word_regex.buildRegex("_R___", ['D', 'w']))

if __name__ == "__main__":
    main()
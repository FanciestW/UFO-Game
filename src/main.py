from ufo_game.base import Game

def main_loop():
    game = Game("nouns.txt")
    game.startGame()
    print(game._Game__codeword)
        

if __name__ == "__main__":
    main_loop()
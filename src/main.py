from ufo_game.base import Game

def main():
    game = Game.getInstance()
    game.startGame()
    del game

if __name__ == "__main__":
    main()
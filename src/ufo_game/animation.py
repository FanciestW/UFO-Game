import time
import os
from . import ufo_animation

def ufo_win():
    for frame in ufo_animation.win:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(0.15)

def ufo_lose():
    for frame in ufo_animation.lose:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(0.15)
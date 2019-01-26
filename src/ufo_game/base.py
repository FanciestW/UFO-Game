import random
import string
import os
from . import ufo

class Game:

    __codeword = ""
    abduction_state = 0
    available_letters = string.ascii_uppercase;
    incorrent_guesses = []
    codeword_status = []
    file = None
    file_lines = None

    def __init__(self, fileName):
        self.file = open(fileName, "r")
        self.file_lines = self.file.readlines()

    def setRandomCodeWord(self):
        random_int = random.randint(0, len(self.file_lines))
        self.__codeword = self.file_lines[random_int].strip().upper()
            
    def resetGame(self):
        self.abduction_state = 0
        self.available_letters = string.ascii_uppercase
        self.incorrent_guesses = []
        self.setRandomCodeWord()
        self.codeword_status = ['_']*len(self.__codeword)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("UFO: The Game")
        print("Instructions: save us from alien abduction by guessing letters in the codeword.", end="\n\n")
        self.status()

    def startGame(self):
        self.resetGame()

    def status(self):
        # TODO::Print state of game
        print(ufo.states[self.abduction_state])
        print("Incorrect Guesses:")
        if not self.incorrent_guesses:
            print("None", end="\n\n")
        else:
            print(*self.incorrent_guesses, end="\n\n")
        print("Codeword:")
        print(*self.codeword_status, end="\n\n")
        

    def guess(self, letter):
        if letter not in self.available_letters:
            print('Already Guessed')
            return
        
        if letter in self.__codeword:
            self.status()
            print('Good job')
        else:
            self.abduction_state += 1
            self.status()
            print('Try again')


        
import random
import string
import os
import re
from . import ufo
from . import animation
from . import word_regex

class Game:

    __codeword = ""
    abduction_state = 0
    available_letters = list(string.ascii_uppercase);
    incorrent_guesses = []
    codeword_status = []
    wordlist_file = None
    words = None

    def __init__(self, wordlist = None):
        default_wordlist = f"{os.path.dirname(__file__)}/wordlist.txt"
        if wordlist == None:
            self.wordlist_file = open(default_wordlist, "r")
        else:
            self.wordlist_file = open(wordlist, "r")

        self.words = self.wordlist_file.readlines()
    
    def startGame(self):
        while(True):
            self.resetGame()
            self.gameLoop()
            ans = input("Would you like to play again (Y/N)? ").upper()
            if ans == 'Y':
                continue
            else:
                print("\nGoodbye!")
                break

    def setRandomCodeWord(self):
        random_int = random.randint(0, len(self.words))
        self.__codeword = self.words[random_int].strip().upper()

    def gameLoop(self):
        while(True):
            if '_' not in self.codeword_status:
                self.winGame()
                break
            elif self.abduction_state >= 6:
                self.loseGame()
                break
            
            user_input = input("Please enter your guess: ")
            print('\n')
            if not re.match("^[a-zA-Z]{1}", user_input):
                print("Bad input. Try again\n")
                continue
            self.guess(user_input.upper())
        
        print(f"The codeword is: {self.__codeword}.\n")
  
    def guess(self, letter):
        letter = letter.upper()
        if letter in self.incorrent_guesses or letter in self.codeword_status:
            print("You can only guess that letter once, please try again.\n")
            return
        if letter not in self.available_letters:
            print("I cannot understand your input. Please guess a single letter.\n")
            return
        print(type(self.available_letters))
        self.available_letters.remove(letter)

        if letter in self.__codeword:
            indices = [i for i, ch in enumerate(self.__codeword) if ch == letter]
            for i in indices:
                self.codeword_status[i] = letter
            os.system('cls' if os.name == 'nt' else 'clear')
            if '_' in self.codeword_status:
                print("Correct! You're closer to cracking the codeword.\n")
                self.status()
        else:
            self.abduction_state += 1
            self.incorrent_guesses.append(letter)
            os.system('cls' if os.name == 'nt' else 'clear')
            if self.abduction_state < 6:
                print("Incorrect! The tractor beam pulls the person in further.\n")
                self.status()

    def resetGame(self):
        self.abduction_state = 0
        self.available_letters = list(string.ascii_uppercase)
        self.incorrent_guesses = []
        self.setRandomCodeWord()
        self.codeword_status = ['_']*len(self.__codeword)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("UFO: The Game")
        print("Instructions: save us from alien abduction by guessing letters in the codeword.", end="\n\n")
        self.status()    
    
    def status(self):
        # Uncomment below to view codeword while play testing
        # print(self.__codeword)
        print(ufo.states[self.abduction_state])
        print("Incorrect Guesses:")
        if not self.incorrent_guesses:
            print("None", end="\n\n")
        else:
            print(*self.incorrent_guesses, end="\n\n")
        print("Codeword:")
        print(*self.codeword_status, end="\n\n")
        print("Number of dictionary matches: %s" %(self.countDictMatches()), end="\n\n")

    def countDictMatches(self):
        word_pattern = ''.join(self.codeword_status)
        regex = word_regex.buildRegex(word_pattern)
        excludeRegex = word_regex.buildExcludeRegex(self.incorrent_guesses)
        print(regex)
        print(excludeRegex)
        count = 0
        for word in self.words:
            if re.match(regex, word) and re.match(excludeRegex, word):
                count += 1

        return count

    def winGame(self):
        animation.ufo_win()
        print("Correct! You saved the person and earned a medal of honor!")

    def loseGame(self):
        animation.ufo_lose()
        print("Incorrect! The person has been abducted!")
        
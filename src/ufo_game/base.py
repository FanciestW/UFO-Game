import random
import string
import os
import re
from ufo_game import ufo
from ufo_game import animation
from ufo_game import word_regex

class Game:

    __instance = None
    __codeword = ""
    abduction_state = 0
    available_letters = list(string.ascii_uppercase);
    incorrent_guesses = []
    codeword_status = []
    wordlist_file = None
    words = None

    @staticmethod
    def getInstance():
        """Singleton check to make sure only one game instance runs at a time."""
        if Game.__instance == None:
            Game()
        return Game.__instance

    def __init__(self, wordlist = None):
        """Creates new game instance and sets it to default or passed wordlist."""

        if Game.__instance != None:
            raise Exception("There is a game session already in progress.")
        else:
            Game.__instance = self

        default_wordlist = f"{os.path.dirname(__file__)}/wordlist.txt"
        if wordlist == None:
            self.wordlist_file = open(default_wordlist, "r")
        else:
            self.wordlist_file = open(wordlist, "r")

        self.words = self.wordlist_file.readlines()
    
    def startGame(self):
        """Begins game session and run loop for replay."""

        welcomeMsg = (
            "UFO: The Game\n"
            "Instructions: save us from alien abduction by guessing letters in the codeword.\n"
        )
        while(True):
            self.resetGame()
            self.status(msg=welcomeMsg)
            self.gameLoop()
            ans = input("Would you like to play again (Y/N)? ").upper()
            if ans == 'Y':
                continue
            else:
                print("\nGoodbye!")
                break

    def gameLoop(self):
        """Game loop for a new code word and game session."""

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
            result = self.guess(user_input.upper())
            if result == 0:
                self.status(msg="Incorrect! The tractor beam pulls the person in further.\n")
            elif result == 1:
                self.status(msg="Correct! You're closer to cracking the codeword.\n")
        
        print(f"The codeword is: {self.__codeword}.\n")
  
    def guess(self, letter):
        """Guesses a letter for the current game session and checks input."""

        letter = letter.upper()
        if letter in self.incorrent_guesses or letter in self.codeword_status:
            print("You can only guess that letter once, please try again.\n")
            return -1
        if letter not in self.available_letters:
            print("I cannot understand your input. Please guess a single letter.\n")
            return -1
        print(type(self.available_letters))
        self.available_letters.remove(letter)

        if letter in self.__codeword:
            indices = [i for i, ch in enumerate(self.__codeword) if ch == letter]
            print(indices)
            for i in indices:
                self.codeword_status[i] = letter
            os.system('cls' if os.name == 'nt' else 'clear')
            if '_' in self.codeword_status:
                return 1

        else:
            self.abduction_state += 1
            self.incorrent_guesses.append(letter)
            if self.abduction_state < 6:
                return 0
    
    def setNewCodeWord(self, codeword=None):
        """Sets an explicit or random new codeword."""

        if codeword == None or codeword == "":
            random_int = random.randint(0, len(self.words)-1)
            self.__codeword = self.words[random_int].strip().upper()
        else:
            codeword = codeword.strip().upper()
            self.words.append(codeword)
            self.__codeword = codeword

        self.codeword_status = ['_']*len(self.__codeword)

    def resetGame(self):
        """Resets game session data in preparation for a new game."""

        self.abduction_state = 0
        self.available_letters = list(string.ascii_uppercase)
        self.incorrent_guesses = []
        self.setNewCodeWord()   
    
    def status(self, msg=""):
        """Prints status of game to display current game progress."""

        os.system('cls' if os.name == 'nt' else 'clear')
        print(msg)
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
        """Uses word_regex to build a regex to test possible matches in wordlist."""

        word_pattern = ''.join(self.codeword_status)
        regex = word_regex.buildRegex(word_pattern)
        excludeRegex = word_regex.buildExcludeRegex(self.incorrent_guesses)
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
        
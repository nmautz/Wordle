import wordle
import os

os.system("")  # enables ansi escape characters in terminal

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "YELLOW": "\u001b[33m",
    "WHITE": "\u001b[37m",
    "ENDC": "\033[0m"
}


def build_wordle_string(game):
    word = game.word
    prev_guesses = game.prev_guesses
    wordle_string = ""

    for i, guess in enumerate(prev_guesses):
        # create one line
        string = ""
        for c, char in enumerate(guess):
            added_char = False
            is_in_word = False
            for j, word_char in enumerate(word):
                if not added_char:
                    if char is word_char and c is j:
                        string += (COLOR.get("GREEN") + char + COLOR.get("ENDC"))
                        added_char = True
                    elif char is word_char:
                        is_in_word = True
            if not added_char:
                if is_in_word:
                    string += (COLOR.get("YELLOW") + char + COLOR.get("ENDC"))
                else:
                    string += (COLOR.get("WHITE") + char + COLOR.get("ENDC"))
        wordle_string += (string + "\n")
    return wordle_string

class WordleController:

    def __init__(self):
        self.game = wordle.WordleGame()
        self.GUESS_STRING = "Please enter a 5 letter word\n"

    def start_game(self):
        player_guess = ""
        while self.game.guess_count < self.game.max_guesses and player_guess is not self.game.word:

            print(build_wordle_string(self.game))
            #print("-------------------------------")
            #print("the word is: " + self.game.word)
            print("Guesses remaining: " + str(self.game.max_guesses - self.game.guess_count))

            player_guess = input(self.GUESS_STRING)
            while not self.game.is_valid_guess(player_guess):
                print("Invalid Guess, try again")
                player_guess = input(self.GUESS_STRING)

            self.game.guess(player_guess)

        if player_guess is self.game.word:
            print("\n\n\nYou got it!!!\n\"" + self.game.word + "\" was the word")
        else:
            print("\n\n\nYou lose\nThe word was \n\"" + self.game.word + "\"")

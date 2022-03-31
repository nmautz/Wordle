import random

import wordle
import wordle_controller


def find_valid_words(valid_letters, all_letters_guessed, wordlist):
    if len(all_letters_guessed) != 0:
        valid_words = wordlist
        count = 0 #number of good words found
        max = 100 #max num of good words to stop at

        if isinstance(valid_words, list):
            for word in wordlist:
                if count < max:
                    bad_word = False
                    for letter in all_letters_guessed:
                        if letter not in valid_letters:
                            if letter in word:
                                bad_word = True
                        else:
                            if not letter in word:
                                bad_word = True
                    if not bad_word:
                        valid_words.append(word)
                        count += 1
        return valid_words
    return wordlist


class WordleBot:

    def __init__(self):
        self.game = wordle.WordleGame()

    def start_game(self):

        while self.game.guess_count < self.game.max_guesses:
            valid_words = find_valid_words(self.game.letters_in_word, self.game.guessed_letters, self.game.wordlist)
            self.game.guess(random.choice(valid_words))
            print("---------")
            print("Round " + str(self.game.guess_count))
            print("---------")
            print(wordle_controller.build_wordle_string(self.game))
            print("---------")

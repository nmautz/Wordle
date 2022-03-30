import random


def load_wordlist():
    wordlist_file = open("Wordlist.txt", "r")

    word = wordlist_file.readline()

    word = word[0:word.__len__()-1]

    words = [word]

    while word != "":
        word = word[0:word.__len__() - 1]
        words.append(word)
        word = wordlist_file.readline()

    return words


class WordleGame:

    def __init__(self):
        self.wordlist = load_wordlist()
        self.word = random.choice(self.wordlist)
        self.max_guesses = 6
        self.guess_count = 0
        self.letters_in_word = []
        self.guessed_letters = []
        self.guesses = []
        self.revealed_word = ['_', '_', '_', '_', '_']

    def is_valid_guess(self, word):
        if word in self.wordlist:
            return True
        return False

    def guess(self, word):
        self.guess_count += 1
        self.add_letters_from_word(word)
        self.guesses.append(word)

        if word is self.word:
            return True
        else:
            return False

    def add_letters_from_word(self, word):
        for char in word:
            for c, g_char in enumerate(self.word):
                if char == g_char:
                    if char not in self.letters_in_word:
                        self.letters_in_word.append(char)
                        self.revealed_word[c] = char


            if char not in self.guessed_letters:
                self.guessed_letters.append(char)

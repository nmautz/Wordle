import random


def load_wordlist():
    wordlist_file = open("Wordlist.txt", "r")

    word = wordlist_file.readline()

    words = [word]

    while word != "":
        words.append(word)
        word = wordlist_file.readline()

    return words


class WordleGame:

    def __init__(self):
        self.wordlist = load_wordlist()
        self.word = random.choice(self.wordlist)
        self.max_guesses = 6
        self.guesses = 0

    def guess(self, word):
        if self.guesses < self.max_guesses:
            if word in self.wordlist:
                self.guesses += 1

                if word is self.word:
                    return True
                else:
                    return False

            else:
                return False



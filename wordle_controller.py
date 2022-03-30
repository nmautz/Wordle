import wordle


class WordleController:



    def __init__(self):
        self.game = wordle.WordleGame()
        self.GUESS_STRING = "Please enter a 5 letter word\n"

    def start_game(self):
        player_guess = ""
        while self.game.guess_count < self.game.max_guesses and player_guess is not self.game.word:
            print("Previous Guesses")
            print(self.game.guesses)
            print("Wordle Revealed")
            print(self.game.revealed_word)
            print("All Guessed Letters")
            print(self.game.guessed_letters)
            print("Guesses remaining: " + str(self.game.max_guesses-self.game.guess_count))

            player_guess = input(self.GUESS_STRING)
            while not self.game.is_valid_guess(player_guess):
                print("Invalid Guess, try again")
                player_guess = input(self.GUESS_STRING)

            self.game.guess(player_guess)

        if player_guess is self.game.word:
            print("\n\n\nYou got it!!!\n\"" + self.game.word + "\" was the word")
        else:
            print("\n\n\nYou lose\nThe word was \n\"" + self.game.word + "\"")





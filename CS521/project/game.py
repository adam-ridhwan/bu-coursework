class Hangman:
    def __init__(self, word):
        self.__word = word					# chosen random word
        self.asterisk = "*" * len(word)	    # hides the word
        self.answer = list(self.asterisk)  # updated word shown
        self.correctDuplicate = "" 			# stores duplicates of correct letter
        self.wrongDuplicate = ""			# stores duplicates of wrong letter
        self.correct = []					# stores the correct letter
        self.wrong = []						# stores the wrong letter
        self.counter = 0					# number of tries

    # private class

    def chosenWord(self):
        return list(self.__word)

    # reprt function
    def __repr__(self):
        return repr(Hangman.chosenWord)

    # function for correct guesses
    def correctGuess(self, letter):
        if letter in self.chosenWord():
            for i in range(len(self.answer)):
                if letter == self.chosenWord()[i]:
                    self.answer[i] = self.chosenWord()[i]
                    self.correctDuplicate += letter
                    self.correct.append(letter)

    # function to print messages duplicate correct letters
    def duplicateCorrectGuess(self, letter):
        print(letter + " already in word.")

    # function for wrong guesses
    def wrongGuess(self, letter):
        self.wrongDuplicate += letter
        self.counter += 1
        self.wrong.append(letter)

    # function to print messages duplicate wrong guesses
    def duplicateWrongGuess(self, letter):
        print("You already guessed " + letter + " wrong.")

    # function to print winning message
    def winGame(self):
        print("\nYou guessed the word correctly! You win!")
        print("The secret word is '" + str("".join(self.chosenWord())) +
              "'. You missed " + str(self.counter) + " times")
        print("Correct letters: ", end="")
        for i in self.correct:
            print(i, end=" ")
        print()
        print("Wrong letters: ", end="")
        for i in self.wrong:
            print(i, end=" ")
        print()

    # function to print losing message
    def loseGame(self):
        print('\nSorry, you hanged the man. You lost.')
        print("The secret word is '" + str("".join(self.chosenWord())) +
              "'. You missed " + str(self.counter) + " times")
        print("Correct letters: ", end="")
        for i in self.correct:
            print(i, end=" ")
        print()
        print("Wrong letters: ", end="")
        for i in self.wrong: 
            print(i, end=" ")
        print()

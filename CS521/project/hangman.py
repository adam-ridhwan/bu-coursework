from game import Hangman
import random

# list of images of hangman for 0-6 tries
image = [
    '  +---+   \n  |   |   \n      |   \n      |   \n      |   \n      |   \n=========',
    '  +---+   \n  |   |   \n  0   |   \n      |   \n      |   \n      |   \n=========',
    '  +---+   \n  |   |   \n  0   |   \n  |   |   \n      |   \n      |   \n=========',
    '  +---+   \n  |   |   \n  0   |   \n /|   |   \n      |   \n      |   \n=========',
    '  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n      |   \n      |   \n=========',
    '  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n /    |   \n      |   \n=========',
    '  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n / \\  |   \n      |   \n========='
]


def main():

    # random word picked from a given list and stored into a variable then called into class function
    words = ["fall", "spring", "winter", "summer"]
    randomWord = random.choice(words)
    game = Hangman(randomWord)

    # prints a welcome message the top of the console
    print("\n============================")
    print("Welcome to a game of hangman")
    print("============================\n")
    print("Guess the secret word")

    # while loop used to check if there are no asterisks or tries exceeds 6
    while game.chosenWord() != game.answer and game.counter != 6:

        # prints image of hangman
        print(image[game.counter])

        # prints the hidden secret word
        print("Secret Word: " + "".join(game.answer))

        '''
            - while loop used to check if user entered the correct inputs using try block
                input not accepted are: -
                    - duplicates
                    - digits
                    - multiple characters
                    - spaces
                    - symbols
        '''
        while True:
            try:
                letter = str(input("Enter a letter: "))
                print()
                if len(letter) == 1 and letter.isalpha():
                    if letter in game.wrongDuplicate:
                        game.duplicateWrongGuess(letter)
                        continue
                    elif letter not in game.chosenWord():
                        game.wrongGuess(letter)
                    else:
                        if letter in game.correctDuplicate:
                            game.duplicateCorrectGuess(letter)
                            continue
                        else:
                            game.correctGuess(letter)
                    break
                else:
                    raise TypeError

            except TypeError:
                if letter.isdigit():
                    print("Numbers not accepted.")
                elif (len(letter) >= 2) or letter.isdigit():
                    print("Multiple characters not accepted.")
                elif letter.isspace():
                    print("Spaces not accepted.")
                else:
                    print("Symbols not accepted.")
                continue

    # if-else statement checks to see if user wins the game within six tries. Otherwise, the user loses the game
    if game.chosenWord() == game.answer:
        print(image[game.counter])
        print("Secret Word: " + "".join(game.answer))
        game.winGame()

    else:
        print(image[game.counter])
        print("Secret Word: " + "".join(game.answer))
        game.loseGame()

    # while loop used to ask user if the want to replay the game
    while True:
        restart = input("\nDo you want to guess another word? Enter y or n: ")
        if restart == "y":
            main()
        elif restart == "n":
            exit()
        else:
            print("Invalid input")
            continue


# starts the game
main()

# function main used to start and restart program
def main():
    import random

    # words is defined to store list of words
    words = ["write", "that", "program"]
    
    # random_word is defined to store a random word from variable words
    random_word = random.choice(words)
    
    # asterisk is defined for hidden word
    asterisk = "*" * len(random_word)

    # answer is the separated version of asterisk
    answer = list(asterisk)
    
    # counter is used to count the number of times user guessed the word wrong
    counter = 0

    # while loop is ued to loop through the guessing question
    while list(random_word) != answer:  
        user_guess = input("(Guess) Enter a letter in word " + "".join(answer) + " > ")
        # checks to see if user entered a letter
        if len(user_guess) > 1:
            print("Invalid input. Please enter only 1 letter.")

        # checks to see if user's guess letter is in the word
        elif user_guess in str(answer):
            print(user_guess + " is already in the word")

        # checks to see if user guessed the wrong letter
        elif user_guess not in list(random_word):
            print(user_guess + " is not in word")
            counter += 1

        # for loop used to check if user's guessed letter is in the word and replaces the asterisk with letter
        for i in range(len(answer)):
            if user_guess == list(random_word)[i]:
                answer[i] = list(random_word)[i]
        
    print("The word is " + random_word + ". You missed " + str(counter) + " time\n")   

    # while loop used to ask if user wants to restart the program or not
    while True:
        restart = input("Do you want to guess another word? Enter y or n> ")
        if restart == "y":
            main()
        elif restart == "n":
            exit()
        else: 
            print("Invalid input")
            continue

main()
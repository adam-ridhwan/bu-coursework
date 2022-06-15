def main():
    # checks to see if in correct file directory - will exit program if file is not found
    try: 
        dataSource = open("charles_dickens.txt", "r")
    except:
        print("Could not find text file. Please try again")
        exit()

    # dictionary defined as a counter to count the frequency of a character
    characters = {
        "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0,
    }

    # while loop used to append value 1 to characters dictionary for each specific character
    lineRead = "\n"
    while lineRead.endswith("\n"):
        lineRead = dataSource.readline()
        for i in lineRead.upper():
            if i in characters:
                characters[i] += 1

    # calculates the sum of characters in txt.file
    sumCharacters = sum(characters.values())

    # totaAlphabet defined to store the percentages of character
    totalCharacters = {
        "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0,
    }

    # for loop used to append the percentage of each character to totalCharacters dictionary
    for i in totalCharacters:
        totalCharacters[i] = format(((characters[i]/sumCharacters)*100), '.2f')

    # prints the distribution table using for loop
    print("Char\tFreq\t%total")
    for i in characters:
        print('{}  {:>8}  {:>7}'.format(i, characters[i], totalCharacters[i]))
        
main()

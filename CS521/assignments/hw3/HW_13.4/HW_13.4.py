import random,sys

# variable filename defined to store user input
fileName = input("Enter a filename: ")

# checks to see if test.txt exists. Program exits if it does
if fileName == "test.txt":
    print("The file already exists")
    sys.exit()

# opens a new txt file 
with open(fileName, "w") as aFile:
    print("The 100 random integers written are: ")
    # creates 100 numbers and prints in console
    for i in range(100):
        line = str(random.randint(1,100))
        aFile.write(line)
        print(line, end=" ")

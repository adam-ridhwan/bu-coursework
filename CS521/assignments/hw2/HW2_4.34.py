# variable is created to ask user input
hex_character = input("Enter a hex character: ")

# list is created for alphbets a - f
alphabet = ['a', 'b', 'c', 'd', 'e', 'f']

# if-statement checks to see if user input is in list
if hex_character.lower() in alphabet: 
    print("The decimal value is " + str(int(hex_character, 16)))

# elif-statement checks to see if user input is an integer
elif hex_character.isdigit():
    print("The decimal value is " + str(int(hex_character, 16)))

# else-statement prints error message if user input enters invalid input
else:
    print("Invalid input")



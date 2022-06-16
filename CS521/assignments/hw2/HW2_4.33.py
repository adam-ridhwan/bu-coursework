# variable interger is created to ask user to input a value between 0 - 15
integer = int(input("enter a decimal value (0 to 15): "))

# if-statement checks to see if user input is between the range. Then calculates the hex_number
if 0 <= integer <= 15:
    hex_number = hex(integer)
    print("The hex value is " + str(hex_number.upper())[-1])
    
# else-statement prints error message if user inputs invalid number
else:
    print("Invalid input")
# number is defined to ask user to input number within range 0 - 1000
number = input("Enter a number between 0 and 1000: ")

# first_number is defined for first number
first_number = int(number) % 10 

# second_number is defined for second number
remaining_number = int(number) // 10
second_number = int(remaining_number) % 10

# third_number is defined for third number
remaining_number = int(remaining_number) // 10
third_number = int(remaining_number) % 10

# sum is defind for the total of all 3 numbers
sum = first_number + second_number + third_number

# prints result
print("The sum of the digits is " + str(sum))

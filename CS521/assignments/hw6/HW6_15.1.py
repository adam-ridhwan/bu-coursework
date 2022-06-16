
def sumDigits(number):
    # checks to see if number is less than 10
    if number < 10:
        return number
    # recursion     
    else:
        x = number // 10
        y = number % 10
        return y + sumDigits(x)

# asks user to input number
number = int(input("Enter a number: "))

# prints results
print("The sum of digits is", sumDigits(number))


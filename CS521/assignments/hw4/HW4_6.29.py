# function isValid() returns true if the card number is valid
def isValid(number):
    if (getSize(number) >= 13 and getSize(number) <= 16) \
        and ((prefixMatched(number, 4) or prefixMatched(number, 5) or prefixMatched(number, 37) or prefixMatched(number, 6))) \
        and ((sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0):
        return True
    return False

# function sumOfDoubleEvenPlace() returns the sum of numbers in even place
def sumOfDoubleEvenPlace(number):
    evenPlaceSum = 0
    for i in getDigit(number):
        evenPlaceSum += i
    return evenPlaceSum

# function getDigit() returns the list of numbers in even place
def getDigit(number):
    number = list(str(number))
    number.reverse()
    everyEvenPlace = number[1::2]
    evenPlaceList = []
    for i in everyEvenPlace:
        digit = int(i) * 2
        if len(str(digit)) == 1:
            evenPlaceList.append(digit)
        elif len(str(digit)) > 1:
            sumDigits = 0 
            for i in list(str(digit)):
                sumDigits += int(i)
            evenPlaceList.append(sumDigits)
    return evenPlaceList 
        
# function sumOfOddPlace() returns the sum of numbers in odd place
def sumOfOddPlace(number):
    number = list(str(number))
    number.reverse()
    everyOddPlace = number[::2]
    oddPlaceSum = 0
    for i in everyOddPlace:
        oddPlaceSum += int(i)
    return oddPlaceSum

# function prefixMatched() returns true if prefix matches
def prefixMatched(number, d):
    return getPrefix(number, d) == d

# functions getSize() returns the length of digits
def getSize(d):
    d = int(len(list(str(d))))
    return d
    
# getPrefix returns the prefix number of user input
def getPrefix(number, k):
    k = len(list(str(k)))
    if getSize(number) > k:
        number = int(''.join([i for i in str(number)])[:k])
        return number
    return number

# calls and prints main function
number = int(input("Enter credit card number: "))
print(isValid(number))
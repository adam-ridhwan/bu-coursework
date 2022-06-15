# minutes is dfined to ask user's input for number of minutes
minutes = input("Enter the number of minutes: ")

# years is defined to calculate number of years
years = int(minutes) // 525600

# remaining_minutes is defined to calculate remaining minutes
remaining_minutes = int(minutes) % 525600

# day is defined to calculate the number of minutes
day = remaining_minutes / 1440

# prints result
print(str(minutes) + " minutes is approximately " + str(years) + " years and " + str(int(day)) + " days")

# Variables y, m & q are assigned to ask user's input for year, month and day of the month
y = int(input("Enter year: (e.g., 2008): "))
m = int(input("Enter month: 1-12: "))

# Checks to see if user input 1 or 2 for m. If true, 1 is replaced with 13 and 2 is replaced with 14. y is deducted by 1
if m == 1:
    m = 13
    y = y - 1
elif m == 2:
    m = 14
    y = y - 1

q = int(input("Enter the day of the month: 1-31: "))
j =  y // 100
k = y % 100

# calculates the day of the week
h = (q + (26 * (m + 1) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7 

# prints the result
week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print("Day of week is " + week[h])
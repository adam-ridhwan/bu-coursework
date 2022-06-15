# Location class defined
class Location:
    def __init__(self, row, column, maxValue):
        self.row = int(row)
        self.column = int(column)
        self.maxValue = float(maxValue)

# function locateLargest defined to find the location of largest value
def locateLargest(a):
    row = 0
    column = 0
    # nested for loop used to iterate through the location of largest element and overrides when a larger element is found
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] > a[row][column]:
                row = i
                column = j
    return Location(row, column, a[row][column])

# gets the input data of user and stores in variable
num = input("Enter the number of rows and columns in the list:" )
data = num.strip().split(',')
rows = int(data[0])
columns = int(data[1])

# lst is the two dimensional list   
lst = []
for i in range(rows):
    x = input("Enter row " + str(i) + ": ")
    x = x.strip().split()
    y = []
    for i in x:
        y.append(float(i))
    lst.append(y)

largestElement = locateLargest(lst)

# prints result
print("The location of the largest element is " + str(largestElement.maxValue) + " at (" + str(largestElement.row) + ", " + str(largestElement.column) + ")")




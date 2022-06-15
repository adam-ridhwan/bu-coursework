# LinearEquation defined as class with contructor and private data fields for a-f
class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = int(a)
        self.__b = int(b)
        self.__c = int(c)
        self.__d = int(d)
        self.__e = int(e)
        self.__f = int(f)

    # getters defined for private data fields a-f
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getD(self):
        return self.__d

    def getE(self):
        return self.__e
    
    def getF(self):
        return self.__f

    # isSolvable defined as methods to check if ad - bc is not zero
    def isSolvable(self):
        if (self.__a * self.__d) - (self.__b * self.__c) != 0:
            return True
    
    # getX and getY defined as methods to calculate x and y values
    def getX(self):
        return ((self.__e * self.__d) - (self.__b * self.__f)) / ((self.__a * self.__d) - (self.__b * self.__c)) 

    def getY(self):
        return ((self.__a * self.__f) - (self.__e * self.__c)) / ((self.__a * self.__d) - (self.__b * self.__c))     

#  function main() prints the values
def main():
    a = (input("Enter value for a: "))
    b = (input("Enter value for b: "))
    c = (input("Enter value for c: "))
    d = (input("Enter value for d: "))
    e = (input("Enter value for e: "))
    f = (input("Enter value for f: "))

    equation = LinearEquation(a, b, c, d, e, f)
    if equation.isSolvable() == True:
        print("\nThe value of x is", equation.getX())
        print("The value of y is", equation.getY())
    else:
        print("\nThe equation has no solution")

main()

# test case #1 
# a = 1
# b = 2
# c = 4
# d = 5
# e = 3
# f = 6

# test case #2
# a = 1
# b = 1
# c = 4
# d = 4
# e = 3
# f = 6

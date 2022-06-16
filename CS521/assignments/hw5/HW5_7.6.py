import math

# QuadraticEquation defined as class with constructor and datafields for three values: a,b,c
class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = int(a)
        self.__b = int(b)
        self.__c = int(c)

    # getA, getB, getC defined as getters
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    # mgetDiscriminant defined as method to get the discriminant
    def getDiscriminant(self):
        return (self.__b**2 - (4 * self.__a * self.__c))

    # getRoot1 and getRoot2 defined as methods to calculate both roots
    def getRoot1(self):
        return (-self.__b + math.sqrt(self.getDiscriminant())) / (2 * self.__a)
    
    def getRoot2(self):
        return (-self.__b - math.sqrt(self.getDiscriminant())) / (2 * self.__a)

# function main() prints results
def main():
    a = (input("Enter a value for a: "))
    b = (input("Enter a value for b: "))
    c = (input("Enter a value for c: "))

    equation = QuadraticEquation(a, b, c)

    if equation.getDiscriminant() == 0:
        print("\nThe one root is:", equation.getRoot1())
    elif equation.getDiscriminant() < 0:
        print("\nThe equation has no roots.")
    else:
        print("\nThe two roots are:", equation.getRoot1(), "and", equation.getRoot2())

main()

# test case 2 (dicriminant = 0)
# a = -3
# b = -6
# c = -3

# test case 3 (discriminant < 0)
# a = -1
# b = 3
# c = -3

# test case 1 (discriminant > 0)
# a = 1
# b = 5
# c = 4
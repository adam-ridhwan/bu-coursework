# Rectangle is defined as a class that includes a constructor with data fields for width and height
class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height
    
    # method getArea is defined to calculate the area of rectangle
    def getArea(self):
        return self.width * self.height

    # method getPerimeter is defined to calculate perimeter
    def getPerimeter(self):
        return self.width + self.width + self.height + self.height

# function main() defined to print the result of rectangle 1 & 2
def main():
    rectangle1 = Rectangle(4, 40)
    rectangle2 = Rectangle(3.5, 35.7)

    print("Rectangle 1:-")
    print(" Width = " + str(rectangle1.width))
    print(" Height = " + str(rectangle1.height))
    print(" Area = " + str(rectangle1.getArea()))
    print(" Perimeter = " + str(rectangle1.getPerimeter()),"\n")
    
    print("Rectangle 2:-")
    print(" Width = " + str(rectangle2.width))
    print(" Height = " + str(rectangle2.height))
    print(" Area = " + str(rectangle2.getArea()))
    print(" Perimeter = " + str(rectangle2.getPerimeter()))

main()

# variables x1, y1, x2, y2, x3, x4 is defined to ask user to input numbers
x1 = eval(input("Enter x1 for Point 1: ")) 
y1 = eval(input("Enter y1 for Point 1: ")) 
x2 = eval(input("Enter x2 for Point 1: ")) 
y2 = eval(input("Enter y2 for Point 1: ")) 
x3 = eval(input("Enter x3 for Point 1: ")) 
y3 = eval(input("Enter y3 for Point 1: ")) 

# area is defined to calculate the area of triangle using user's inputs
area = ((x1 * (y2-y3)) + (x2 * (y3-y1)) + (x3 * (y1-y2))) * 0.5

# prints result
print("The area of the triangle is " + str(round(area*-1, 1)))


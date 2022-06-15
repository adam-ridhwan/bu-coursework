# variables are assigned for x coordinate, y coordinate, width and height
x1, y1, w1, h1= map(float,input("Enter r1's center x-, y-coordinates, width, and height: ").split(","))
x2, y2, w2, h2 = map(float,input("Enter r2's center x-, y-coordinates, width, and height: ").split(","))

# if-statement checks to see if r2 is inside r1
if (((y2-y1) ** 2) ** 0.05) + h2 / 2 <= h1 / 2 and \
    (((x2-x1) ** 2) ** 0.05) + w2 / 2 <= w1 / 2 and \
        h1 / 2 + h2 / 2 <= h1 and \
            w2 / 2 + w1 / 2:
    print("r2 is inside r1")

# elif-statement checks to see if r2 overlaps r1
elif (x1 + w1 / 2 > x2 - w2) or \
    (y1 + h1 / 2 > y2 - h2):
    print("r2 overlaps r1")

# else-statement returns if if-statement and elif-statement is false
else:
    print("r2 does not overlap r1")
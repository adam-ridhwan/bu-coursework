# Variable "introduction" is created to assign the first two sentence
introduction  = "Greetings from a beginning Python programmer." + "\nDo you want to be addressed as ..."

# Variable "arrow" is created to assign arrows
arrow = ".......................................======>"

# Prints empty lines in between the variable "introduction"
print("\n" + introduction + "\n")

# Section for Jane Margeret Doe. Variables created for first name, middle name and last name. Then format() is used to assign the variables to indexes and used print() to print each line.
first_name = "Jane"
middle_name = "Margeret"
last_name = "Doe"
print("{0}{1} {2} {3}?".format(arrow, first_name, middle_name, last_name))
print("{0}{1} {2}?".format(arrow, first_name, last_name))
print("{0}Mr./Ms. {1} {2} {3}?".format(arrow, first_name, middle_name, last_name))
print("{0}Dear {1}?".format(arrow, first_name))
print("or")
print("{0}{3}, {1} {2}?".format(arrow, first_name, middle_name, last_name))
print("\n")

# Section for Archibald Montague Abercrombie. Variables created for first name, middle name and last name. Then format() is used to assign the variables to indexes and used print() to print each line.
first_name = "Archibald"
middle_name = "Montague"
last_name = "Abercrombie"
print("{0}{1} {2} {3}?".format(arrow, first_name, middle_name, last_name))
print("{0}{1} {2}?".format(arrow, first_name, last_name))
print("{0}Mr./Ms. {1} {2} {3}?".format(arrow, first_name, middle_name, last_name))
print("{0}Dear {1}?".format(arrow, first_name))
print("or")
print("{0}{3}, {1} {2}?".format(arrow, first_name, middle_name, last_name))
print("\n")

# Section for Cleopatra Anastasia Montgomery. Variables created for first name, middle name and last name. Then format() is used to assign the variables to indexes and used print() to print each line.
first_name = "Cleopatra"
middle_name = "Anastasia"
last_name = "Montgomery"
print("{0}{1} {2} {3}?".format(arrow, first_name, middle_name, last_name))
print("{0}{1} {2}?".format(arrow, first_name, last_name))
print("{0}Mr./Ms. {1} {2} {3}?".format(arrow, first_name, middle_name, last_name))
print("{0}Dear {1}?".format(arrow, first_name))
print("or")
print("{0}{3}, {1} {2}?".format(arrow, first_name, middle_name, last_name))

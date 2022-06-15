# Eliza300
# Intent: A list of helpful actions that a troubled person could take. Build 3

possible_actions = ['taking up yoga', 'sleeping eight hours a night', 'relaxing', 
        'not working on weekends', 'spending two hours a day with friends']

'''
Precondition: possible_actions is the list defined above

Postconditions:

1. (Welcome): A welcome message is on the console

2. (user_complaint): user_complaint is the user's response to
"Please describe your emotional complaint--in one punctuation-free line: "

3. (how_long): how_long is the user's string response to
"How many months (between 1 and 99) have you experienced ...?"

4. (Month validity): EITHER how_long has the requested form
OR this terminated AND "Sorry, illegal input. Eliza is quitting; run Eliza again."
is on the console

5. (Advice): EITHER how_long >= 3
OR "Please return in * months" is on the console where * is 3 - how_long

6. (actions_not_taken): actions_not_taken consists of the actions (elements) in
possible_actions that the user answered 'n' to when questioned "Have you tried..."

7. (Summarized): Eliza300 recommended that the user take the actions in
actions_not_taken
'''


# Postcondition 1 (Welcome) - prints welcome message at the start of program
print("Thank you for using Eliza300, a fun therapy program.")

# Postcondition 2 (user_complaint) - user_complaint is defined that asks the user to input a complaint
user_complaint = input("Please describe your emotional complaint--in one punctuation-free line:")

# Postcondition 3 (how_long) - how_long is defined that asks the user to input the number of months the user is experiencing the complaint
how_long = input("How many months (between 1 and 99) have you experienced ...?'" + user_complaint + "'")

# Postcondition 4 (Month validity) - checks to see if user entered a number that is between 1 and 99
if 1 <= int(how_long) <= 99: 

    # Postcondition 5 (Advice) - if-else statement checks to see if user entered a number in how_long that is either below 3 OR greater than or equal to 3. A response is then printed for each statement
    if int(how_long) < 3:
        print("Please return in " + str(3 - int(how_long)) + " months")
    else:
        print(str(how_long) + " months is significant. Sorry to hear it.")

        # Postcondition 6 (actions_not_taken) - actions_not_taken is defined to store possble_actions. A for-loop is used to loop through possible_actions that asks user to answer 'y' and 'n'. Results for 'n' is added into actions_not_taken
        actions_not_taken = []
        for i in possible_actions:
            question = input("Have you tried..." + i + "? Please answer y or n:") 
            if question == 'n':
                actions_not_taken.append(i) 
            
        # Postcondition 7 (Summarized) - prints Eliza300's advice. A for-loop is used to loop through actions_not_taken and prints each result in new line
        print("After careful analysis:), here is Eliza300's advice:")
        for i in actions_not_taken:
            print(i)

else:
    print("Sorry, illegal input. Eliza is quitting; run Eliza again.")

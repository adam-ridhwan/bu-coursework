# Post 1 (Welcome) prints welcome message
print("Thank you for using Eliza300, a fun therapy program.")

# Post 2 (Complaint) AND user_complaint is defined as the complaint 
# entered by the user in response to a prompt
user_complaint = input("Please state your emotional complaint:")

# Post 3 (Duration) how_long is defined as the number of months user has experienced complaint
how_long = input("How many months has it been that have you experienced '" + user_complaint + "'?")

# Post 5 (Action Recommended) Checks to see if user entered an integer the exceeds 2 OR less than and equal to 2
if int(how_long) > 2:
    # Post 4 (Error Check) Checks to see if user entered an integer between 1 and 100. Program quits if user enters an integer over 100 twice.
    if int(how_long) > 2 and int(how_long) < 100:
        print(how_long + " months if too much time to go without help! Let's schedule a few sessions.")
    elif int(how_long) > 100:
        new_input = input("Please try one more time to enter duration in months less than 100")   
        if int(new_input) <= 2: 
            print("Come back in a couple of months if this persists.")  
        elif int(new_input) > 2 and int(new_input) < 100:
            print(new_input + " months if too much time to go without help! Let's schedule a few sessions.")
        else:
            print("Sorry, try running Eliza again")
            import sys
            sys.exit()
elif int(how_long) <= 2: 
    print("Come back in a couple of months if this persists.") 
            
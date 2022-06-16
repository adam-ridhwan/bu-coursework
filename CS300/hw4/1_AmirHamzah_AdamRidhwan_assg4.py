# Build 1 

# A list of key words for depression 
key_words = ['depress', 'sad', 'down']

'''
Postconditions
1 (Welcome): A welcome message is on the console  
2 (user_complaint): user_complaint is the user's response in reply to "Please state your complaint:"
3 (observed_complaint_type): observed_complaint_type = get_complaint_type(user_complaint)
2 (Advice displayed): EITHER "You have depression" OR nothing is displayed according to observed_complaint_type
'''

def get_complaint_type(user_complaint):
    '''
    Precondition: user_complaint is a string 

    Postcondition:
    EITHER user_complaint contains one of key_words
         AND observed_complaint_type is the set consisting of "Depression"
    OR observed_complaint_type is the empty set

    Returns: observed_complaint_type 
    '''
    target = set()
    for i in key_words:
        if i.lower() in user_complaint.lower():
            target.add("Depression")
    return target


# (Welcome): Postcondition 1
print("Thank you for using Eliza300, a fun therapy program.")

# (user_complaint): Postcondition 2
print("Please state your complaint:")
user_complaint = input()

# (observed_complaint_type): Postcondition 3
observed_complaint_type = get_complaint_type(user_complaint)

# (Advice displayed): Postcondition 4
if len(observed_complaint_type) > 0:
    print("You have depression")



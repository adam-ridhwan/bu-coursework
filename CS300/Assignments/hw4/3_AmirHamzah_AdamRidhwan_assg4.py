# Build 3

'''
Postconditions
1 (Welcome): A welcome message is on the console  
2 (user_complaint): user_complaint is the user's response in reply to "Please state your complaint:"
3 (observed_complaint_types): observed_complaint_types = get_complaint_type(user_complaint)
4 (Remedies displayed): the remedies in advice_per_type corresponding to
observed_complaint_types are on the monitor, one line for each.
'''

# A list of types of emotional complaints and corresponding key words for each 
complaint_type = ['Depression', 'Human Relations', 'Substance Abuse']
key_words = [['depress', 'sad', 'down'],
             ['conflict', 'argument', 'mistreat', 'quarrel'],
             ['drug', 'alcohol', 'drink', 'cocaine', 'opioid', 'heroin']]
advice_per_type = [
    ['Get out more.', 'Take up a hobby that you love.'],
    ["Don't expect too much of people.", "Don't take offence easily."],
    ['Get counseling.', "Don't delay action on counseling."]]

def get_complaint_type(user_complaint):
    '''
    Precondition: 
    1. a_user_complaint is a string
    2. complaint_type is a list of strings
    3. key_words is a list of lists of strings
    3. complaint_type and key_words are the same length
    '''
    target = set()
    for i in range(len(complaint_type)):
        for j in key_words[i]:
            if j.lower() in user_complaint.lower():
                target.add(i)
    return target
            
# (Welcome): Postcondition 1
print("Thank you for using Eliza300, a fun therapy program.")

# (user_complaint): Postcondition 2
print("Please state your complaint:")
user_complaint = input()

# (observed_complaint_type): Postcondition 3
observed_complaint_types = get_complaint_type(user_complaint)

# (Remedies displayed): Postcondition 4
if len(observed_complaint_types) > 0:
    for i in list(observed_complaint_types):
        for j in advice_per_type[i]:
            print(j)



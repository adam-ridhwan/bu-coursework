from eliza300_5_functions_1 import get_complaint_type

advice_per_type = [
    ['Get out more.', 'Take up a hobby that you love.'],
    ["Don't expect too much of people.", "Don't take offence easily."],
    ['Get counseling.', "Don't delay action on counseling."]]

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
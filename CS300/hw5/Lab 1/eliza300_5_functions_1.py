complaint_type = ['Depression', 'Human Relations', 'Substance Abuse']
key_words = [['depress', 'sad', 'down'],
             ['conflict', 'argument', 'mistreat', 'quarrel'],
             ['drug', 'alcohol', 'drink', 'cocaine', 'opioid', 'heroin']]

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
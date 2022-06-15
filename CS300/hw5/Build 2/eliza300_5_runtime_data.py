complaint_types = []
key_words = []


def read_complaint_data():
    '''
    Intent: Get complaint_types and key_words from local ElizaData.txt

    Precondition =========

    ElizaData.txt is a local file consisting of paragraphs of the form

    On first line: 'Key Words for '<phrase describing a complaint category>
    On second line: <words, separated by blanks, that may occur within a
    description of the corresponding category>

    Example of ElizaData.txt:

    Key Words for Depression
    depress sad

    Key Words for Human Relations
    conflict argument mistreat

    Postconditions =========

    (1) complaint_types = list of the phrases in ElizaData.txt describing all
    complaint categories
    {2) key_words = list of lists of words in ElizaData.txt that may occur
    within phrases that describe the corresponding complaint category

    '''

    global complaint_types, key_words

    # --(data_source): data_source represents 'ElizaData.txt' (local file) within the program
    
    #    AND data_source (which is like a cursor) is at the beginning of the first unread line

    # --(Postconditions for all read): Post(1) and Post(2) are valid for the data read so far

    # --(line_read): line_read = contents of most recently read line from data_source 

    try:
        data_source = open("ElizaData.txt", 'r')    
    except: 
        print("Could not open ElizaData.txt") 

    complaint_types, key_words = [], []

    line_read = "\n"

    while line_read.endswith('\n'):
        line_read = data_source.readline()
        if line_read.startswith('Key Words'):
            complaint_types.append(line_read[14:-1])
        elif line_read == '\n':
            pass
        elif line_read == '':
            pass
        else:
            list_1 = line_read.split(' ')
            list_2 = []
            for i in list_1:
                if i.endswith('\n'):
                    list_2.append(i[:-1])
                else: 
                    list_2.append(i)
            key_words.append(list_2)

            
read_complaint_data()  


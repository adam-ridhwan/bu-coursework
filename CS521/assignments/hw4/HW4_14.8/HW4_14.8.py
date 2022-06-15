# checks to see is user opens file in correct directory
try:
    dataSource = open("lorem.txt", "r")
except:
    print("Could not open text file")
    exit()

lineRead = "\n"

# while loop used to read line by line and splits each word with a comma
nonDuplicates = []
while lineRead.endswith("\n"):
    lineRead = dataSource.read()
    words = lineRead.split()

    # removes symbols
    wordsLowered = []
    for word in words:
        word = word.strip("?,.!/;:()")
        wordsLowered.append(word.lower())

    # removes duplicates
    for word in wordsLowered:
        if wordsLowered.count(word) == 1:
            nonDuplicates.append(word)

# prints non-duplicate words
for word in sorted(nonDuplicates):
    print(word)

    

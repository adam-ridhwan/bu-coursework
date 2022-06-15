'''
Message for TA: i am getting different results on both VScode and python IDLE. But the correct output format should show on VScode. 
i am not sure why python IDLE is not producing the correct output layout on my end.
'''

trials = 4000
primeNumberList = []
reversedNumberList = []
reversedPrimeNumberList = []

# for-loop used to append prime numbers to variable primeNumberList
for num in range(2, trials + 1):
   if num > 12:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           primeNumberList.append(num)

# for-loop used to append the reverse version of primeNumberList
for i in primeNumberList:
    reversedNumberList.append(int(str(i)[::-1]))

# for-loop used to append prime numbers to reversedPrimeNumberList
for num in reversedNumberList:
   if num > 12:
       for i in range(2, num):
           if (num % i) == 0:
            break
       else:
           reversedPrimeNumberList.append(num)

# creates a dictionary of primeNumberList and reversedNumberList
numDictionary = dict(zip(primeNumberList, reversedNumberList))

joinedList = primeNumberList + reversedPrimeNumberList

# checks for duplicates. appends values to emirp list
emirp = []    
for key,value in numDictionary.items():
    if key == value:
        pass
    elif key and value in joinedList:
        emirp.append(key)
        emirp.append(value)

# adds a value to start of list
finalEmirp = sorted(set(emirp))
a = 0
finalEmirp = [a] + finalEmirp

# prints result
i = 1
while i != 101:
    print('{0:>4}'.format(finalEmirp[i]), end='  ')
    if i % 10 == 0:
        print()
    i += 1
    

# sends string to helper
def displayPermutation(s):
    return displayPermutationHelper("", s)

def displayPermutationHelper(s1, s2):
    # checks to see if len of s2 is 0 and prints if true
    if len(s2) == 0:
        print(s1)
    # recursion
    for i in s2:
        new_str = s1 + i 
        index = s2.index(i)
        new_remaining = s2[0:index] + s2[index+1::]
        displayPermutationHelper(new_str, new_remaining)

displayPermutation(input("Enter a string: "))
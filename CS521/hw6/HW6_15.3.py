def gcd(m, n):
    # checks to see if n is 0 and returns m if true
    if (n == 0):
        return m
    else:
        # recursion
        return gcd(n, m % n)

# variable m & n stores user's inputs
m = int(input("Enter 1st number: ")) 
n = int(input("Enter 2nd number: "))

# print result
print("The greatest common divisor is ", gcd(m, n))
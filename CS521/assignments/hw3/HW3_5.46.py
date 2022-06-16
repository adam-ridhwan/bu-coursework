# variable sum is defined to store the sum of 10 numbers 
sum = 0

# variable sumDevi is defined to store the squared values
sumDevi = 0

print("enter ten numbers: ", end = "")

# for-loop is used to loop 10 times to get user's input for each number
for i in range (0,10):
    x = eval(input())
    sum += x
    sumDevi += x**2

# calculations for mean and deviation
mean = sum/10
deviation = ((sumDevi - ((sum)**2/10))/9)**0.5

print("The mean is", format(mean, ".2f"))
print("The standard deviation is", format(deviation, ".2f")) 
# function defined to get approximation of pi
def approximationPi(rank):
    value = 0
    for i in range(1, 2 * rank + 1, 2):
        num = -(i % 4 - 2)
        value += float(num) / i
    return 4 * value

# prints the first row
print("i\t\tm(i)")
print()

# prints table
counter = 1
for i in range(1, 902, 100):
    answer = approximationPi(i)
    print(counter, end="\t\t")
    print("{:.4f}".format(answer))
    counter += 100
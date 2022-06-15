import random

# variable trials is number of trials
trials = 1000000

# variable hits is a counter
hits = 0 

# for loop is used to loop through number of times 
for i in range(trials):
    x = random.random() * 2.0 - 1
    y = random.random() * 2.0 - 1
    if x < 0:
        hits += 1
    elif not (x > 1 or x < 0 or y > 1 or y < 0):
        slope = (1.0 - 0) / (0 - 1.0)
        x1 = x + -y * slope
        if x1 <= 1:
            hits += 1 

result = hits/ trials
print(result)
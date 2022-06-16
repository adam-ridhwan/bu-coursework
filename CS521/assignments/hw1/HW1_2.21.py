# balance is defined to ask user to input a number
balance = input("Enter the monthly saving amount: ")

# balance is calculated and overriden each line
balance = int(balance) * (1 + 0.00417)
balance = (100 + round(balance, 3)) * (1 + 0.00417) 
balance = (100 + round(balance, 3)) * (1 + 0.00417)  
balance = (100 + round(balance, 3)) * (1 + 0.00417)  
balance = (100 + round(balance, 3)) * (1 + 0.00417)  
balance = (100 + round(balance, 3)) * (1 + 0.00417)

# prints result
print("After the sixth month, the account value is " + (str(balance)[:6]))


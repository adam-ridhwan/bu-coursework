# Account defined as class with constructor with private data fields for id, balance and annual interest rate
class Account:
    def __init__(self, id = 0, balance = 100.0, annualInterestRate = 0.0):
        self.__id = int(id)
        self.__balance = float(balance)
        self.__annualInterestRate = float(annualInterestRate)
    
    # getId, getBalance, getannualInterestRate defined as getters
    def getId(self):
        return self.__id
    
    def getBalance(self):
        return self.__balance

    def getannualInterestRate(self):
        return self.__annualInterestRate 

    # setId, setBalance, setAnnualInterestRate defined as setters
    def setId(self, id):
        self.__id = int(id)

    def setBalance(self, balance):
        self.__balance = float(balance)

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = float(annualInterestRate)

    # getMonthlyInterestRate, getMonthlyInterest defined to calculate the interest 
    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate / 100) / 12
    
    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()
    
    # withdraw and deposit defined to adjust the amount of balance
    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount


def main():
   # List of accounts stored 
    accounts = []
  
   # for loop used to create accounts from id 1-10
    for i in range(0, 10):
       account = Account(i, 100.0)
       accounts.append(account)
    
   # while loop used to check if user enter correct id
    while True:
        id = int(input("\nEnter an account id: "))
        
        # checks to see if user input for id is from 1-9
        while id < 0 or id > 9:
            id = int(input("\nInvalid Id.. Re-enter: "))

        # while loop used to provide options
        while True:
            print("\nMain menu\n1: view balance \n2: withdraw \n3: deposit \n4: exit ")
            
            # asks user to enter a choice from options
            choice = int(input("\nEnter a choice: "))
            
            # for loop used to check for id
            for acc in accounts:
                if acc.getId() == id:
                    userAccount = acc
                    break
            
            # checks the balance if choice is 1
            if choice == 1:
                print("The balance is:", userAccount.getBalance())
                
            # withdraw amount is choice is 2    
            elif choice == 2:
                amount = float(input("Enter an amount to withdraw: "))
                userAccount.withdraw(amount)
                
            # deposts amount if choice is 3
            elif choice == 3:
                amount = float(input("Enter an amount to deposit: "))
                userAccount.deposit(amount)

            # exits game
            else:
                break
          
# print function     
main()

        

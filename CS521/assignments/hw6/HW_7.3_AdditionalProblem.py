# Account defined as class with constructor with private data fields for id, balance and annual interest rate

class Account:
    def __init__(self, id = 0, balance = 100.0, annualInterestRate = 0.0):
        self.__id = int(id)
        self.__balance = float(balance)
        if annualInterestRate > 0:
            self.__annualInterestRate = float(annualInterestRate)
        else:
            raise ValueError("Annual interest must be postive")
    
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
        if amount < 0:
            raise ValueError("Withdraw amount must be positive")
        else:
            self.__balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        else:
            self.__balance += amount

# function main() prints result
def main():
    account1 = Account(1122, 20000.00, -4.5)
    account1.withdraw(-2500.00)
    account1.deposit(-3000.00)

main()


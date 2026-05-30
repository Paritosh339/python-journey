class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, balance):
        self.balance += balance
        print("Deposit", balance , "Balance: " , self.check_balance())
    
    def withdraw(self, amount):
     if amount > self.balance:  
        print("Insufficient funds!")
     else:
        self.balance -= amount
        print("Withdraw", amount, "Balance: ", self.check_balance())
    
    def check_balance(self):
        return self.balance

account1 = BankAccount("Paritosh", 1000)
print(f"Account Owner: ", account1.name)
print(f"Balance: ", account1.balance)

account1.deposit(500)
account1.withdraw(200)



        
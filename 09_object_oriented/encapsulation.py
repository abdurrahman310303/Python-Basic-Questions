class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance
    
    def get_account_info(self):
        return f"Account: {self.__account_number}, Balance: ${self.__balance}"

account = BankAccount("12345", 1000)
print(account.get_account_info())
account.deposit(500)
print(account.get_balance())
account.withdraw(200)
print(account.get_account_info())

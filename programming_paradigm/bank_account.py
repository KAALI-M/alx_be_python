class BankAccount:
    def __init__(self,account_balance=0 ):
        self.account_balance=account_balance
    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount}")
    def withdraw(self, amount):
        if self.account_balance >= amount :
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
            return True
        else:
            print (f"Insufficient funds.")
            return False
    def display_balance(self):
        print("Current Balance: ${elf.account_balance}")

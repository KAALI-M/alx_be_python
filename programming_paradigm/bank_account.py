class BankAccount:
<<<<<<< HEAD
    def __init__(self,account_balance=0 ):
        self.account_balance=account_balance
=======
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

>>>>>>> 3da765e6bb91691ba437d831fa027122a501afe4
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
<<<<<<< HEAD
        print("Current Balance: ${elf.account_balance}")
=======
        print(f"Current Balance: ${self.__account_balance:.2f}")

    def get_balance(self):
        return self.__account_balance
>>>>>>> 3da765e6bb91691ba437d831fa027122a501afe4

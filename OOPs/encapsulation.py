class BankAccount:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance

    def deposit(self, amount):
        if amount > 0:
            self._balance+=amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount>self._balance:
            print("Insufficient funds!")
        else:
            self._balance-=amount

    def get_balance(self):
        return self._balance
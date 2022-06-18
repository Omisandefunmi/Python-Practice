class Account:
    def __init__(self, name, pin):
        self.balance = 0
        self.name = name
        self._pin = pin

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount, pin):
        if self._pin == pin:
            if amount < self.balance:
                self.balance -= amount
            else:
                raise ValueError("Amount cannot be greater than balance")
        else:
            raise AssertionError("Pin mismatch")

    def transfer(self, amount, account, sender_pin):
        pass


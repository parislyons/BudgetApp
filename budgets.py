class Budget():
    _amount = None

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Remaining balance: {self.amount}"

    def deposit(self, amount):
        self.amount += amount
        return amount

    def withdraw(self, amount):
        self.amount -= amount
        return amount

    def reallocate(self, amount, to, from_):
        self.amount = amount
        self.to = to
        self.from_ = from_

class Food(Budget):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

class Clothing(Budget):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

class Entertainment(Budget):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount




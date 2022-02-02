class Budget():
    _amount = None

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Remaining {self.name} budget: £{self.amount}"

    def deposit(self, amount):
        self.amount += amount
        return amount

    def withdraw(self, amount):
        self.amount -= amount
        return amount

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

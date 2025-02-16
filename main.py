class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, another):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {another.name}")
            another.deposit(amount, f"Transfer from {self.name}")
            self.ledger.append({'amount': -amount, 'description': f"Transfer to {another.name}"})
            another.ledger.append({'amount': amount, 'description': f"Transfer from {self.name}"})
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        result = f"{self.name:*^30}\n"
        for item in self.ledger:
            result += f"{item['description'][:23]:<23}{item['amount']:7.2f}\n"
        result += f"Total: {self.get_balance():7.2f}"
        return result


def create_spend_chart(categories):
    pass

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)



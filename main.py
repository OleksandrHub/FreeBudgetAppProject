class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = "".join(f"{item['description'][:23]:23}{item['amount']:>7.2f}\n" for item in self.ledger)
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    spends = [sum(-item["amount"] for item in cat.ledger if item["amount"] < 0) for cat in categories]
    total_spent = sum(spends)

    percentages = [(spend / total_spent) * 100 // 10 * 10 for spend in spends]

    for percent in range(100, -1, -10):
        chart += f"{percent:>3}| "
        for p in percentages:
            chart += "o  " if p >= percent else "   "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"

    max_len = max(len(cat.name) for cat in categories)

    names = [cat.name.ljust(max_len) for cat in categories]
    for i in range(max_len):
        chart += "     " + "  ".join(name[i] for name in names) + "  \n"

    return chart.rstrip("\n") 

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(1000, "deposit")
food.withdraw(100, "groceries")

entertainment.deposit(500, "deposit")
entertainment.withdraw(200, "movies")

business.deposit(300, "deposit")
business.withdraw(50, "supplies")

chart = create_spend_chart([food, entertainment, business])
print(chart)

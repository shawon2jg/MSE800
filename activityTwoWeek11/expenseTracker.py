class Expense:
    # Represents a single expense entry
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

class ExpenseTracker:
    # Tracks multiple expenses and calculates total spending
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        #Add a new expense with description and amount
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        expense = Expense(description, amount)
        self.expenses.append(expense)
        return expense

    def calculate_total(self):
        #Calculate and return the total of all expenses
        return sum(expense.amount for expense in self.expenses)

# Example usage
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense("Groceries", 50)
    tracker.add_expense("Transport", 20)
    print("Total Expenses: $", tracker.calculate_total())

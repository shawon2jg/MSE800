import unittest
from expenseTracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        # Create a new ExpenseTracker instance before each test
        self.tracker = ExpenseTracker()

    def test_add_expense(self):
        # Test if expense is added correctly
        self.tracker.add_expense("Lunch", 15)
        self.assertEqual(len(self.tracker.expenses), 1)
        self.assertEqual(self.tracker.expenses[0].description, "Lunch")
        self.assertEqual(self.tracker.expenses[0].amount, 15)

    def test_calculate_total(self):
        # Test total calculation of all expenses
        self.tracker.add_expense("Coffee", 5)
        self.tracker.add_expense("Book", 25)
        self.assertEqual(self.tracker.calculate_total(), 30)

    def test_negative_amount(self):
        # Test that negative amounts are not allowed
        with self.assertRaises(ValueError):
            self.tracker.add_expense("Invalid", -10)

if __name__ == "__main__":
    unittest.main()

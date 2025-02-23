from .expense import Expense

class ExpenseDB:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
    
    def remove_expense(self, expense_id):
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]
    
    def get_expense_by_id(self, expense_id):
        return [expense for expense in self.expenses if expense.id == expense_id]
    
    def get_expense_by_title(self, expense_title):
        return [expense for expense in self.expenses if expense.title.tolower() == expense_title.tolower()]
    
    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]


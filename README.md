# Expense Tracker 🏦  

A simple Python-based **Expense Tracker** that allows users to **add, update, remove, and retrieve expenses**.  
The project uses **Object-Oriented Programming (OOP)** principles and **UUIDs** for unique expense identification.

---

## 🚀 Features  
✅ **Create Expenses** – Add new financial expenses  
✅ **Retrieve Expenses** – Get expenses by ID or title  
✅ **Update Expenses** – Modify title or amount of an expense  
✅ **Delete Expenses** – Remove an expense from the database  
✅ **Store Data in Memory** – Uses Python lists or dictionaries for storage  
✅ **Timestamps** – Track creation and modification times  

---

## 🛠️ Installation  

### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/YOUR_USERNAME/expense-tracker.git
cd expense-tracker


---

### **🔹 How to Use the Module**
Once you've created the package, you can use it in **another script** like this:

```python
from expense_tracker import Expense, ExpenseDB

# Initialize the expense database
db = ExpenseDB()

# Add a new expense
expense = Expense("Coffee", 5.50)
db.add_expense(expense)

# Fetch all expenses
print(db.to_dict())
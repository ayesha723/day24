expenses=[]

def add_expense(amount , category):
    expenses.append({'amount' : amount , 'category' : category})


def display_summary():

    summary={}
    for expense in expenses:
        category = expense['category']
        amount =   expense['amount']
        summary[category]=summary.get(category, 0 )+amount

    print("Expense Summary:")

    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")

add_expense(50, "Groceries")
add_expense(20, "Transport")
add_expense(30, "education")
add_expense(10, "Entertain")

# Display the summary
display_summary()
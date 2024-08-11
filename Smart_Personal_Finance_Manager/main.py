def get_income():
    income = float(input("Enter your total monthly income: $"))
    return income

def get_expenses():
    expenses = {}
    num_expenses = int(input("Enter the number of expense categories: "))
    for _ in range(num_expenses):
        category = input("Enter expense category: ")
        amount = float(input(f"Enter monthly expense for {category}: $"))
        expenses[category] = amount
    return expenses

import matplotlib.pyplot as plt

def analyze_finances(income, expenses):
    total_expenses = sum(expenses.values())
    savings = income - total_expenses
    return total_expenses, savings

def generate_visualizations(income, expenses):
    labels = list(expenses.keys())
    amounts = list(expenses.values())

    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Expense Breakdown')
    plt.axis('equal')
    plt.show()

def budget_suggestions(total_expenses, savings):
    if savings < 0:
        print("Uh-oh! You're spending more than you're earning. Consider reducing expenses.")
    elif savings == 0:
        print("You're breaking even. Look for areas to optimize spending.")
    else:
        print("Great job! You're saving money each month. Consider investing or increasing savings.")

def main():
    print("Welcome to the Personal Finance Manager!")

    income = get_income()
    expenses = get_expenses()

    total_expenses, savings = analyze_finances(income, expenses)

    print("\nAnalysis Results:")
    print(f"Total Monthly Income: ${income:.2f}")
    print(f"Total Monthly Expenses: ${total_expenses:.2f}")
    print(f"Monthly Savings: ${savings:.2f}")

    generate_visualizations(income, expenses)

    print("\nBudgeting Suggestions:")
    budget_suggestions(total_expenses, savings)

if __name__ == "__main__":
    main()

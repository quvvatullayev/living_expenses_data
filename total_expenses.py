import json
# Calculate the total expenses

def total_expenses(monthly_expenses: dict) -> int:
    """
    Calculate the total expenses
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        total_expenses: total expenses
    """
    sum = 0
    for i in monthly_expenses.values():
        sum += i
    return sum

print(total_expenses(json.loads(open('data.json').read())))
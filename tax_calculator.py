# Indian Income Tax Calculator
def taxable_income(income):
    if income < 0:
        raise ValueError("Income cannot be negative")
    return income

def tax(income):
    income = taxable_income(income)
    slabs = [
        (400000, 0.00),
        (800000, 0.05),
        (1200000, 0.10),
        (1600000, 0.15),
        (2000000, 0.20),
        (2400000, 0.25),
        (float('inf'), 0.30)
    ]
    tax_amount = 0
    previous_limit = 0
    for limit, rate in slabs:
        taxable = min(income, limit) - previous_limit
        if taxable > 0:
            tax_amount += taxable * rate
        previous_limit = limit
        if income <= limit:
            break
    return tax_amount
def net_income(income):
    income = taxable_income(income)
    return income - tax(income)
# Main program
if __name__ == "__main__":
    print("===== INDIAN TAX CALCULATOR =====")
    income = float(input("Enter your annual income: ₹"))
    total_tax = tax(income)
    remaining_income = net_income(income)
    print("\n----- TAX SUMMARY -----")
    print("Annual Income: ₹", income)
    print("Tax Amount: ₹", total_tax)
    print("Net Income: ₹", remaining_income)

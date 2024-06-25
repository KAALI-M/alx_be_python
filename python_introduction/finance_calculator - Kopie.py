monthly_income = input("Enter your monthly income: ")
total_expenses = input ("Enter your total monthly expenses: ")
monthly_income = float(monthly_income)
total_expenses = float(total_expenses)
monthly_savings = monthly_income - total_expenses
Projected_Savings = monthly_savings*12 + (monthly_savings*12*0.05)
print("Your monthly savings are $",monthly_savings)
print ("Projected savings after one year, with interest, is: $",Projected_Savings)


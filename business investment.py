# Compound Interest Calculator
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time_years = float(input("Enter the time in years: "))
compound_per_year = int(input("Enter number of times interest compounded per year: "))
rate_decimal = rate / 100
#... A = P * (1 + r/n)^(n*t)
total_amount = principal * (1 + rate_decimal/compound_per_year) ** (compound_per_year * time_years)
total_interest = total_amount - principal
monthly_interest = total_interest / (time_years * 12)
# Loan Repayment / EMI Calculator
loan_amount = float(input("Enter the loan amount: "))
annual_interest = float(input("Enter annual interest rate (in %): "))
loan_period_years = float(input("Enter loan period in years: "))
monthly_interest_rate = annual_interest / (12 * 100)  # r = R/12/100
total_months = int(loan_period_years * 12)  # n = t*12
# .....EMI = [P * r * (1+r)^n] / [(1+r)^n – 1]
emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_months) / \
      ((1 + monthly_interest_rate) ** total_months - 1)
total_payment = emi * total_months
# Simple Savings Calculator (No Interest)
monthly_saving = float(input("Enter your monthly saving amount: "))
saving_period_years = float(input("Enter saving period in years: "))
total_months = int(saving_period_years * 12)
total_savings = monthly_saving * total_months
print("\n--- Simple Savings Calculator ---")
print(f"Monthly Saving: ${monthly_saving:.2f}")
print(f"Total Months: {total_months}")
print(f"Total Savings after {saving_period_years} years: ${total_savings:.2f}")
#level_1
name=input()
emp_id=int(input())
try:
        basic_salary = float(input("Enter Basic Monthly Salary (INR): "))
        special_allowances = float(input("Enter Special Allowances (Monthly, INR): "))
        bonus_percentage = float(input("Enter Annual Bonus Percentage ( of Gross Salary): "))
except:
    print("Invalid input. Please enter numeric values for salary components.")
        
gross_monthly_salary = basic_salary + special_allowances

annual_bonus = (gross_monthly_salary * 12) * (bonus_percentage / 100)

annual_gross_salary = (gross_monthly_salary * 12) + annual_bonus

print(f"Employee Name      : {name}")
print(f"Employee ID        : {emp_id}")
print(f"Gross Monthly Salary : {gross_monthly_salary:,.2f}")
print(f"Annual Gross Salary  : {annual_gross_salary:,.2f}")

#level_2
standard_deduction=50000
taxable_income=annual_gross_salary-standard_deduction

print(f"Gross Monthly Salary   : {gross_monthly_salary:,.2f}")
print(f"standard_deduction    : {standard_deduction:,.2f}")
print(f"taxable_income    : {taxable_income:,.2f}")
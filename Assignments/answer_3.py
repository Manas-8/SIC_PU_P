# Farmers problem
def farmer_sales():
    # Land details
    total_acres = 80
    segment_acres = total_acres / 5  # 16 acres per segment
    
    # Crop data: [name, yield (tonne/acre), price, is_chemical_free_after_11_months]
    crops = [
        ["Tomatoes", (0.3*10 + 0.7*12), 7, True],  # 30% @ 10t, 70% @ 12t → avg 11.4t
        ["Potatoes", 10, 20, True],
        ["Cabbage", 14, 24, True],
        ["Sunflower", 0.7, 200, False],  # Not chemical-free in 11 months
        ["Sugarcane", 45, 4000, False]   # Not chemical-free in 11 months
    ]
    
    total_sales = 0
    chemical_free_sales = 0
    
    for name, yield_per_acre, price, is_chemical_free in crops:
        if name == "Tomatoes" or name == "Sugarcane":
            # Tomatoes: yield is already calculated as weighted average
            # Sugarcane: price is per tonne (no kg conversion needed)
            revenue = segment_acres * yield_per_acre * price * (1000 if name != "Sugarcane" else 1)
        else:
            # Other crops: convert tonnes to kg (×1000)
            revenue = segment_acres * yield_per_acre * price * 1000
        
        total_sales += revenue
        if is_chemical_free:
            chemical_free_sales += revenue
    
    print(f"Total sales from 80 acres: ₹{total_sales:,.2f}")
    print(f"Chemical-free sales after 11 months: ₹{chemical_free_sales:,.2f}")

farmer_sales()

# Find smallest of 3 distinct numbers
number_1=int(input("Enter first number: "))
number_2=int(input("Enter second number: "))
number_3=int(input("Enter third number: "))
if number_1<number_2 and number_1<number_3:
    print(f"The smallest number is {number_1}")
elif number_2<number_1 and number_2<number_3:
    print(f"The smallest number is {number_2}")
else:
    print(f"The smallest number is {number_3}")
	

# perect square or not
square=int(input("Enter the number to be checked: "))
if(square ** 0.5 % 1 == 0):
    print(f"{square} is a perfect square")
else:
    print(f"{square} is not a perfect square")


# leap year or not
year=int(input("Enter the year: "))
if ((year % 4 == 0 and year % 100 !=0) or year % 400 ==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")




# taxation problem
#level_1
def tax_calculator():
    print("\nGlobalNext Solutions - Employee Tax Calculator\n")
    print("Please enter employee details:")
    
    # Input validation functions
    def is_valid_name(name):
        return name and len(name) <= 50 and name.replace(" ", "").isalpha()
    
    def is_valid_empid(empid):
        return 5 <= len(empid) <= 10 and empid.isalnum()
    
    def is_valid_salary(value):
        return value.replace('.', '', 1).isdigit() and float(value) >= 0
    
    def is_valid_bonus(value):
        return value.replace('.', '', 1).isdigit() and 0 <= float(value) <= 100
    
    # Get employee details with validation
    while True:
        name = input("Employee Name: ")
        if is_valid_name(name):
            break
        print("Invalid name. Must contain only alphabets and spaces (max 50 chars).")
    
    while True:
        empid = input("Employee ID: ")
        if is_valid_empid(empid):
            break
        print("Invalid ID. Must be 5-10 alphanumeric characters.")
    
    while True:
        basic = input("Basic Monthly Salary (₹): ")
        if is_valid_salary(basic):
            basic = float(basic)
            break
        print("Invalid salary. Must be a positive number.")
    
    while True:
        allowances = input("Special Allowances (₹): ")
        if is_valid_salary(allowances):
            allowances = float(allowances)
            break
        print("Invalid amount. Must be a non-negative number.")
    
    while True:
        bonus_pct = input("Bonus Percentage (0-100): ")
        if is_valid_bonus(bonus_pct):
            bonus_pct = float(bonus_pct)
            break
        print("Invalid percentage. Must be between 0 and 100.")
    
    # Level 1: Salary Calculations
    gross_monthly = basic + allowances
    annual_bonus = (gross_monthly * 12) * (bonus_pct / 100)
    annual_gross = (gross_monthly * 12) + annual_bonus
    
    # Level 2: Taxable Income
    standard_deduction = 50000
    taxable_income = max(annual_gross - standard_deduction, 0)
    
    # Level 3: Tax Calculation
    tax = 0
    remaining_income = taxable_income
    
    slabs = [
        (300000, 0.00),
        (300000, 0.05),
        (300000, 0.10),
        (300000, 0.15),
        (300000, 0.20),
        (float('inf'), 0.30)
    ]
    
    for slab_amount, rate in slabs:
        if remaining_income <= 0:
            break
        taxable = min(remaining_income, slab_amount)
        tax += taxable * rate
        remaining_income -= slab_amount
    
    # Apply rebate if applicable
    if taxable_income <= 700000:
        tax = 0
    
    # Add cess
    cess = tax * 0.04
    total_tax = tax + cess
    
    # Level 4: Net Salary
    net_salary = annual_gross - total_tax
    
    # Level 5: Report Generation
    print("\n" + "="*50)
    print("EMPLOYEE TAX REPORT".center(50))
    print("="*50)
    print(f"Employee Name: {name}")
    print(f"Employee ID: {empid}")
    print("-"*50)
    print(f"Gross Monthly Salary: ₹{gross_monthly:,.2f}")
    print(f"Annual Gross Salary: ₹{annual_gross:,.2f}")
    print(f"Standard Deduction: ₹{standard_deduction:,.2f}")
    print(f"Taxable Income: ₹{taxable_income:,.2f}")
    print("-"*50)
    print("TAX DETAILS:")
    print(f"Income Tax: ₹{tax:,.2f}")
    print(f"Health & Education Cess (4%): ₹{cess:,.2f}")
    print(f"Total Tax Payable: ₹{total_tax:,.2f}")
    print("-"*50)
    print(f"ANNUAL NET SALARY: ₹{net_salary:,.2f}")
    print("="*50 + "\n")

# Run the tax calculator
tax_calculator()

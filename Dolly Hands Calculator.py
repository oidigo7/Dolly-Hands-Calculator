'''
Dolly Hands Compensation Calculator
by Obi Idigo
'''

'''Designed to calculate how much I take home from a dolly after subtracting 
tax, fuel, and vehicle maintenance costs.'''


# Collect total price, duration, and distance to Dolly location from user.

Price = float(input("Please enter the listed price of the Dolly Request: $"))

Distance = float(input("Please enter the mapped distance from your current location to the Dolly: "))

Duration = int(input("Please enter the duration of the Dolly: "))


# Calculate mileage expense base on inputted distance and US standard mileage rate of $0.545 / mile.

TAX_RATE = .20 # Constant please don't change while script is running.

DOLLY_COMMISSION = .30 # Already withheld from total price. Constant please don't change while script is running.

MILEAGE_RATE = .58 # Constant please don't change while script is running.

INSURANCE_RATE = .113 # Constant please don't change while script is running.

Mileage_expense = Distance * MILEAGE_RATE


# Calculate tax and insurance expense.

Tax_expense = Price * TAX_RATE

Insurance_expense = Distance * INSURANCE_RATE


# Check that tax, mileage expense, and insurance was calculated correctly.

print("\nTax Expense =",Tax_expense,
      "\nMileage Expense =",Mileage_expense,
      "\nInsurance Expense =",Insurance_expense)


# Subtract tax rate of 20% and mileage expense from total price to find out take home.

Final_take_home = Price - Tax_expense - Mileage_expense - Insurance_expense
Hourly_wage = Final_take_home / Duration
print("\nFinal Take Home = $",round(Final_take_home,2),
      "\nHourly Wage =",round(Hourly_wage,2),"$/hr")

print("\n\t\t\t*** Don't request Dolly's with an hourly wage < 18 $/hr ***")


# Create text file and append data to it.

with open("DollyHandsCalculator.txt", "w") as df:
    df.write(str(Final_take_home))
    df.write(str(Hourly_wage))

# Include total price, distance to Dolly, commission withheld, taxes withheld, mileage expense, and final take home


# Tip Calculator Project
print("Welcome to the tip calculator!")

# User Input
total_bill = float(input("What was the total bill? $\n"))
tip_percentage = int(input("How much tip would you like to give? 10,12 or 15?\n"))
bill_split = int(input("How many people to split the bill?\n"))

# Calculate Bill with Tip
bill_with_tip = total_bill + (total_bill * (tip_percentage/100))

# Calculate Price each person has to pay
price_per_person = round(bill_with_tip/bill_split, 2)

# Result
print(f"Each person should pay: ${price_per_person}")
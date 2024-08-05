# --------------------------------------------------------------------------------------------
# Control Flow

# If-Else Statements
# Conditional execution based on the truthiness of the condition

condition = True

# If the condition is True, it will print "Hello".
# Otherwise, it will print "World".
if condition:
  print("Hello")
else:
  print("World")

# --------------------------------------------------------------------------------------------

# Comparison Operators
# Operators used to compare values

# >   - Greater than
# <   - Less than
# >=  - Greater than or equal to
# <=  - Less than or equal to
# ==  - Equal to
# !=  - Not equal to

# --------------------------------------------------------------------------------------------

# Logical Operators
# Logical operators are used to combine conditional statements.

# 'and' Operator
# Returns True if both conditions are true. If either condition is false, the result is False.
A = True
B = False
result_and = A and B  # Result: False

# 'or' Operator
# Returns True if at least one of the conditions is true. It only returns False if both conditions are false.
C = True
D = False
result_or = C or D  # Result: True

# 'not' Operator
# Returns True if the condition is false. It inverts the Boolean value of the condition.
E = True
result_not = not E  # Result: False

# --------------------------------------------------------------------------------------------

# Real Life Example: Rollercoaster Ticket Pricing

print("Welcome to the rollercoaster!")

# Get user input for height and age
height = int(input("What is your height in cm?"))
age = int(input("What is your age?"))
bill = 0


# Check if the user is tall enough to ride the rollercoaster
if height > 120:
  print("You can ride the rollercoaster")

  # Determine ticket price based on age
  if age < 12:
    print("Child tickets are 5€")
    bill += 5
  elif age <= 18: 
    print("Youth tickets are 7€")
    bill += 7
  elif age >= 45 and age <= 55: 
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    print("Adult tickets are 12€")
    bill += 12

  # Ask if the user wants a photo taken
  wants_photo = input("Do you want a photo taken? Y or N.")

  # Add the cost of the photo if desired
  if wants_photo == "Y":
    bill += 3

  # Print the final bill
  print(f"Your final bill is {bill}€")
else:
  print("Sorry, you have to grow taller before you can ride.")
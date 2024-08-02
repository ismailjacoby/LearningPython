# DATA TYPES
# --------------------------------------------------------------------------------------------

# String
# Strings are enclosed in double quotes "" or single quotes ''.
"Hello"

# Accessing a character in a string using index
# This retrieves the character at position 0 (H) from the string "Hello"
print("Hello"[0])  # Output: H

# Concatenating strings
# Adding "123" and "456" results in "123456" because they are treated as strings, not numbers
"123" + "456"  # Result: "123456"

# Note: In Python you can only concatenate strings not integers

# --------------------------------------------------------------------------------------------

# Integer / Whole Numbers
# Example of an integer
123

# Performing arithmetic with integers
# Adding 123 and 456 gives 579
123 + 456  # Result: 579

# Float / Decimal Numbers
# Example of a float (decimal number)
3.14159

# When performing arithmetic operations with integers and floats, the result will always be a float.

# --------------------------------------------------------------------------------------------

# Booleans
# Boolean values represent True or False
# Note: Booleans start with an uppercase letter
True 
False

# --------------------------------------------------------------------------------------------

# Type Conversion

# type() will check the type of the given parameter
num = 1
print(type(num)) # Output: <class 'int'>

# Type Conversion
str(123) # Convert integer to string
float("123.5") # Convert string to float

# --------------------------------------------------------------------------------------------

# Math Operations
addition = 3 + 5  # Addition
subtraction = 7 - 4  # Subtraction
multiplication = 3 * 2  # Multiplication
division = 6 / 3  # Division - Result is always a float when dividing numbers
floor_division = 8 // 3  # Floor division - Result is an integer, discards remainder
power = 2 ** 3  # 2 to the power of 3, which is 8


# PEMDAS (Order of Operations)
# Parentheses ()
# Exponentiation **
# Multiplication * and Division /
# Addition + and Subtraction -

# Compound Assignment Operators
score = 0
score += 1  # Equivalent to : score = score + 1
score -= 1  # Equivalent to : score = score - 1
score *= 1  # Equivalent to : score = score * 1
score /= 1  # Equivalent to : score = score / 1
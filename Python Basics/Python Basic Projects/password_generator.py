#Password Generator Project
import random

# Define lists of possible characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Get user input for the number of each character type
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Password with characters in the order specified
password = ""

# Add random letters to the password
for letter in range(0, nr_letters):
  password += random.choice(letters)

# Add random symbols to the password
for letter in range(0, nr_symbols):
  password += random.choice(symbols)

# Add random numbers to the password
for letter in range(0, nr_numbers):
  password += random.choice(numbers)

print(f"Easy Level Password: {password}")


# Hard Level - Randomize the order of characters
# Convert the password to a list of characters, shuffle it, and join back into a string

password_list = list(password)
random.shuffle(password_list)
hard_password = ''.join(password_list)

print(f"Hard Level Password: {hard_password}")
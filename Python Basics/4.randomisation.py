# --------------------------------------------------------------------------------------------

# Random

# Import the random module to use its functions
import random;

# Generate a Random Integer
# Returns a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1,10) # Example: 7

# Generate a Random Floating Point Number within a Specified Range
# Returns a random float between 1.0 and 10.0 (inclusive)
random_float = random.uniform(1, 10)  # Example: 7.345

# Generate a Random Floating Point Number between 0.0 and 1.0 (exclusive)
random_float = random.random() # Example: 0.456

# Generate a Random Floating Point Number between 0.0 and 10.0 (exclusive)
random_float = random.random() * 10 # Example: 5.678

# --------------------------------------------------------------------------------------------

# Lists
# Lists are ordered collections that can contain various data types

# Create a List of States
states_in_the_us = ["California","Florida", "New York"]

# Example operations on lists:
# Accessing the first element
first_state = states_in_the_us[0]  # Result: "California"

# Adding a new state to the list
states_in_the_us.append("Texas")

# Removing a state from the list
states_in_the_us.remove("Florida")

# Printing the updated list
print(states_in_the_us)  # Example Output: ['California', 'New York', 'Texas']

# Nested Lists
# Lists within lists to represent more complex data structures

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Broccoli", "Spinach", "Tomatoes"]

# Creating a Nested List
healthy_food = [fruits, vegetables]

# Printing the Nested List
print(healthy_food) # Output: [["Apple", "Banana", "Orange"], ["Broccoli", "Spinach", "Tomatoes"]]

# Accessing an Element in a Nested List
print(healthy_food[0][2]) # Output: Orange

# --------------------------------------------------------------------------------------------

# Excercise - Who pays the bill?
# Randomly choose a friend to pay the bill

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1: Using random.choice()
print(random.choice(friends)) 

# Option 2: Using random.randrange()
print(friends[random.randrange(0, len(friends))])
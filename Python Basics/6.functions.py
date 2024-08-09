# Functions

# Note: In Python, the function must be declared before we can call it.

# Define a function that prints "Hello World"
def say_hello_world():
  print("Hello World")

# Call the function to execute its code
say_hello_world()

# Functions that have inputs, in this case (a,b)
def add_two_numbers(a, b):
  return a + b

# Call the function with arguments 10 and 5, and print the result
result = add_two_numbers(10, 5)
print(result)  # Output: 15

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

# Keyword argument
greet_with(name="John", location="Luxembourg")
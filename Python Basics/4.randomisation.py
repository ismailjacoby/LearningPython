# --------------------------------------------------------------------------------------------
# Random

# Imports the random module
import random;

# randint() will return a random integer between 1 & 10 (inclusive)
random_integer = random.randint(1,10)

# Generates random floating point number in the range 0.0 and 1.0 (inclusive)
random_integer = random.uniform(1,10)

# Generates random floating point number in the range 0.0 and less than 1.0
random_float = random.random()

# Generates random floating point number in the range 0.0 and less than 10.0
random_float = random.random() * 10


#Prints the random number
print(random_integer)
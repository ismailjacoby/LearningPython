# For Loop

# List of fruits
fruits = ["Apple", "Banana", "Orange"]

# Iterate over each fruit in the list
for fruit in fruits:
    # Print out the current fruit
    print(fruit)

# --------------------------------------------------------------------------------------------

# Range

# Iterate over a sequence of numbers from 1 to 99
# range(start, stop) generates numbers from start up to, but not including, stop
for number in range(1, 100):
    print(number)

# Iterate over a sequence of numbers from 0 to 99 with a step of 5
# range(start, stop, step) generates numbers from start up to, but not including, stop, incremented by step
for number in range(0, 100, 5):
    print(number)

# --------------------------------------------------------------------------------------------

# Example

# List of student scores
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65]

# Method 1: Using built-in sum() function to calculate the total score
total_exam_score = sum(student_scores)
print(f"Total exam score (Method 1): {total_exam_score}")

# Method 2: Using a for loop to manually sum the scores
total_sum = 0

for score in student_scores:
    total_sum += score

print(f"Total exam score (Method 2): {total_sum}")




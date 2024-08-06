import random

# List of choices
choice = ["Rock", "Paper", "Scissor"]

print("Welcome to Rock Paper Scissors!")

# Get user choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))



# Validate user choice
if user_choice not in [0, 1, 2]:
    print("Invalid choice. Please choose 0, 1, or 2.")
else:
  # Get computer choice
  computer_choice = random.randint(0,2)

  # Display user choice
  print(f"You chose: {choice[user_choice]}")

  # Display computer choice
  print(f"Computer chose: {choice[computer_choice]}")

  # Determine the winner
  if user_choice == computer_choice:
    print("It's a Draw")
  elif  (user_choice == 0 and computer_choice == 2) or \
        (user_choice == 1 and computer_choice == 0) or \
        (user_choice == 2 and computer_choice == 1):
    print("You Win")
  else:
    print("You Lose")
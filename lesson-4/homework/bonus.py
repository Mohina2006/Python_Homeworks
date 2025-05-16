import random

human_count = 0
computer_count = 0
my_list = ["rock", "paper", "scissors"]

while True:
    computer_choice = random.choice(my_list)
    user_choice = input("Enter rock, paper or scissors: ").lower()
    
    if user_choice not in my_list:
        print("Invalid input. Please try again.")
        continue
    
    print(f"Computer chose {computer_choice}")
    print(f"You chose {user_choice}")
    
    if computer_choice == user_choice:
        print("It is a tie!")
    elif (computer_choice == "rock" and user_choice == "scissors") or \
         (computer_choice == "scissors" and user_choice == "paper") or \
         (computer_choice == "paper" and user_choice == "rock"):
        computer_count += 1
        print("Computer wins this round!")
    else:
        human_count += 1
        print("You win this round!")
    
    print(f"Score - You: {human_count}, Computer: {computer_count}")
    
    if human_count == 5:
        print("You won the game!")
        break
    elif computer_count == 5:
        print("Computer won the game!")
        break
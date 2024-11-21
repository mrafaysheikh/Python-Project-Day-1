#Project Day 1

import random
choices = ["Rock","Paper"," Scissor"]
print("Welcome to Rock,Paper, or Scissor!")

#Now Enter player choices

player_choice= input("Enter your Choice,(Rock,Paper, or Scissor):")

#CHeck player choice is correct or not

if player_choice not in choices:
    print("Invalid Choice, Enter the Choice Again,(Rock, Paper,or Scissor:")

else:

    computer_choice = random.choice(choices)
    print(f"\nplayer choice: {player_choice}")
    print(f"computer choice: {computer_choice}")

if player_choice == computer_choice:
    print("it's a Tie")

elif (player_choice == "Rock" and computer_choice == "Scissor") or \
     (player_choice == "Scissor" and computer_choice == "Paper") or \
     (player_choice == "Paper" and computer_choice == "Rock"):

     print("player Win!")

else:
     print("computer Win!")








      

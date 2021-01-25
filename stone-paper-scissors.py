# STONE PAPER SCISSORS!

import random

num_of_rounds = int(input("Enter the number of rounds: "))

human_score = 0
comp_score = 0

comp_random = random.randint(1, 3)

if comp_random == 1:
    comp_choice = "Stone"

elif comp_random == 2:
    comp_choice = "Paper"

else:
    comp_choice = "Scissors"

for num in range(1, num_of_rounds + 1):
    human_choice = input("Enter 'Stone', 'Paper' or 'Scissors': ")

    print(f"You chose: {human_choice}")
    print(f"The computer chooses: {comp_choice}")

    if human_choice == "Stone" or human_choice == "stone":
        if comp_choice == "Stone":
            human_score = human_score + 0
            comp_score = comp_score + 0
            print(f"Your score: {human_score}")
            print(f"Computer's score: {comp_score}")

        elif comp_choice == "Paper":
            comp_score = comp_score + 1
            print(f"Your score: {human_score}")
            print(f"Computer's score: {comp_score}")

        else:
            human_score = human_score + 1
            print(f"Your score: {human_score}")
            print(f"Computer's score: {comp_score}")

    elif human_choice == "Paper" or human_choice == "paper":
        if comp_choice == "Stone":
            human_score = human_score + 1
            print(f"Your score: {human_score}")
            print(f"Computer's score: {comp_score}")

        elif comp_choice == "Paper":
            human_score = human_score + 0
            comp_score = comp_score + 0
            print(f"Your score: {human_score}")
            print(f"Computer's score: {comp_score}")

        else:
            comp_score = comp_score + 1
            print(f"Your score: {human_score}")
            print(f"Computer's score: {comp_score}")

    elif human_choice == "Scissors" or human_choice == "scissors":
        if comp_choice == "Stone":
            comp_score = comp_score + 1
            print(f"Your score: {human_score}")
            print(f"Computer's score: {comp_score}")

        elif comp_choice == "Paper":
            human_score = human_score + 1
            print(f"Your score: {human_score}")
            print(f"Computer's score: {comp_score}")

        else:
            human_score = human_score + 0
            comp_score = comp_score + 0
            print(f"Your score: {human_score}")
            print(f"Computer's score: {comp_score}")

    else:
        print("Error: Incorrect input")

print(f"Your total score: {human_score}")
print(f"Computer's total score: {comp_score}")

if human_score > comp_score:
    print("You won! 🍾 🍾")

elif human_score < comp_score:
    print("Computer won! 🍾 🍾")

else:
    print("It's a draw!")
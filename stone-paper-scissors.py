# STONE PAPER SCISSORS!

human_1 = input(
    """Player 1
Enter 'Stone', 'Paper' or 'Scissors':"""
)
human_2 = input(
    """Player 2
Enter 'Stone', 'Paper' or 'Scissors':"""
)
if human_1 == "Stone" or human_1 == "stone":
    if human_2 == "Stone" or human_2 == "stone":
        print("It's a draw!")
    elif human_2 == "Paper" or human_2 == "paper":
        print("Human 2 wins the match! 🍾 🍾")
    elif human_2 == "Scissors" or human_2 == "scissors":
        print("Human 1 wins the match! 🍾 🍾")

elif human_1 == "Paper" or human_2 == "paper":
    if human_2 == "Stone" or human_2 == "stone":
        print("Human 1 wins the match! 🍾 🍾")
    elif human_2 == "Paper" or human_2 == "paper":
        print("It's a draw!")
    elif human_2 == "Scissors" or human_2 == "scissors":
        print("Human 2 wins the match! 🍾 🍾")

elif human_1 == "Scissors" or human_2 == "scissors":
    if human_2 == "Stone" or human_2 == "stone":
        print("Human 2 wins the match! 🍾 🍾")
    elif human_2 == "Paper" or human_2 == "paper":
        print("Human 1 wins the match! 🍾 🍾")
    elif human_2 == "Scissors" or human_2 == "scissors":
        print("It's a draw!")
else:
    print("Error: Incorrect input")
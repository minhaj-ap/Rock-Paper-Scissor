import random

options = ["rock", "paper", "scissor"]
userScore = 0
botScore = 0
attempts = 6
while attempts > 0:
    botOption = options[random.randint(0, 2)]
    userOption = input("Choose your option(rock,paper,sccissor): ").lower()
    attempts -= 1
    print(f"Bot choosed: {botOption}")
    if (
        (userOption == "rock" and botOption == "scissor")
        or (userOption == "scissor" and botOption == "paper")
        or (userOption == "paper" and botOption == "rock")
    ):
        print("You gained a score")
        userScore += 1
    elif (
        (botOption == "rock" and userOption == "scissor")
        or (botOption == "scissor" and userOption == "paper")
        or (botOption == "paper" and userOption == "rock")
    ):
        print("Bot gained a score")
        botScore += 1
    elif userOption not in options:
        print("Invalid input")
        attempts+=1
    else:
        print("It's a tie")
if botScore < userScore:
    print("YOU WON!!!")
elif userScore < botScore:
    print("YOU LOST")
else:
    print("IT'S A TIE")
print(f"Your score:{userScore}\n Bot score:{botScore}")

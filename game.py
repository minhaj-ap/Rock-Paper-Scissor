import random


def gamePlay():
    options = ["rock", "paper", "scissor"]
    userScore = 0
    botScore = 0
    attempts = 6
    while attempts > 0:
        botOption = options[random.randint(0, 2)]
        userOption = input("Choose your option(rock,paper,sccissor): ").lower()
        attempts -= 1
        print(f"Bot choosed: {botOption}")
        if userOption not in options:
            print("Invalid input")
            attempts += 1
        elif userOption == botOption:
            print("It's a tie")
        else:
            userScore += scoreChooser(userOption, botOption, "user")
            botScore += scoreChooser(botOption, userOption, "bot")

    if botScore < userScore:
        print("YOU WON!!!")
    elif userScore < botScore:
        print("YOU LOST")
    else:
        print("IT'S A TIE")
    print(f"Your score:{userScore}\n Bot score:{botScore}")


def scoreChooser(option1, option2, player):
    if (
        (option1 == "rock" and option2 == "scissor")
        or (option1 == "scissor" and option2 == "paper")
        or (option1 == "paper" and option2 == "rock")
    ):
        print(f"You {"lost"if player=="bot" else "gained"} a score")
        return 1
    else:
        return 0


gamePlay()

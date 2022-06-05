import random

ai = random.choice(["ROCK", "PAPER", "SCISSORS"])
user = str.upper(input("Enter your choice: "))
if user == "ROCK" or user == "PAPER" or user == "SCISSORS":
    print("Your choice:", str.lower(user), "\nMy choice:", str.lower(ai))
    if user == ai:
        print("I have selected", str.lower(ai), ", so have you. So it's a draw!")
    else:
        if user == "ROCK":
            if ai == "PAPER":
                print("The rock got completely wet infront of the paper. I Win!")
            else:
                print("Scissors got banged hard by the hit of the rock. You win :(")
        if user == "PAPER":
            if ai == "SCISSORS":
                print("The paper got shreded to pieces by the scissors. I Win!")
            else:
                print("The rock ripped to pieces after seeing the paper. You Win :(")
        if user == "SCISSORS":
            if ai == "ROCK":
                print("The rock broke through the scissors. I Win!")
            else:
                print("The scissors didnt leave a sign of existence for the paper. You win :(")
else:
    print("Invalid input. Enter a proper word.")
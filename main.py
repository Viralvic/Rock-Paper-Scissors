from random import choice

done = False
all_choices = ["rock", "paper", "scissors"]
computer_score = 0
user_score = 0

# game loop
while not done:
    choice_made = None

    # generate random choice for Computer
    computer_choice = choice(all_choices)

    # ask user for user's choice
    user_input = input("\nEnter R for Rock, P for Paper, or S for Scissor: ")

    # validate user's input
    if user_input == "R":
        user_choice = "rock"
        choice_made = "valid"
    elif user_input == "P":
        user_choice = "paper"
        choice_made = "valid"
    elif user_input == "S":
        user_choice = "scissors"
        choice_made = "valid"
    else:
        print("Invalid input. Try again!!!")

    # if user input is valid, compare
    if choice_made == "valid":
        print(f"Machine selects \'{computer_choice}\', user selects \'{user_choice}\'")

        if user_choice == computer_choice:
            print("Its a tie !!!")
        else:
            if user_choice == "rock":
                if computer_choice == "paper":
                    print("Computer wins!!!")
                    computer_score += 1
                else:
                    print("You win!!!")
                    user_score += 1
            if user_choice == "paper":
                if computer_choice == "scissors":
                    print("Computer wins!!!")
                    computer_score += 1
                else:
                    print("You win!!!")
                    user_score += 1
            if user_choice == "scissors":
                if computer_choice == "rock":
                    print("Machine wins!!!")
                    computer_score += 1
                else:
                    print("You win!!!")
                    user_score += 1
        print("Thanks for playing")
        print(f"Final Score: Computer = {computer_score}, User = {user_score}")
        done = True
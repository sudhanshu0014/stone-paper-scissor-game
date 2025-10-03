import random
while True:

    print("Welcome to stone, paper , scissor game.")
    
    number_of_rounds = int(input("How many times you wanna try your luck:"))

    choices = {
        "stone": -1,
        "paper": 0,
        "scissor":1
    }
    computer_choices = {
        1  : "scissor",
        0 : "paper",
        -1 : "stone"
    }
    computer_score = 0
    user_score = 0

    for i in range(number_of_rounds):
        users_choice = input("enter your choice:")
        user_input = choices.get(users_choice)
        if user_input is None:
            print("invalid choice, please choose from : stone , paper or scissor.")
        computer_input = random.randint(-1,1)
        computer_choice = computer_choices.get(computer_input)

        print(f'''
            you chose {users_choice}
            computer chose {computer_choice}
            ''')
        
        if computer_input == user_input:
            print("Its a draw.")
        elif computer_input == 1 and user_input == 0:
            computer_score+=1
            print("you lose this time.")
        elif computer_input == 1 and user_input == -1: 
            user_score+=1 
            print("you won this time.")  
        elif computer_input == 0 and user_input == -1:
            computer_score+=1
            print("you lose this time.")
        elif computer_input == 0 and user_input == 1:
            user_score+=1 
            print("you won this time.")
        elif computer_input == -1 and user_input == 1:
            computer_score+=1
            print("you lose this time.")
        elif computer_input == -1 and user_input == 0:
            user_score+=1 
            print("you won this time.")
        else:
            print("something went wrong.")

    print(f'''Here is the final score:
        computer won {computer_score} rounds
        you won = {user_score} rounds''')
    if computer_score == user_score:
        print("Its a draw.Better luck next time.")
    elif computer_score > user_score:
        print("You lose buddy.Go home.")
    elif computer_score < user_score:
        print("You won.Celebrate your victory.")   
    else:
        print("Something went wrong.")           

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
            print("Thanks for playing with me.")
            break

    

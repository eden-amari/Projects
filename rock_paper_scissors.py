import random

# Initializing
print("Welcome to Rock, Paper, Scissors!\nHow many rounds do you want to play?")
rounds = int(input("Number of rounds: "))


print("\n")

print("Ready?")
print("To answer, play choose Rock, Paper, or Scissors. If you're ready to stop playing, type Q to quit.")


print("\n")

def run_game():
    user_wins = 0
    computer_wins = 0
    round_count = 1

    while round_count <= rounds:
        # Setting up the score counter
        
        for x in range(rounds):
            print(f"Round {round_count}: ")
            acceptable_answers = ["Rock", "rock", "Paper", "paper", "Scissor", "Scissors", "scissors"]
            acceptable_rock_answers = ["Rock", "rock"]
            acceptable_paper_answers = ["Paper", "paper"]
            acceptable_scissors_answers = ["Scissor", "Scissors", "scissors"]
            quit_inputs = ["Quit", "quit", "Q", "q",]

            # Allowing the user to choose r/p/s
            user_choice = input("Your Choice >> ")

            # Non-inputs
            while user_choice not in acceptable_answers:
                if user_choice not in quit_inputs:
                    print("Hm...that's not a fair choice. Try again!")
                    user_choice = input("Your Choice >> ")
                    print("\n")

                # If user quits
                elif user_choice in quit_inputs:
                    print("Thanks for playing!")
                    break
    
            
            if user_choice in acceptable_answers:
                # Computer Choice
                rand_num = random.randint(1, 3)
                    # 1 = rock
                    # 2 = paper
                    # 3 = scissors
                
            
                # If the computer picks rock
                if rand_num == 1 and user_choice not in acceptable_paper_answers:
                    computer_wins += 1
                    print("Sorry, the computer takes this round!")
                    print(f"User: {user_wins}, Computer: {computer_wins}")
                    print("\n")

                # If the computer picks paper
                elif rand_num == 2 and user_choice not in acceptable_scissors_answers:
                    computer_wins += 1
                    print("Sorry, the computer takes this round!")
                    print(f"User: {user_wins}, Computer: {computer_wins}")
                    print("\n")


                # If the computer picks scissors
                elif rand_num == 3 and user_choice not in acceptable_rock_answers:
                    computer_wins += 1
                    print("Sorry, the computer takes this round!")
                    print(f"User: {user_wins}, Computer: {computer_wins}")
                    print("\n")
                
                else:
                    user_wins += 1
                    print("You win this round!")
                    print(f"User: {user_wins}, Computer: {computer_wins}")
                    print("\n")
                round_count += 1
    print(f"Final Score:\nUser: {user_wins}, Computer: {computer_wins}")




    # Would they like to play again?
    if user_choice not in quit_inputs:
        print("\n")
        print("Play again?")
        play_again = input("")

        acceptable_yes_answers = ["Yes", "YES", "yes", "Y", "y",]
        acceptable_no_answers = ["No", "NO", "no", "N", "n",]
        if play_again in acceptable_yes_answers:
            print("\n")
            run_game()
        
        elif play_again in acceptable_no_answers:
            while play_again in acceptable_no_answers:
                print("\n")
                print("Thanks for playing! :}")
                break

        elif play_again not in acceptable_yes_answers and play_again not in acceptable_no_answers:
            while play_again not in acceptable_yes_answers and play_again not in acceptable_no_answers:
                print("\n")
                print("Invalid input, try again.")
                play_again = input("")
run_game()
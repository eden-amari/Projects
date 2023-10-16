import random
rand_num = random.randrange(1, 101)

player_name = input("Please enter your name: ")
print("Hi", player_name + "!")
print("I have generated random number between 1 and 100. You will have 10 attempts to guess the number.")

print("Guess 1: ", end="")
user_guess = int(input(""))

## ----------------------------------------------------------------------------------------

for i in range(1, 11):
    if user_guess != rand_num:
       if user_guess < rand_num:
           print("Your guess is less than my random number. Try again.")
           i += 1
           print(f"Guess {i}: ", end="")
           user_guess = int(input(""))
       else: 
           print("Your guess is greater than my random number. Try again.")
           i += 1
           print(f"Guess {i}: ", end="")
           user_guess = int(input(""))

    else:
        print("You correctly guessed my number!")
        break
           
       

    
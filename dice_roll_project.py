import random

print("Hello there!")
print("--------------->>")
print("How many dice do you wish to roll?")

roll_again = ""

# Roll process -------------------------------------
def roll_die():
    num_dice = int(input("Number of dice: "))
    if num_dice < 1:
        while num_dice < 1:
            print("Number of dice must be at least one. Try again!")
            num_dice = int(input("Number of dice: "))

    print("How many sides does your desired die have?")
    num_sides = int(input("Number of sides: "))

    print("\n")

    if num_sides < 2:
        while num_sides < 2:
            print("Number of sides must be at least two. Try again!")
            num_sides = int(input("Number of sides: "))

    if num_dice == 1:
        print("Rolling...")
        print(f'You rolled a {random.randrange(1, num_sides)} !')
    

    if num_dice > 1:
        print("Rolling...")
        count = 1
        roll_sum = 0
        while count <= num_dice:
            roll_num = random.randrange(1, num_sides)
            print(f'Roll {count}: You rolled a {roll_num}!')
            count += 1
            roll_sum += roll_num
        print("Total:", roll_sum )

    
    # Another roll? -------------------------------
    valid_yes_answers = ["Yes", "yes", "Y", "y",]
    valid_no_answers = ["No", "no", "N", "n",]

    print("\n")
    print(f'Would you like to roll again? Please type "Yes" or "No".')
    roll_again = str(input())

    if roll_again in valid_yes_answers:
        roll_die()
    
    elif roll_again in valid_no_answers:
        print("Understood. Thank you for using this roll generator!")
    
    else:
        while roll_again not in valid_yes_answers and roll_again not in valid_no_answers:
            print("\n")
            print("Error! Please try again.")
            print(f'Would you like to roll again? Please type "Yes" or "No".')

            roll_again = str(input())
            if roll_again in valid_yes_answers:
                    roll_die()
            
            if roll_again in valid_no_answers:
                print("\n")
                print("Understood. Thank you for using this roll generator!")
                break


# Execute function
roll_die()
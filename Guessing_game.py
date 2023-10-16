#W0478181
#Repository: <https://github.com/W0478181/PROG1700Assignments>
#Import Modules and variables
import random
import sys
#Initialize variables
yes = "yes"
no = "no"
# Ask Users for their name
user_name = None
error_count = 0
user_guess = None
user_score = 0
comp_score = 0
tries = 0
def error():
    global error_count
    error_count += 1
    if error_count == 3:
        print("3 strikes and you're out, try again when you're ready")
        sys.exit()
error()
while True:
    user_name = input("Hello, My Name is Al Gorithm, What is yours: ")
    # Users must enter a name with no digits
    if user_name.isdigit():
        print("Enter a valid name.")
        error()
    else:                 
        break
print(f"Hi {user_name}, We are going to play a guessing game. I will pick a number from 1 to 10, and you will have 5 attempts to guess my number to win.")
def guessing_game():
    global tries, user_score, comp_score
    computer_value = random.randint(1, 10)
    while tries < 5:
        user_guess = input("What is your guess?: ")
        # Check if the user's guess is a valid number
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess == computer_value:
                tries += 1
                user_score += 1
                print(f"Congrats, you guessed my number in {tries} tries!")
                print(f"User Score: {user_score}, Al Gorithm Score: {comp_score}")
                break
            elif user_guess < computer_value:
                print("Your guess is too low.")
                tries += 1
            else:
                print("Your guess is too high.")
            tries += 1
            if tries >= 5:
                print(f"That's 5 tries! The number was {computer_value}.")
                comp_score += 1
                print(f"User Score: {user_score}, Al Gorithm Score: {comp_score}")
        else:
            error()
guessing_game()
while True:
    repeat = input("Would you like to try the algorithm again? (yes or no): ").lower()
    if repeat == yes:
        guessing_game()
    elif repeat == no:
        break
    else:
        print("Please put yes or no")
        error()
        error()

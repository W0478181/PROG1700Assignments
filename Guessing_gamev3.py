#W0478181
#Repository: <https://github.com/W0478181/PROG1700Assignments>
<<<<<<< HEAD
#Import Modules and variablesimport random
import sys
import random
error_count = 0
tries = 0
user_score = 0
comp_score = 0
#If users get 3 errors they will get message and program will close and User will only have 5 tries
def error():
    global error_count
    error_count += 1
    if error_count == 3:
        print("3 strikes and you're out, try again when you're ready")
        sys.exit()
def again():
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == "yes"
while True:
    computer_value = random.randrange(1, 10, 1)
    #Users must enter a name with no digits
    user_name = input("Hello, My Name is Al Gorithm. What is yours:")
    if user_name.isalpha():
        print(f"Hi {user_name}, we are going to play a guessing game. I will pick a number from 1 to 10, and you will have 5 attempts to guess my number to win.")
    else:
        print("Please use letters only")
        error()
        continue
    while tries < 5:
        #Users guess must be a number 1-10 only
        user_guess = int(input("What is your guess?:"))
=======
#Import Modules and variables
import random
import sys
#If users get 3 errors they will get message and program will close and User will only have 5 tries
error_count = 0
#Keep score
user_score = 0
comp_score = 0 
while True:
    user_name = input("Hello My Name is Al Gorithm, What is yours:")       
    #Users must enter a name letters only
    if user_name.isalpha():
        print(f"Hi {user_name}, We are going to play a guessing game.I will pick a number from 1 to 10, and you will have 5 attempts of guessing my number to win.")
        break
    else:
        print("Please use letter only")
        error_count += 1
        if error_count == 3:
            print("3 strikes and you're out, try again when you're ready")
            sys.exit()
while True:
    tries = 0  # Initialize tries for each game
    computer_value = random.randint(1, 10)
    while tries < 5:
        user_guess = int(input("Whats your guess?: "))
>>>>>>> 1a8def7101ff8a8b9774bed8ffbeebf81494fbbd
        if 1 <= user_guess <= 10:
            tries += 1
            if user_guess == computer_value:
                user_score += 1
<<<<<<< HEAD
                print(f"Congrats, you guessed my number on the {tries} try!")
                print(f"User Score: {user_score}, Al Gorithm Score: {comp_score}")
                break
=======
                print(f"Congrats, you guessed my number in {tries} tries!\nUser Score: {user_score}, Al Gorithm Score: {comp_score}")
                break
            #Users will be told if guess is too high or too low
>>>>>>> 1a8def7101ff8a8b9774bed8ffbeebf81494fbbd
            elif user_guess < computer_value:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")
        else:
<<<<<<< HEAD
            print("Enter a valid number")
            error_count += 1
            error()
    if tries == 5:
        comp_score += 1
        print(f"That's 5 tries! The number was {computer_value}.")
        print(f"User Score: {user_score}, Al Gorithm Score: {comp_score}")
    #If users enter yes it will be true and game will restart
    if not again():
        sys.exit()
=======
            print("Enter a valid number.")
            error_count += 1
            if error_count == 3:
                print("3 strikes and you're out, try again when you're ready")
                sys.exit()
    if tries == 5:
        comp_score += 1
        print(f"That's 5 tries! The number was {computer_value}\nUser Score: {user_score}, Al Gorithm Score: {comp_score}")

    play_again = input("Do you want to play again? (yes or no): ")
    if play_again.lower() != "yes":
        break
>>>>>>> 1a8def7101ff8a8b9774bed8ffbeebf81494fbbd

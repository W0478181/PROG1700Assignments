#W0478181
#Repository: <https://github.com/W0478181/PROG1700Assignments>
#Import Modules and variables
import random
import sys
<<<<<<< HEAD
def error():
    global error_count
    error_count += 1
    if error_count == 3:
        print("3 strikes and you're out, try again when you're ready")
        sys.exit()
=======
#If users get 3 errors they will get message and program will close and User will only have 5 tries
error_count = 0
>>>>>>> 1a8def7101ff8a8b9774bed8ffbeebf81494fbbd
while True:
    #If users get 3 errors they will get message and program will close and User will only have 5 tries
    error_count = 0
    tries = 0
    computer_value = random.randrange(1,10,1)
    user_name = input("Hello My Name is Al Gorithm, What is yours:")       
    #Users must enter a name letters only
    if user_name.isalpha():
        print(f"Hi {user_name}, We are going to play a guessing game.I will pick a number from 1 to 10, and you will have 5 attempts of guessing my number to win.")
    else:
        print("Please use letter only")
<<<<<<< HEAD
        error()
        continue
    while tries < 5:
        #Users guess must be a number 1-10 only
        user_guess = int(input("What is your guess?:"))
        if user_guess >= 1 and user_guess <= 10:
            tries += 1
            if user_guess == computer_value:
                print(f"Congrats,You guessed my number on the {tries} try!")
=======
        error_count += 1
        if error_count == 3:
            print("3 strikes and you're out, try again when you're ready")
            sys.exit()
while True:
    tries = 0  # Initialize tries for each game
    computer_value = random.randint(1, 10)
    while tries < 5:
        user_guess = int(input("Whats your guess?: "))
        if 1 <= user_guess <= 10:
            tries += 1
            if user_guess == computer_value:
                print(f"Congrats, you guessed my number in {tries} tries!")
>>>>>>> 1a8def7101ff8a8b9774bed8ffbeebf81494fbbd
                break
            #Users will be told if guess is too high or too low
            elif user_guess < computer_value:
                print("Your guess is too low.")
            else:
<<<<<<< HEAD
            
                print("Your guess is too high.")
        else:
            print("Enter a valid number")
            error()
    if tries == 5:
        comp_score =+ 1
        print(f"Thats 5 tries! the number was {computer_value}.")
=======
                print("Your guess is too high.")
        else:
            print("Enter a valid number.")
            error_count += 1
            if error_count == 3:
                print("3 strikes and you're out, try again when you're ready")
                sys.exit()
    if tries == 5:
        print(f"That's 5 tries! The number was {computer_value}")

    play_again = input("Do you want to play again? (yes or no): ")
    if play_again.lower() != "yes":
        break
>>>>>>> 1a8def7101ff8a8b9774bed8ffbeebf81494fbbd

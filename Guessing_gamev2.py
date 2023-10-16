#W0478181
#Repository: <https://github.com/W0478181/PROG1700Assignments>
#Import Modules and variables
import random
import sys
def error():
    global error_count
    error_count += 1
    if error_count == 3:
        print("3 strikes and you're out, try again when you're ready")
        sys.exit()
while True:
    #If users get 3 errors they will get message and program will close and User will only have 5 tries
    error_count = 0
    tries = 0
    computer_value = random.randrange(1,10,1)
    user_name = input("Hello My Name is Al Gorithm, What is yours:")       
    #Users must enter a name with no digits
    if user_name.isalpha():
        print(f"Hi {user_name}, We are going to play a guessing game.I will pick a number from 1 to 10, and you will have 5 attempts of guessing my number to win.")
    else:
        print("Please use letter only")
        error()
        continue
    while tries < 5:
        #Users guess must be a number 1-10 only
        user_guess = int(input("What is your guess?:"))
        if user_guess >= 1 and user_guess <= 10:
            tries += 1
            if user_guess == computer_value:
                print(f"Congrats,You guessed my number on the {tries} try!")
                break
            #Users will be told if guess is too high or too low
            elif user_guess < computer_value:
                print("Your guess is too low.")
            else:
            
                print("Your guess is too high.")
        else:
            print("Enter a valid number")
            error()
    if tries == 5:
        comp_score =+ 1
        print(f"Thats 5 tries! the number was {computer_value}.")
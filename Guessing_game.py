#W0478181
#Repository: <https://github.com/W0478181/PROG1700Assignments>
#Import Modules and variables
import random
import sys
#ask Users for their name
user_name = None
#If users get 3 errors they will get message and program will close
error_count = 0
user_guess = None
#Variables to keep score
user_score = 0
comp_score = 0
#User will only have 5 tries
tries = 0
while True:
            user_name = input("Hello My Name is Al Gorithm, What is yours:")       
            #Users must enter a name with no digits
            if user_name.isdigit():
                print("Enter a valid name.")
                error_count += 1
                if error_count >= 3:
                    print("3 strikes and your out,try again when your ready")
                    sys.exit()                 
            else:
                user_name == str
                break
print(f"Hi {user_name}, We are going to play a guessing game.I will pick a number from 1 to 10, and you will have 5 attempts of guessing my number to win.")
computer_value = random.randrange(1,10,1)
while True:
    user_guess = input("What is your guess?:")
    #Users guess must be a number
    if user_guess.isdigit:
        user_guess = int(user_guess)
    #Cast to an integer numbers 1-10 only
    #Calculate computer's value
        if user_guess == computer_value:
            tries += 1
            user_score += 1
            print(f"Congrats,You guessed my number in {tries} tries!")
            print(f"User Score:{user_score},Al Gorithm Score:{comp_score}")
            break
        #Users will be told if guess is too high or too low
        elif ((user_guess < computer_value)):
            print("your guess is too low.")
            tries += 1
            if tries >= 5:
                print(f"Thats 5 tries! the number was {computer_value}.")
                comp_score += 1
                print(f"User Score:{user_score},Al Gorithm Score:{comp_score}")
        else:
            print("Your guess is too high.")
            tries +=1
            if tries >=5:
                print(f"Thats 5 tries! the number was {computer_value}.")
                print(f"User Score:{user_score},Al Gorithm Score:{comp_score}")
            
    else:
        print("Enter a valid guess.")
        error_count += 1
        if error_count >= 3:
            print("3 strikes and your out,try again when your ready")
            sys.exit()           
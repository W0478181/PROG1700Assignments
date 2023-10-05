#W0478181
#Repository: <https://github.com/W0478181/PROG1700Assignments>
#Import Modules and variables
import random
import sys
#List of options so users input can be displayed as what they played
options = {1:"rock",2:"paper",3:"scissors"}
#If error count gets to 3 its will give a message and run sys.exit()
error_count = 0
#Scoreboard for users to see 
user_score = 0
comp_score = 0
#Program Control
while True:
    user_input = input("Press 1 for rock, 2 for paper, 3 for scissors:")
    #Validate the input to ensure the program has valid input
    #Return true is a digit is entered or else false
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input <=3 and user_input >=1:
            #Cast to an integer 1,2,3 numbers only
            #Calculate computer's value
            computer_value = random.randrange(1,4,1)
            #Determine the computer's choice
            #Determine winner 
            if user_input == computer_value:
                print(f"It's a tie!You both played {options[user_input]}.")
                print(f"User Score:{user_score},Al Gorithm Score:{comp_score}")
            elif ((user_input == 1 and computer_value == 3) or (user_input == 2 and computer_value == 1) or (user_input == 3 and computer_value == 2)):
                print(f"You win!You played {options[user_input]} and Al Gorithm played {options[computer_value]}.")
                user_score += 1
                print(f"User Score:{user_score},Al Gorithm Score:{comp_score}")
            else:
                print(f"Computer wins!You played {options[user_input]} and Al Gorithm played {options[computer_value]}.")
                comp_score += 1
                print(f"User Score:{user_score},Al Gorithm Score:{comp_score}")
        else:
            print("Enter a valid number")
            error_count += 1
            if error_count >= 3:
                print("3 strikes and your out,try again when your ready")
                sys.exit()
    else:
        print("Enter a valid number")
        error_count += 1
        if error_count >= 3:
            print("3 strikes and your out,try again when your ready")
            sys.exit()
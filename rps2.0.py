#W0478181
# #Repository: <https://github.com/W0478181/PROG1700Assignments>
#Import Modules and variables
import random
import sys
rock = 1
paper = 2
scissors = 3
error_count = 0
#Program Control
while True:
    user_imput = input("Press 1 for rock, 2 for paper, 3 for scissors:")
    #Validate the input to ensure the program has valid imput
    #Return true is a digit is entered or else false
    if user_imput.isdigit():
        user_imput = int(user_imput)
        if user_imput <=3 and user_imput >=1:
            #Cast to an integer
            # 1,2,3 numbers only
            #Calculate computer's value
            computer_value = random.randrange(1,4,1)
            # Determine the computer's choice
            #Determine winner 
            if user_imput == computer_value:
                print("It's a tie!")
            elif ((user_imput == 1 and computer_value == 3) or (user_imput == 2 and computer_value == 1) or (user_imput == 3 and computer_value == 2)):
                print("You win!")
            else:
                print("Computer wins!")
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
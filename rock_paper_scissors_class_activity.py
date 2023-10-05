#W0478181
#Repository: <https://github.com/W0478181/PROG1700Assignments>
#Import Modules and variables
import random
import sys
rock = 1
paper = 2
scissors = 3
user_choice = None
computer_choice = None
error_count = 0
#Program Control
while True:
    user_imput = input("Press 1 for rock, 2 for paper, 3 for scissors:")
    #Validate the input to ensure the program has valid imput
    #Return true is a digit is entered or else false
    if user_imput.isdigit():
        #Cast to an integer
        user_imput = int(user_imput)
        # 1,2,3 numbers only
        if user_imput <=3 and user_imput >=1:
            #Calculate computer's value
                computer_value = random.randrange(1,4,1)
                # Determine the computer's choice
                if computer_value == 1:
                    computer_choice = "rock"
                elif computer_value == 2:
                    computer_choice = "paper"
                else:
                    computer_choice = "scissors"
                # Determine the user's choice
                if user_imput == 1:
                    user_choice = "rock"
                elif user_imput == 2:
                    user_choice = "paper"
                elif user_imput == 3:
                    user_choice = "scissors"
                else:
                    #If 3 imput errors occur any point while playing user will get error message and code will shut down 
                    print("Please enter a valid number.")
                    error_count += 1
                    if error_count >= 3:
                        print("3 strikes and your out,try again when your ready")
                        sys.exit()
                #User will be shown what they have chosen and what the computer has chose with the "f"
                print(f"You chose {user_choice} and the computer chose {computer_choice}")

                # Determine the winner or tell user there was a tie
                if user_imput == computer_value:
                    print("It's a tie!")
                elif ((user_imput == 1 and computer_value == 3) or (user_imput == 2 and computer_value == 1) or (user_imput == 3 and computer_value == 2)):
                    print("You win!")
                else:
                    print("Computer wins!")
                #User is given option to play again or close the code
                play_again = input("Do you want to play again? (yes/no): ")
                if play_again.lower() == "yes":
                    break
                elif play_again.lower() == "no":
                    sys.exit()
                else: 
                    ValueError
                    print("Please enter a valid response.")
                    error_count += 1
                    if error_count >= 3:
                        print("3 strikes and your out,try again when your ready")
                        sys.exit()
        else:
            print("Please enter a valid number (1 for rock, 2 for paper, 3 for scissors).")
            error_count += 1
            if error_count >= 3:
                print("3 strikes and your out,try again when your ready")
                sys.exit()
    else:
        print("Please enter a valid number (1 for rock, 2 for paper, 3 for scissors).")
        error_count += 1
        if error_count >= 3:
            print("3 strikes and your out,try again when your ready")
            sys.exit()
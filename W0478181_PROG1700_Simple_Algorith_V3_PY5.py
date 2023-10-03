#Aiden Connolly
#W0478181 
#Prog1700 
#Project:Simple Algorithm
#Sept26,2023 
#V.4
# Programming Language: Python 3
#License: Creative Commons
# #Repository: <https://github.com/W0478181/PROG1700Assignments>
import datetime
import sys
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
age = None
month = None
year_of_birth = None
yes = "yes"
no = "no"
error_count = 0
#This is a function to calculate someones birth year
#Made some jokes to keep people entertained
#Users have 3 attempts to enter proper values or else the algorih will quit
def Birth_year_finder():
    global error_count
    while True:
        try:
            age=int(input("Please enter age(numbers only),:")) 
            #Must be at least 1 to move forward
            if age <= 0:
                print("Please enter a valid number.")
                error_count += 1
                if error_count >= 3:
                    print("3 strikes and your out,try again when your ready")
                    sys.exit()
            elif age <= 4:
                print("your not old enough yet bucko,Try agin in a few years.")
                error_count += 1
                if error_count >= 3:
                    print("3 strikes and your out,try again when your ready")
                    sys.exit()
                
            else:
                break
        except ValueError:
            print("Use a whole number c'mon")
            error_count += 1
            if error_count >= 3:
                print("3 strikes and your out,try again when your ready")
                sys.exit()
            
#Added this while statement to fix bug because if your birthday hasnt come yet you would get the wrong birth year        
    while True:
        try:
            month=int(input("Please enter what month you were born(month number only),:"))
           #This is to allows only the 12 months in a year and not break the code
            if month <= 0 or month > 12:
                print("Please enter valid number.")
                error_count += 1
                if error_count >= 3:
                    print("3 strikes and your out,try again when your ready")
                    sys.exit()
            
            else:
                break
        
        except ValueError:
            print("Use a whole number c'mon")
            error_count += 1
            if error_count >= 3:
                print("3 strikes and your out,try again when your ready")
                sys.exit()
                    
    #This line is for if the users birth month hasnt come yet it will change the answer to the proper birth year
    if month > current_month:
        year_of_birth = current_year - age - 1
    #Ive added a new loop because i found another flaw in my code so i also factor in if the users birthday has happened if their birth month is the current month
    elif month == current_month:
        
        while True:    
                birthday_happened = input("Has your birthday happened? (yes or no): ").lower()
                if birthday_happened == "yes":
                    year_of_birth = current_year - age
                    break
            
                elif birthday_happened == "no":
                    year_of_birth = current_year - age - 1
                    break
                
                else:
                    print("Please put yes or no")
                    error_count += 1
                    if error_count >= 3:
                        print("3 strikes and your out,try again when your ready")
                        sys.exit()
                    
    else:
        year_of_birth = current_year - age
    #Possible but doubt somebody this old would be alive or able to use python
    if age > 99:
        print("I don't think dinosaurs can use python,but you were born in",(year_of_birth))
    
    else:
        print("You were born in year",(year_of_birth))   

Birth_year_finder()
def Repeat_algorithm():
    global error_count
    while True:
        #coverts users response to lower case so function doesnt break
        repeat=(input("Would you like to try the algorithm again?(yes or no),:" ).lower())
        if repeat == yes:
            Birth_year_finder()
        
        elif repeat == no:
            break
        
        else:
            print("Please put yes or no")
            error_count += 1
            if error_count >= 3:
                print("3 strikes and your out,try again when your ready")
                sys.exit()
               
#Option to Repeat function if user wants
Repeat_algorithm()

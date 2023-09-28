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
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
age = None
month = None
year_of_birth = None
yes = "yes"
no = None
#This is a function to calculate someones birth year
#Made some jokes to keep people entertained
def Birth_year_finder():
    while True:
        try:
            age=int(input("Please enter age(numbers only),:")) 
            #Must be at least 1 to move forward
            if age <= 0:
                print("Please enter a valid number.")
            
            elif age <= 4:
                print("your not old enough yet bucko,Try agin in a few years.")
                continue
            
            else:
                break
        except ValueError:
            print("Use a whole number c'mon")

#Added this while statement to fix bug because if your birthday hasnt come yet you would get the wrong birth year        
    while True:
        try:
            month=int(input("Please enter what month you were born(month number only),:"))
           #This is to allows only the 12 months in a year and not break the code
            if month <= 0 or month > 12:
                print("Please enter valid number.")
                continue
            
            else:
                break
        
        except ValueError:
            print("Use a whole number c'mon")    
    #This line is for if the users birth month hasnt come yet it will change the answer to the proper birth year
    if month > current_month:
        year_of_birth = current_year - age - 1
    
    else:year_of_birth = current_year - age
    #Possible but doubt somebody this old would be alive or able to use python
    if age > 99:
        print("I don't think dinosaurs can use python,but you were born in",(year_of_birth))
    
    else:
        print("You were born in year",(year_of_birth))   

Birth_year_finder()
def Repeat_algorithm():
    while True:
        #conerts users response to lower case so function doesnt break
        repeat=(input("Would you like to try the algorithm again?(yes or no),:" ).lower())
        if repeat == yes:
            Birth_year_finder()

        else:
            break
               
#Option to Repeat function if user wants
Repeat_algorithm()
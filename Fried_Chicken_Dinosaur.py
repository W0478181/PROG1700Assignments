#W0478181
#Repository: <https://github.com/W0478181/PROG1700Assignments>
#Variables
chicken_in_box = 20
days = 0
chicken_eaten_daily = 0
chicken_eaten_ill = 0
while chicken_in_box > 0:
    days += 1
    if days == 1:
        chicken_eaten_daily = 1
        chicken_in_box -= chicken_eaten_daily
        print(f"On day {days} the dinosaur started his new diet of fried chicken, he bought 20 pounds and ate 1. He has {round(chicken_in_box, 2)} pounds left.")
    elif days == 7:
        print(f"On day {days} the dinosaur became ill and didn't eat. He still has {round(chicken_in_box, 2)} pounds of chicken left.")
    else:
        chicken_eaten_daily += 0.05
        chicken_in_box -= chicken_eaten_daily
    if chicken_in_box <= 0:
        chicken_in_box = 0
        print(f"Sadly, on day {days} he ate the last bit of chicken he had left. He has {chicken_in_box} pounds of chicken left.")
        print("He starved to death a few days later.")
    else:
        if days >= 2 and days != 7:
            print(f"On day {days} the dinosaur started eating more chicken because he loves it so much. He has {round(chicken_in_box, 2)} pounds left.")
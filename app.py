#Countdown Timer Python Project -6

import time

#Introduction
print("Welcome to the countdown timer!")
print("Enter the time in seconds, and ill count down for you.\n")

#user se input lena
try:
    total_time = int(input("Enter the count down timer in seconds. "))
except ValueError:
    print("Invalid Input! Please enter a valid number.")
    exit()


# Countdown Logic
while total_time > 0:
    minutes, seconds = divmod(total_time, 60)
    timer = f"{minutes:02d}:{seconds:02d}"
    print(timer, end = "\r")
    time.sleep(1)
    total_time -= 1

    # times ups!
print("Time's ups!")
# 14 Sept 2023:- Countdown Timer in Python:
# First create a function to take time in seconds and print it out in a formatted string. The countdown timer will start at a given time and count down to zero. At each second, it will print out the remaining time. When the timer reaches zero, it will print out a message saying, “Time’s up!.”
import time
b = int(input("Enter the countdown number: "))
while b > 0:
  if b > 0:
    print(b)
    b -= 1
    print(f"Remaining time is: {b}")
    time.sleep(1)
  if b == 0:
    print("Time's up!")

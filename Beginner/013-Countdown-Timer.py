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

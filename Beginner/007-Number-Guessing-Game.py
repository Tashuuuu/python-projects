# Python Number Guessing Game: 
# The basic idea is to have the computer produce a random number between 1 and 100 and then have the user try to guess it.
# If the user guesses correctly, they win! If not, the computer tells them whether their guess was too high or too low, and they get another chance.

import random
a = random.randint(1, 100)
print("Guess the number between 1 and 100")
b = int(input("Guess the number: "))
if a == b:
  print("Congratulations! You won!")
  print(f"The number {a}. Your guess {b}")
else:
  if ((a - b) >= 30):
    print("Your guess is too low")
  elif ((b - a) >= 30):
    print("Your guess is too high")
  elif (0 < (a - b) < 30):
    print("Your guess is low")
  elif (0 < (b - a) < 30):
    print("Your guess is high")
  c = int(input("Guess another number: "))
  if a == c:
    print("Congratulations! You won!")
    print(f"The number {a}. Your 1st guess {b} and 2nd {c}")
  else:
    if ((a - c) >= 20):
      print("Your guess is too low")
    elif ((c - a) >= 20):
      print("Your guess is too high")
    elif (0 < (a - c) < 20):
      print("Your guess is still low")
    elif (0 < (c - a) < 20):
      print("Your guess is still high")
    d = int(input("Guess again: "))
    if a == d:
      print("Congratulations! You won!")
      print(f"The number {a}. Your 1st guess {b}, 2nd {c} and 3rd {d}")
    else:
      if ((a - d) >= 10):
        print("Your guess is too low")
      elif ((d - a) >= 10):
        print("Your guess is too high")
      elif (0 < (a - d) < 10):
        print("Your guess is still low")
      elif (0 < (d - a) < 10):
        print("Your guess is still high")
      e = int(input("Guess again, this is your last chance: "))
      if a == e:
        print("Congratulations! You won!")
      else:
        print("You have lost.")
      print(f"The number {a}. Your 1st guess {b}, 2nd {c}, 3rd {d} and last {e}")

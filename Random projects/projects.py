# 4. Generate Password:
import random
password_len = int(input("Enter the length of password: "))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s, password_len))
print("Password suggestion for you is:", p)



# 5. Number Guessing Game:
import random
a = random.randint(1, 100)
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



# 6. Countdown Timer:
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



# 7. Create Contact Book:
contact = {}
while True:
  a = input("Do you want to add a contact [y/n]: ")
  if a == "y":
    num = input("Enter the number you want to save: ")
    while len(num) != 10:
      print("Please enter 10 digits.")
      num = input("Enter the number you want to save: ")
    num = int(num)
    name = input("Enter the name to save it with: ")
    contact[name] = num
  elif a == "n":
    print("Thank you!")
    break
  else:
    print("Please enter either 'y' or 'n'.")
# The following code is to add, edit, and delete contacts from the contact book.
while True:
  b = input("Enter whether you want to add, edit or delete contact, enter 'n' if nothing: ")
  if b == "add":
    num = input("Enter the number you want to save: ")
    while len(num) != 10:
      print("Please enter 10 digits.")
      num = input("Enter the number you want to save: ")
    num = int(num)
    name = input("Enter the name to save it with: ")
    contact[name] = num
    print("Added!")
  elif b == "edit":
    while True:
      c = input("You want to edit name or number: ")
      if c == "number":
        d = input("Enter the name whose number you want to edit: ")
        e = input("Enter the edited number: ")
        while len(e) != 10:
          print("Please enter 10 digits.")
          e = input("Enter the edited number: ")
        e = int(e)
        contact[d] = e
        print("Edited!")
        break
      elif c == "name":
        f = input("Enter the name you want to edit: ")
        g = input("Enter the edited name: ")
        contact[g] = contact[f]
        del contact[f]
        print("Edited!")
        break
      else:
        print("Please enter either 'name' or 'number'.")
  elif b == "delete":
      h = input("Enter the name of contact that you want to delete: ")
      del contact[h]
      print("Deleted!")
  elif b == "n":
    print(f"Your edited contact list {contact}")
    break
  else:
    print("Please enter either 'add', 'edit', 'delete' or 'n'.")



# 8. Age Calculator:
import time
this_year = int(time.strftime("%Y"))
this_month = int(time.strftime("%m"))
this_day = int(time.strftime("%d"))

a = input("Enter your date of birth (DD/MM/YYYY): ")
age = a.split("/")

born_year = int(age[2])
born_month = int(age[1])
born_day = int(age[0])

def year(son):
  p = this_year - (born_year + 1)
  return p
age_year = year(born_year)

def month(born_month):
  q = (12 - born_month) + (this_month - 1)
  return q
age_month = month(born_month)

def day(born_day):
  if (born_month == 1 or born_month == 3 or born_month == 5 or born_month == 7 or born_month == 8 or born_month == 10 or born_month == 12):
    r =  (31 - born_day) + this_day
    return r
  elif (born_month == 4 or born_month == 6 or born_month == 9 or born_month == 11):
    r =  (30 - born_day) + this_day
    return r
  else:
    r = (28 - born_day) + this_day
    return r
age_day = day(born_day)

if age_day >= 93:
  age_month = age_month + 3
  age_day = age_day - 93
elif age_day >= 62:
  age_month = age_month + 2
  age_day = age_day - 62
elif age_day >= 31:
  age_month = age_month + 1
  age_day = age_day - 31

if age_month >= 36:
  age_year = age_year + 3
  age_month = age_month - 36
elif age_month >= 24:
  age_year = age_year + 2
  age_month = age_month - 24
elif age_month >= 12:
  age_year = age_year + 1
  age_month = age_month - 12

print(f"So your age is {age_year} years {age_month} months and {age_day} days.")



# 9. Hangman Game:
word = "hey"
turns = 5
right_ans = set()
all_ans = ""
print(f"Guess the correct word. It has {len(word)} letters.")
while turns > 0:
  ask = input("Guess a character: ")
  all_ans += ask
  for i in word:
    if i in all_ans:
      print(i, end = " ")
      right_ans.add(i)
    else:
      print("_", end = " ")
  if ask not in word:
    turns = turns - 1
    print("\nWrong guess!")
    print(f"You have {turns} attempts left.")
  if turns == 0:
    break
  if right_ans == (q:=set(word)):
    print(f"\nThe word was \'{word}\'. You guessed it right.")
    print("Yay!\nYou won!")
    break
if right_ans != q:
  print("You lost.")



# 10. Basic Calculator:
print("NOTE: You can only perform calculatons on 4 numbers!!")
def sum(a, b, c = 0, d = 0):
  return a + b + c + d
def sub(a, b, c = 0, d = 0):
  return a - b - c - d
def mul(a, b, c = 1, d = 1):
  return a * b * c * d
def div(a, b, c = 1, d = 1):
  return a / b / c / d
def quit():
  pass
while True:
  print("Choose from \'sum\' for addition (+), \'sub\' for subtraction (-), \'mul\' for multiplication (x), \'div\' for division (/) and \'quit\' to quit.")
  do = eval(input("What do you want to do?: "))
  if (do == sum or do == sub or do == mul or do == div):
    z = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    a = input("Do you want to add more numbers? (y/n): ")
    if a == "y":
      x = int(input("Enter the third number: "))
      a = input("Do you want to add more numbers? (y/n): ")
      if a == "y":
        w = int(input("Enter the fourth number: "))
        print(f"The result of the numbers is {do(z, y, x, w)}")
      elif a == 'n':
        print(f"The result of the numbers is {do(z, y, x)}")
      else:
        print("Please enter either 'y' or 'n'.")
    elif a == 'n':
      print(f"The result of the numbers is {do(z, y)}")
    else:
      print("Please enter either 'y' or 'n'.")
  elif do == quit:
    break
  else:
    print("Please choose only from the mentioned options.")
# Another way to solve it is:
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    if n1 > n2:
        return n1 - n2
    return n2 - n1
def divide(n1, n2):
    if n1 > n2:
        return n1 / n2
    return n2 / n1
def multiply(n1, n2):
    return n1 * n2

operation = {'+': add, '-': subtract, '/': divide, '*': multiply}

continue_choice = 'yes'

while continue_choice == 'yes':
    num1 = int(input("\nEnter the first number: "))
    num2 = int(input("Enter the second number: "))

    for symbol in operation:
        print(symbol, end="  ")
    operation_symbol = input("\n Pick an operation from the line above: ")

    cal = operation[operation_symbol]
    result = cal(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {result}")
    continue_choice = input('\n Do you want to perform another operation? [yes/no] \n')



# 11. Word Counter:
text = input("Enter you text: ")
word = text.split()
print(f"Your given text is \'{text}\'")
print(f"The number of words in your given text is {len(word)}")



# 12. Group Anagrams:
from collections import defaultdict
def group_anagrams(a):
  dfdict = defaultdict(list)
  for i in a:
    sorted_i = " ".join(sorted(i))
    dfdict[sorted_i].append(i)
  return dfdict.values()
words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))



# 13. Find Missing Number:
def missing_num(a):
  b = []
  for i in range(a[-1]):
    if i in a:
      pass
    else:
      b.append(i)
  print("Missing numbers are:", b)
hi = [1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 25]
missing_num(hi)



# 14. Find prime numbers:
num = int(input("Enter the number you want to check: "))
div = 2
if (num == 2 or num == 1):
  print(num, "is a prime number.")
else:
  while num > div:
    if num % div == 0:
      print(num, "is not prime number. Because it is divisible by", div)
      break
    else:
      div = div + 1
  if num == div:
      print(num, "is a prime number.")



# 15. Print all prime numbers till n:
n = int(input("Enter the value of n: "))
num = 3
prime = []
while num < n:
  div = 2
  while div < num:
    if num % div == 0:
      break
    else:
      div = div + 1
    prime.append(num)
    break
  num = num + 1
if (n == 1 or n == 2 or n == 3):
  print(n, "is prime.")
elif (n == 0):
  print("We can't tell whether 0 is prime or not.")
print(f"All the prime numbers till {n} are {prime}")



# 16. BMI calculator:
while True:
  ask_weight = input("Do you know your weight in pound(same as LBS) or kg?: ")

  if ask_weight == "kg":
    kg_weight = float(input("Please enter your weight in kilograms: "))
    break

  elif ask_weight == "pound":
    pound_weight = float(input("Please enter your weight in pounds: "))
    kg_weight = pound_weight * 0.4536
    break

  else:
    print("Please write either \'pound\' or \'kg\'")


while True:
  ask_height = input("Do you know your height in m (meter), cm (centimeter), feet (foot) or inch?: ")

  if ask_height == "m":
    m_height = float(input("Please enter your height in meters: "))
    break

  elif ask_height == "cm":
    cm_height = float(input("Please enter your height in centimeters: "))
    m_height = cm_height * 0.01
    break

  elif ask_height == "inch":
    inch_height = float(input("Please enter your height in inches: "))
    m_height = inch_height * 0.0254
    break

  elif ask_height == "feet":
    feet_height = float(input("Please enter your height in feet: "))
    m_height = feet_height * 0.3048
    break

  else:
    print("Please write either \'m\', \'cm\', \'feet\' or \'inch\'")

BMI = kg_weight / (m_height)**2

print("Your Body mass index (BMI) is", round(BMI, 4))



# 3 Dec 2023: Calculator:
def add(num1, num2):
  return num1 + num2
def multiple(num1, num2):
  return num1 * num2
def divide(num1, num2):
  return num1 / num2
def subtract(num1, num2):
  return num1 - num2
def power(num1, num2):
  return num1 ** num2
def calculator(num1, num2, operator):
  return operator(num1, num2)

calculator(2,4,add)

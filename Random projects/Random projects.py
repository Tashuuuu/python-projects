# Python Program to Generate Password
import random
a = int(input("Enter the length of your password(must be at between 4 to 10): "))
b = "abcdefghijklmnopqrstuvwxyz"
c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d = "123456789"
e = '''`~!@#$%^&*()-_=+[{}]\|;:',<.>/"?'''
if a == 4:
  password = print(f"Your password is {random.choice(b)}{random.choice(c)}{random.choice(d)}{random.choice(e)}")
elif a == 5:
  password = print(f"Your password is {random.choice(b)}{random.choice(c)}{random.choice(d)}{random.choice(e)}{random.choice(b)}")
elif a == 6:
  password = print(f"Your password is {random.choice(b)}{random.choice(c)}{random.choice(d)}{random.choice(e)}{random.choice(b)}{random.choice(c)}")
elif a == 7:
  password = print(f"Your password is {random.choice(b)}{random.choice(c)}{random.choice(d)}{random.choice(e)}{random.choice(b)}{random.choice(c)}{random.choice(d)}")
elif a == 8:
  password = print(f"Your password is {random.choice(b)}{random.choice(c)}{random.choice(d)}{random.choice(e)}{random.choice(b)}{random.choice(c)}{random.choice(d)}{random.choice(e)}")
elif a == 9:
  password = print(f"Your password is {random.choice(b)}{random.choice(c)}{random.choice(d)}{random.choice(e)}{random.choice(b)}{random.choice(c)}{random.choice(d)}{random.choice(e)}{random.choice(b)}")
elif a == 10:
  password = print(f"Your password is {random.choice(b)}{random.choice(c)}{random.choice(d)}{random.choice(e)}{random.choice(b)}{random.choice(c)}{random.choice(d)}{random.choice(e)}{random.choice(b)}{random.choice(c)}")

# OR

import random
passlen = int(input("Enter the length of password: "))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s, passlen))
print("Password suggestion for you is:", p)



# 13 September 2023
# Python Number Guessing Game: 
# The basic idea is to have the computer produce a random number between 1 and 100 and then have the user try to guess it.
# If the user guesses correctly, they win! If not, the computer tells them whether their guess was too high or too low, and they get another chance.
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



# 14 Sept 2023:- Countdown Timer in Python:
# First create a function to take time in seconds and print it out in a formatted string.
# The countdown timer will start at a given time and count down to zero. At each second, it will print out the remaining time.
# When the timer reaches zero, it will print out a message saying, “Time’s up!.”
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



# 16 Sept 2023: Create Contact Book using Python:
# A contact book is a handy tool to keep all your contacts in one place. This python project will allow you to create a contact book
# and add, edit, and delete contacts. In addition, you’ll be able to view all your contacts and their details in one place.
# Answer: Following code is to create a contact book.
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
# Following code is to add, edit and delete contacts from the contact book.
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



# 18 september 2023: Age Calculator:
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



# 19 Sept 2023: Python Hangman Game:
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

# The above code is mine with a few alterations and complete understanding. Create it with scratch but used below code to understand. Took me two days. But I'm happy to finish it.
# OR

name = input("What is your name?")
print ("Hello, " + name, "\nTime to play hangman!")
word = ("secret")
guesses = ""
turns = 10
failed = 0 # Make a counter that starts with zero.
while turns > 0:
  for char in word: # for every character in secret_word
    if char in guesses: # see if the character is in the players guess
      print (char, end=" ") # print then out the character
    else:
      print ("_", end=" ") # if not found, print a dash
      failed += 1 # and increase the failed counter with one
  if failed == 0:
    print ("You won")
    break
  guess = input("guess a character: ") # ask the user to guess a character
  guesses += guess # set the players guess to guesses
  if guess not in word: # if the guess is not found in the secret word
    turns -= 1 # turns counter decreases with 1 (now 9)
    print ("Wrong")
    print ("You have", + turns, 'guesses left.') # how many turns are left
    if turns == 0:
      print ("You Lose!")
print(word)



# 21 Sept 2023: Basic Caluculator:
print("NOTE: You can only perform calculatons on 4 numbers!!")
while True:
  print("Choose from \'add\' for addition (+), \'sub\' for subtraction (-), \'mul\' for multiplication (x), \'div\' for division (/) and \'quit\' to quit.")
  do = input("What do you want to do?: ")
  if do == "add":
    no_one = int(input("Enter the first number: "))
    no_two = int(input("Enter the second number: "))
    a = input("Do you want to add more numbers? (y/n): ")
    if a == "y":
      no_three = int(input("Enter the third number: "))
      a = input("Do you want to add more numbers? (y/n): ")
      if a == "y":
        no_four = int(input("Enter the fourth number: "))
        print(no_one + no_two + no_three + no_four)
      elif a == 'n':
        print(no_one + no_two + no_three)
      else:
        print("Please enter either 'y' or 'n'.")
    elif a == 'n':
      print(no_one + no_two)
    else:
      print("Please enter either 'y' or 'n'.")
  elif do == "sub":
    no_one = int(input("Enter the first number: "))
    no_two = int(input("Enter the second number: "))
    a = input("Do you want to add more numbers? (y/n): ")
    if a == "y":
      no_three = int(input("Enter the third number: "))
      a = input("Do you want to add more numbers? (y/n): ")
      if a == "y":
        no_four = int(input("Enter the fourth number: "))
        print(no_one - no_two - no_three - no_four)
      elif a == 'n':
        print(no_one - no_two - no_three)
      else:
        print("Please enter either 'y' or 'n'.")
    elif a == 'n':
      print(no_one - no_two)
    else:
      print("Please enter either 'y' or 'n'.")
  elif do == "mul":
    no_one = int(input("Enter the first number: "))
    no_two = int(input("Enter the second number: "))
    a = input("Do you want to add more numbers? (y/n): ")
    if a == "y":
      no_three = int(input("Enter the third number: "))
      a = input("Do you want to add more numbers? (y/n): ")
      if a == "y":
        no_four = int(input("Enter the fourth number: "))
        print(no_one * no_two * no_three * no_four)
      elif a == 'n':
        print(no_one * no_two * no_three)
      else:
        print("Please enter either 'y' or 'n'.")
    elif a == 'n':
      print(no_one * no_two)
    else:
      print("Please enter either 'y' or 'n'.")
  elif do == "div":
    no_one = int(input("Enter the first number: "))
    no_two = int(input("Enter the second number: "))
    a = input("Do you want to add more numbers? (y/n): ")
    if a == "y":
      no_three = int(input("Enter the third number: "))
      a = input("Do you want to add more numbers? (y/n): ")
      if a == "y":
        no_four = int(input("Enter the fourth number: "))
        print(no_one / no_two / no_three / no_four)
      elif a == 'n':
        print(no_one / no_two / no_three)
      else:
        print("Please enter either 'y' or 'n'.")
    elif a == 'n':
      print(no_one / no_two)
    else:
      print("Please enter either 'y' or 'n'.")
  elif do == "quit":
    break
  else:
    print("Please choose only from the mentioned options.")

# The above code is written by me in 30 minutes but it was so basic so I write again.
# OR 
# The below code is also written by me in 40 minutes on the same day and I can clearly see myself improving. I'm proud of myself.

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



# 22 Sep 2023: Word Counter: Develop a program that counts the number of words in a given text input.
text = input("Enter you text: ")
word = text.split()
print(f"Your given text is \'{text}\'")
print(f"The number of words in your given text is {len(word)}")



# 23 Sep 2023: Random Name Generator: Create a tool that generates random names by combining syllables or using a predefined list of first and last names.
import random
a = "aeious"
b = random.choice(a)
c = random.choice(a)
d = random.choice(a)
e = random.choice(a)
print(f"Your name is {b+c+d+e}")
# OR
name_list = ["Tashu", "Mohini", "Simi", "Kajal", "Shruti", "Anak"]
h = random.choice(name_list)
print("Your name is", h)



# 23 Sep 2023: Group Anagrams: Anagrams are words formed by rearranging the letters of another word, For example, car and arc, cat and act, etc.
from collections import defaultdict
def group_anagrams(a):
  dfdict = defaultdict(list)
  for i in a:
    sorted_i = " ".join(sorted(i))
    dfdict[sorted_i].append(i)
  return dfdict.values()
words = ["tea", "eat", "bat", "ate", "arc", "car"]
# words = ["pin", "nip", "ant", "tan", "abc", "cab"]
print(group_anagrams(words))



# 24 Sep 2023: Find Missing Number: Given an array containing a range of numbers from 0 to n with a missing number, find the missing number in the input array.
import random
a = []
b = int(input("Please choose the range (number only): "))
c = int(input("Enter how many numbers you want to miss: "))
d = []
for i in range(b):
  a.append(i)
while c > 0:
  a.pop(random.randrange(len(a)))
  c = c - 1
  if c == 0:
    break
for i in range(b):
  if i in a:
    pass
  else:
    d.append(i)
print("The missing values are", d)

# OR I'm proud of my above code! Below one is also done by me!! I'm soo proud of myself. I'm learning slow, but I AM learning!

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



# 25 Sep 2023: Grouping elements of the same indices: Means grouping elements of two or more data structures according to their indices.

lisp = [1, 22, "Hey", "Hello", "Hi", 11, True, (2, 43, 33, 71), ["Yo", False, 42, 90], 98.9, 65.6]
string = []
boolean = []
decimal = []
tuplee = []
lis = []
integer = []
for i in lisp:
  if type(i) == str:
    string.append(i)
  elif type(i) == bool:
    boolean.append(i)
  elif type(i) == float:
    decimal.append(i)
  elif type(i) == tuple:
    tuplee.append(i)
  elif type(i) == list:
    lis.append(i)
  elif type(i) == int:
    integer.append(i)
final = [string, boolean, decimal, tuplee, lis, integer] 
print(final) 

# OR I didn't understand this question so I built what I thought it meant.

inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
outputLists = []
index = 0

for i in range(len(inputLists[0])):
    outputLists.append([])
    for j in range(len(inputLists)):
        outputLists[index].append(inputLists[j][ index])
    index = index + 1
a, b, c = outputLists[0], outputLists[1], outputLists[2]
print(a, b, c)



# 27 sep 2023: Decode: Decode a msg with key = -2. 
q = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
alph = "abcdefghijklmnopqrstruwxyz"
def trans(a):
  let = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20, "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26}
  num = {27 : "a", 28 : "b", 3 : "c", 4 : "d", 5 : "e", 6 : "f", 7 : "g", 8 : "h", 9 : "i", 10 : "j", 11 : "k", 12 : "l", 13 : "m", 14 : "n", 15 : "o", 16 : "p", 17 : "q", 18 : "r", 19 : "s", 20 : "t", 21 : "u", 22 : "v", 23 : "w", 24 : "x", 25 : "y", 26 : "z"}
  numbers = []
  number = []
  output = []
  for i in a:
    if i == " ":
      numbers.append(" ")
    elif i == "." or i == "'" or i == "()":
      numbers.append(i)
    elif i in alph:
      numbers.append(let.get(i))
  for i in numbers:
    if type(i) is str:
      number.append(i)
    elif type(i) is int:
      j = i + 2
      number.append(j)
  for i in number:
    if type(i) is str:
      output.append(i)
    elif type(i) is int:
      output.append(num.get(i))
  def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
  
  print(listToString(output))
trans(q)

# I did it with basic coding and it took me around 2 hours and it can't work for any key. But I'm still happy that I code it. I was super fun and challenging. I'm proud of myself ^^



# 2 Oct 2023: Find prime numbers:
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

# 2 Oct: Print all prime numbers till n:

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

# I know above code is easy but it took me a while to figure out. But I did completely on my own and only my code lines 712, 723-726 are extra otherwise it's all same.
# I'm soooo proud of myself that I learnt write good code ><



# 15 Oct 2023: BMI: kg/m^2

# LBS and pound are same.
# If you know your weight in pound. Please use this
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



# 6 Nov 2023: Fixed y/n problem:
while True:
  playagain =input("Enter either 'yes' or 'no': ").lower()
  if playagain == "yes":
      continue
  while (playagain != "no" and playagain != "yes"): 
      print("Invalid input. Please enter either 'yes' or 'no'.")
      playagain =input("Enter either 'yes' or 'no': ").lower()
      if (playagain == "yes" or playagain == "no"):
        break
  if playagain == "no":
      break

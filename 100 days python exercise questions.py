# Q2. Good morning sir
time = int(input("Enter current time \n"))
if (time > 6 and time < 12):
    print("Good morning sir!")
elif (time > 12 and time < 16):
    print("Good after noon sir!")
elif (time > 16 and time < 20):
    print("Good evening sir!")
else:
    print("Good night sir!")
# OR
import time
timestamp_t = time.strftime("%H: %M: %S")
print(timestamp_t)
timestamp_h = time.strftime("%H")
print(timestamp_h)
timestamp_m = time.strftime("%M")
print(timestamp_m)
timestamp_s = time.strftime("%S")
print(timestamp_s)
timestamp = int(timestamp_h)
if (timestamp > 6 and timestamp < 12):
    print("Good morning sir!")
elif (timestamp > 12 and timestamp < 16):
    print("Good noon sir!")
elif (timestamp > 16 and timestamp < 20):
    print("Good evening sir!")
else:
    print("Good night sir!")



# Q3. Kon banega crorepati
name = input("Please enter your name: ")
print("Hello!", name+ ",\n"+ "The game begins.\n")
print("\nThis question is for 10 rupees.\n\nQ1. What is your age? \n\nOptions are:\na. 10 \t b. 20 \nc. 30 \t d. 40\n")
ans1 = input("Enter your answer:\n")
if ans1=="a":
    print("\nYour answer is correct. \nYou won 10 rupees! \n\nNow proceed to next question.\n")
    print("This question is for 20 rupees.\n\nQ2. Where do you live? \n\nOptions are:\na. Delhi \t b. Kanpur \nc. Guna \t d. Goa\n")
    ans2 = input("Enter your answer:\n")
    if ans2=="b":
        print("\nYour answer is correct. \nYou won 20 rupees! \n\nNow proceed to next question.\n")
        print("This question is for 30 rupees.\n\nQ3. What is 2+2? \n\nOptions are:\na. 0 \t b. 6 \nc. 3 \t d. 4\n")
        ans3 = input("Enter your answer: \n")
        if ans3=="d":
            print("\nYour answer is correct. \nYou won 30 rupees!.\n\nYou won the game congratulation!")
        else:
            print("Your answer was wrong. \nYou lost at 20 rupees.")
    else:
        print("Your answer was wrong. \nYou lost at 10 rupees.")
else:
    print("Your answer was wrong. \nYou lost at 0 rupees.")
# OR
questions = [["What is your age?", "10", '20', "30", "40", 1], ["Where do you live?", "Guna", "Delhi", "Kanpur", "Jammu", 2], ["What is 2+2?", "0", "3", "22", "4", 4]]
levels = [1000, 2000, 3000, 4000]
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question is {question[0]}")
    print(f"Options are a. {question[1]}                    b. {question[2]}")
    print(f"            c. {question[3]}                    d. {question[4]} \n")
    reply = int(input("Enter your answer from (1-4): "))
    if reply==question[-1]:
        print(f"\n Correct answer! You have won Rs. {levels[i]} \n")
    else:
        print("Wrong answer!")
        break 



# Q4. Secret code language
# Write a python program to translate a message into secret code language. Use the rules below to
# translate normal English into secret code language.

# Encoding:
# if the word contains at least three characters, remove the first letter and appent it at the end. Now
#   append three random characters at the starting and at the end.
# else:
#   Simply reverse the string

# Decoding:
# if the word contains less than three characters, reverse it
# else:
#   remove three random characters from start and end. Now remove the last letter and append it
#   to the beginning

# Your program should ask whether you want to code or decode
import random
z = "abcdefghijklmnopqrstuvwxyz"
m = input("Enter your message: ")
c = input("You want to encode or decode the message: ")
msg = m.split()
for a in msg:
  if c == "encode":
    if len(a) >= 3:
      a1 = a[0]
      a = a + a1
      a2 = a[1:]
      a3 = random.choice(z)
      a4 = random.choice(z)
      a5 = random.choice(z)
      a6 = random.choice(z)
      a7 = random.choice(z)
      a8 = random.choice(z)
      p = a3 + a4 + a5 + a2 + a6 + a7 + a8
      print(p)
    else:
      p = a[::-1]
      print(p)
  if c == "decode":
    if len(a) < 3:
      k = a[::-1]
      print(k)
    else:
      c1 = a[3:]
      c2 = c1[:-3]
      c3 = c2[-1]
      c4 = c3 + c2
      k = c4[:-1]
      print(k)



# Q5. Snake or water or gun
# Snake, water and gun is a variation of the children's game "rock-paper-scissors" where players use
# hand gestures to represent a snake, water, or a gun. Gun beats snake, water beats gun and snake beats water.

# Write a python program to create a Snake Water Gun Game using if-else statements.
# Do not create any fancy GUI. Use proper functions to check for win.

# Rules:
# 1. Take the input from user, whether they want snake or water or gun.
# 2. Then computer will choose from snake, water or gun. Automatically, will not be in your control.
print("Options are Snake or Water or Gun.")
player = input("Enter your choice: ")
print(f"You choose {player}.")
z = ["Snake", "Water", "Gun"]
import random
computer = random.choice(z)
print(f"Computer choose {computer}.")
if (player == "Gun" and computer == "Snake"):
    print("You won!")
elif (player == "Water" and computer == "Gun"):
    print("You won!")
elif (player == "Snake" and computer == "Water"):
    print("You won!")
elif (computer == "Gun" and player == "Snake"):
    print("Computer won!")
elif (computer == "Water" and player == "Gun"):
    print("Computer won!")
elif (computer == "Snake" and player == "Water"):
    print("Computer won!")
elif (player == computer): # OR else:
    print("Match draw!")   #        print("Match draw!")



# Q6. Library Management System
# Write a library class with no_of_books and books as two instance variables. Wrtie a program to create a library from
# this Library class and show how you can print all books, add a book and get the number of books using different methods.
# Show that your program doesn't persist the books after the program is stopped!
class Library:
    def __init__(self, no_of_books, books):
        self.no_of_books = int(no_of_books)
        self.books = books
        if self.no_of_books == 1:
            print(f"This library has {self.no_of_books} book and its name is {self.books}.")
        elif self.no_of_books == 0:
            print("This library has no books.")
        else:
            print(f"This library has {self.no_of_books} books and their names are {self.books}.")

a = Library(1, "Atomic habit")


# Q Auto password generator
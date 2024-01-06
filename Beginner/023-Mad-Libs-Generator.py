# Day 2: Mad Libs Generator
# The program will ask users to enter a series of inputs considered a Mad Lib. The input could be anything, an adjective,
# a noun, a pronoun, etc. Once all the inputs are entered, the application will take the data and arrange the inputs into a story 
# template form.
a = input("Enter the first word: ")
b = input("Enter the second word: ")
c = input("Enter the third word: ")
d = input("Enter the forth word: ")
e = input("Enter the fifth word: ")
l = [a, b, c, d, e]
for i in l:
  if (type(i) != str):
    raise ValueError(f"{i} it must be in English, could be any adjective, noun, pronoun, letter, word and so on.")
print(f"Once there was a {a} {b}, she has {d}al powers and she had a {c}, they are loved by their people. \n One day their parents died in the black sea. They carried their parent's teachings and ruled the kingdom peacefully and lovingly. \nAnd they lived a {e}.")

# OR

import random
when = ["A long time ago", "Yesterday", "Last year"]
name = ["Neha", "Ayush", "Pratap"]
place = ["school", "mall", "garage", "hill station"]
did = ["ran", "called the police", "panicked"]
print(f"{random.choice(when)}, {random.choice(name)} went to {random.choice(place)} a man was standing with a gun in his hand, {random.choice(did)} seeing that")

# OR
import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mystery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))

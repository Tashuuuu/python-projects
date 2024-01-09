# Basic Python Program to Generate Password
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

# Intermediate-level Python Program to Generate Password

import random
passlen = int(input("Enter the length of password: "))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(s, passlen))
print("Password suggestion for you is:", password)

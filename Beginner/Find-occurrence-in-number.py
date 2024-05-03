# Find how many times a digit is repeating in a number.

n = input("Enter the number: ")
f = input("Enter the digit you want to find: ")
count = 0

for i in n:
  if (i == f):
    count = count + 1
print(f"{f} is occuring {count} times in {n}")

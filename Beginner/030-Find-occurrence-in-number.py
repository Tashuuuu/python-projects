# Find how many times a digit is repeating in a number.

n = input("Enter the number: ")
f = input("Enter the digit you want to find: ")
count = 0

for i in n:
  if (i == f):
    count = count + 1
print(f"{f} is occurring {count} times in {n}")




# Another way:
n = input("Enter the number: ")
count = 0

while (n > 0):
  rem = n % 10
  if (rem == 6):
    count = count + 1
  n = int(n / 10)
  
print(count)

# Reverse a given number:

n = input("Enter the number: ")
a = []
x = 0

while (x < len(n)):
  a.append(n[-1 - x])
  x = x + 1

for i in a:
  print(i, end="")



# Another way: 
n = int(input("Enter the number: "))
ans = 0

while (n > 0):
  rem = n % 10
  n = int(n / 10)
  ans = ans * 10 + rem

print(ans)

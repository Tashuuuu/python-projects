n = int(input("Enter the value of n: ")) # "n" is the number till when you want to count all the prime numbers, like if n = 10 then all the prime numbers would be 2, 3, 5, and 7.
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

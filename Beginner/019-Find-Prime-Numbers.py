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

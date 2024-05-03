a = 3  # Since the first two Fibonacci numbers are fixed we'll start with the third.
n = int(input("Enter the Fibonacci number that you want to find:))
if (n == 1):
    series = [0]
if (n == 2):
    series = [0, 1]
if (n > 2):
    series = [0, 1]
    while (a <= n):
        x = series[-1]
        y = series[-2]
        series.append(x + y)
        a = a + 1
      
print(f"The series is {series}")
print(f"The {n}th Fibonacci number is {series[-1]}")



# Another way is:
a = 0 # First Fibonacci number
b = 1 # Second Fibonacci number
count = 2
n = int(input("Enter the Fibonacci number that you want to find:))
while (count <= n):
    temp = b
    b = a + b
    a = temp
    count++
print(f"The {n}th Fibonacci number is {b}")

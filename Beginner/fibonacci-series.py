a = 3  # Since the first two elements are fixed we'll start with the third.
n = int(input("Enter the series number that you want to find:))
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
print(f"The {n}th series value is {series[-1]}")

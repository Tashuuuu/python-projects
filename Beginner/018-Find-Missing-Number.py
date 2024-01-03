print("Enter the list below (in 'data'), whose missing number you want to find.")
data = [1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 25]
def missing_num(a):
  b = []
  for i in range(a[-1]):
    if i in a:
      pass
    else:
      b.append(i)
  print("Missing numbers are:", b)

missing_num(data)

import random
z = "abcdefghijklmnopqrstuvwxyz"
m = input("Enter your message: ")
c = input("You want to encode or decode the message: ")
msg = m.split()
for a in msg:
  if c == "encode":
    if len(a) >= 3:
      a1 = a[0]
      a = a + a1
      a2 = a[1:]
      a3 = random.choice(z)
      a4 = random.choice(z)
      a5 = random.choice(z)
      a6 = random.choice(z)
      a7 = random.choice(z)
      a8 = random.choice(z)
      p = a3 + a4 + a5 + a2 + a6 + a7 + a8
      print(p)
    else:
      p = a[::-1]
      print(p)
  if c == "decode":
    if len(a) < 3:
      k = a[::-1]
      print(k)
    else:
      c1 = a[3:]
      c2 = c1[:-3]
      c3 = c2[-1]
      c4 = c3 + c2
      k = c4[:-1]
      print(k)

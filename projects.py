# 1. Secret code langauge:
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



# 2. Stone, paper, scissor:
import random
choices = ['stone', 'paper', 'scissor']
while True:
    computerC = random.choice(choices)
    userC = input('Enter your choice (stone/paper/scissor): ').lower()
    if userC =='exit':
        break
    while userC not in choices:
        print('Please enter a valid choice!!')
        userC = input('enter your choice (stone/paper/scissor): ').lower()
    print('user:', userC)
    print('computer:', computerC)

    if userC == computerC:
        print('Its a tie')
    elif ((userC == 'stone' and computerC == 'scissor')
            or (userC == 'paper' and computerC == 'stone')
            or (userC == 'scissor' and computerC == 'paper')):
        print('You win🤩!')
    else:
        print('Computer win🤖')
            
    playagain =input('Do you want to play again (yes/no): ').lower()
    if playagain == "yes":
        continue
    while (playagain != "no" and playagain != "yes"): 
        print("Invalid input. Please enter either 'yes' or 'no'.")
        playagain =input('Do you want to play again (yes/no):').lower()
        if (playagain == "yes" or playagain == "no"):
            break
    if playagain == "no":
        break
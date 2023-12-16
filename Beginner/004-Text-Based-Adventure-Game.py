if __name__ == "__main__":
  while True:
    print('''Welcome to the Adventure Game!
    As an avid traveler, you have decided to visit the Catacombs of Paris.
    However, during your exploration, you find yourself lost.
    You can choose to walk in multiple directions to find a way out.''')
    name = input("Let's start with your name: ")
    print("Good luck, " +name+ ".")
    introScene()


print('''             
*********************************************************************************************************
It's the scary choices that end up being the most worthwhile.
**********************************************************************************************************\n
''')

print("Are you ready to start your journey, Traveler?")
start = input("Please enter 'yes' or 'no'. ")

if start.lower() == 'yes':
  
  
else:
    print("Your indecision leads you astray. The island's perils claim another adventurer.")

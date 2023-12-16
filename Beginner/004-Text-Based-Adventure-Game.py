if __name__ == "__main__":
  while True:
    print("Welcome to the Adventure Game!")
    print("As an avid traveller, you have decided to visit the Catacombs of Paris.")
    print("However, during your exploration, you find yourself lost.")
    print("You can choose to walk in multiple directions to find a way out.")
    print("Let's start with your name: ")
    name = input()
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

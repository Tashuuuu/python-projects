contact = {}
while True:
  a = input("Do you want to add a contact [y/n]: ")
  if a == "y":
    num = input("Enter the number you want to save: ")
    while len(num) != 10:
      print("Please enter 10 digits.")
      num = input("Enter the number you want to save: ")
    num = int(num)
    name = input("Enter the name to save it with: ")
    contact[name] = num
  elif a == "n":
    print("Thank you!")
    break
  else:
    print("Please enter either 'y' or 'n'.")
    
# The following code is to add, edit, and delete contacts from the contact book.
while True:
  b = input("Enter whether you want to add, edit or delete contact, enter 'n' if nothing: ")
  if b == "add":
    num = input("Enter the number you want to save: ")
    while len(num) != 10:
      print("Please enter 10 digits.")
      num = input("Enter the number you want to save: ")
    num = int(num)
    name = input("Enter the name to save it with: ")
    contact[name] = num
    print("Added!")
  elif b == "edit":
    while True:
      c = input("You want to edit name or number: ")
      if c == "number":
        d = input("Enter the name whose number you want to edit: ")
        e = input("Enter the edited number: ")
        while len(e) != 10:
          print("Please enter 10 digits.")
          e = input("Enter the edited number: ")
        e = int(e)
        contact[d] = e
        print("Edited!")
        break
      elif c == "name":
        f = input("Enter the name you want to edit: ")
        g = input("Enter the edited name: ")
        contact[g] = contact[f]
        del contact[f]
        print("Edited!")
        break
      else:
        print("Please enter either 'name' or 'number'.")
  elif b == "delete":
      h = input("Enter the name of contact that you want to delete: ")
      del contact[h]
      print("Deleted!")
  elif b == "n":
    print(f"Your edited contact list {contact}")
    break
  else:
    print("Please enter either 'add', 'edit', 'delete' or 'n'.")

def sum():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"The sum of {a} and {b} is {a + b}")
    while True:
        ask = input("Want to add again? (y/n) ")
        if (ask == "y"):
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(f"The sum of {a} and {b} is {a + b}")
        elif (ask == "n"):
            break
        else:
            print("Please enter either 'y' or 'n'")

sum()

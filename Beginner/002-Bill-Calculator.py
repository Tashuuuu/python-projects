print("Welcome to the bill calculator")

total_bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? \n"))
no_of_people = float(input("How many people to split the bill? \n"))

tip_money = (total_bill * tip) / 100
bill_per_person = (total_bill + tip_money) / no_of_people

print(f'Each person should pay: ${bill_per_person}')

# Code with function would be like this:
# def split_bill():
#   tip_money = (total_bill * tip) / 100
#   bill_per_person = (total_bill + tip_money) / no_of_people
#   print(f"Each person should pay: ${bill_per_person}")
# split_bill()

# 10. Basic Calculator:
# Intermediate way to solve it is:
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    if n1 > n2:
        return n1 - n2
    return n2 - n1
def divide(n1, n2):
    if n1 > n2:
        return n1 / n2
    return n2 / n1
def multiply(n1, n2):
    return n1 * n2

operation = {'+': add, '-': subtract, '/': divide, '*': multiply}

continue_choice = 'yes'

while continue_choice == 'yes':
    num1 = int(input("\nEnter the first number: "))
    num2 = int(input("Enter the second number: "))

    for symbol in operation:
        print(symbol, end="  ")
    operation_symbol = input("\n Pick an operation from the line above: ")

    cal = operation[operation_symbol]
    result = cal(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {result}")
    continue_choice = input('\n Do you want to perform another operation? [yes/no] \n')




# 16. BMI calculator:
while True:
  ask_weight = input("Do you know your weight in pound(same as LBS) or kg?: ")

  if ask_weight == "kg":
    kg_weight = float(input("Please enter your weight in kilograms: "))
    break

  elif ask_weight == "pound":
    pound_weight = float(input("Please enter your weight in pounds: "))
    kg_weight = pound_weight * 0.4536
    break

  else:
    print("Please write either \'pound\' or \'kg\'")


while True:
  ask_height = input("Do you know your height in m (meter), cm (centimeter), feet (foot) or inch?: ")

  if ask_height == "m":
    m_height = float(input("Please enter your height in meters: "))
    break

  elif ask_height == "cm":
    cm_height = float(input("Please enter your height in centimeters: "))
    m_height = cm_height * 0.01
    break

  elif ask_height == "inch":
    inch_height = float(input("Please enter your height in inches: "))
    m_height = inch_height * 0.0254
    break

  elif ask_height == "feet":
    feet_height = float(input("Please enter your height in feet: "))
    m_height = feet_height * 0.3048
    break

  else:
    print("Please write either \'m\', \'cm\', \'feet\' or \'inch\'")

BMI = kg_weight / (m_height)**2

print("Your Body mass index (BMI) is", round(BMI, 4))



# 3 Dec 2023: Calculator:
def add(num1, num2):
  return num1 + num2
def multiple(num1, num2):
  return num1 * num2
def divide(num1, num2):
  return num1 / num2
def subtract(num1, num2):
  return num1 - num2
def power(num1, num2):
  return num1 ** num2
def calculator(num1, num2, operator):
  return operator(num1, num2)

calculator(2,4,add)

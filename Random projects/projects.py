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

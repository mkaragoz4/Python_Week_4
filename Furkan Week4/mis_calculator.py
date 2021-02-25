'''
Developer: Furkan Sürücü
Purpose of Software: Reinforcement of learned python code and self-improvement
What does program do?: As a user, I want to use a program which can calculate basic mathematical operations.
So that I can add, subtract, multiply or divide my inputs.
'''

import adding_numbers, subtracting_numbers, multiplying_numbers, dividing_numbers
from math import ceil

def calculator():
    while True:
        try:
            print("1. Add\n"
                  "2. Substract\n"
                  "3. Multiply\n"
                  "4. Divide\n")

            choice = int(input("Select one of the operations: "))
            if choice != 1 and choice != 2 and choice != 3 and choice != 4:
                print("Please enter a valid input")
                calculator()

            num1 = float(input("Enter the first number:"))
            num2 = float(input("Enter the second number:"))
            if choice == 1:
                result = adding_numbers.add(num1, num2)
                print(num1, '+', num2, '=', ceil(result))

            elif choice == 2:
                result = subtracting_numbers.subtract(num1, num2)
                print(num1, '-', num2, '=', ceil(result))

            elif choice == 3:
                result = multiplying_numbers.multiply(num1, num2)
                print(num1, '*', num2, '=', ceil(result))

            elif choice == 4:
                result = dividing_numbers.divide(num1, num2)
                print(num1, '/', num2, '=', ceil(result))

            while True:
                answer = input("Would you like the calculate again?")
                answer = answer.lower()
                if answer == 'y':
                    calculator()
                elif answer == 'n':
                    return print("take care")
        except:
            print("Please enter a valid input")


calculator()
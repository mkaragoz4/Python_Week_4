import addition
import subtraction
import multiplication
import division
import sys
from math import ceil

while True:
    try:
        operand = input("Please make your selection!\n"
                        "insert 'a' for addition: \n"
                        "insert 's' for subtraction: \n"
                        "insert 'm' for multiplication: \n"
                        "insert 'd' for division: \n")

        b = operand == 'a' or operand == 's' or operand == 'm' or operand == 'd'

        if not b:
            print("Please make a correct selection in 'a', 's', 'm' or 'd'")
            continue

        num1 = int(input("Please write your first number: "))
        num2 = int(input("Please write your second number: "))
        if operand == 'a':
            result = addition.add(num1, num2)
            print("The addition result is ", ceil(result))
        elif operand == 's':
            result = subtraction.subst(num1, num2)
            print("The subtraction result is ", ceil(result))
        elif operand == 'm':
            result = multiplication.mult(num1, num2)
            print("The multiplication result is ", ceil(result))
        elif operand == 'd':
            result = division.div(num1, num2)
            print("The division result is ", ceil(result))


        while True:
            cont = input("Do you want to continue calculating process (y/n): ")
            if cont == 'y':
                comment="go to first loop"
                break
            elif cont == 'n':
                comment="break all loop"
                break
            else:
                print("Please make a correct selection in 'y' or 'n'")
                continue
        if comment == "go to first loop":
            continue
        elif comment == "break all loop":
            break
    except:
        print("OPPS! This is a ", str(sys.exc_info()[0])[7:-1])
        print("Please make a valid selection!")

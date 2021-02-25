import math
import math2
while True:
    seç = input("Operation to perform:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nEnter choice:")
    try:
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        if seç == '1':
            print(math2.addition(n1,n2))
        elif seç == '2':
            print(math2.subtraction(n1, n2))

        elif seç == '3':
            print(math2.ultiplication(n1, n2))

        elif seç == '4':
            print(math2.division(n1, n2))
    except:
        print("something wrong!!!")
    c = input("do you want to continue (Y/N)").upper()
    if c == "Y":
        continue
    elif c =="N":
        break
    else:
        print("enter Y/N ")
        print("something wrong!!!")
        c = input("do you want to continue (Y/N)").upper()
        if c == "Y":
            continue
        elif c == "N":
            break
        else:
            break
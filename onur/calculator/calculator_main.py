import calculator_addition as ad,calculator_subtution as subs
import calculator_multiply as mult,calculator_division as div

control=True

while control:
    print("=========================================================")
    print("=====================MIS CALCULATOR======================")
    print("=========================================================")
    print("\t\t1 for addition\n\t\t2 for substution\n\t\t3 for multiplication\n\t\t4 for division")
    print("=========================================================")
    operation = input("Please choose an operatoin :")

    if operation=="1":
        ad.addition()
    elif operation=="2":
        subs.substution()
    elif operation=="3":
        mult.multiply()
    elif operation=="4":
        div.division()

    else:
        print("Check your choice!!")
        pass
    while True:
        try:
             operation2=input("Do you want to continue? (Y/N) :")
             if operation2 == "N":
                 print("Bye Bye !")
                 control=False
                 break
             elif operation2=="Y":
                 break
             elif operation2 !="Y" or operation2 !="N":
                 raise Exception("Are you kidding with me!")
        except Exception as ex:
             print (ex)


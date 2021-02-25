def substution():
    try:
        a= (input("Enter first  integer: "))
        b= (input("Enter second integer: "))
        if a == '' or b == '':
            raise Exception("You have to enter a value")

        elif int(a)<= 0 or int(b) <= 0:
            raise Exception("It cant be less than 1")
    except ValueError:
        print("Your input`s type should be integer")
    except Exception as excp:
        print(excp)
    else:
       return print("Additon of",a,"and" ,b, "=", int(a)-int(b))
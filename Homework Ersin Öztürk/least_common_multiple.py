from math import gcd


def lcm_func(a, b, c, d):
    lcm1 = int((a * b) / gcd(a,b))
    lcm2 = int((c * d) / gcd(c,d))
    lcm = int((lcm1*lcm2) / gcd(lcm1,lcm2))
    return lcm

while(True):
    try:
        first=int(input("Please insert the first number: "))
        second=int(input("Please insert the second number: "))
        third=int(input("Please insert the third number: "))
        fourth=int(input("Please insert the fourth number: "))
        lcm=lcm_func(first,second,third,fourth)
        print("The LCM of four number is: ", lcm)
        break
    except:
        print("OPPPS!, Please insert an integer number!!!")


#This program asks user to enter the four numbers.
#Uses try/except blocks to verify input entries and warn the user for None input or non numerical inputs
#Calculates the least common multiple (L.C.M.) of four numbers with gcd function in module of math

from math import gcd

numbers=[]
while len(numbers)<=3:

   try:
       value=(input("Please enter an integer: "))
       if value=='':
           raise Exception("You have to enter a value")

       elif int(value)<=0:
           raise Exception("It cant be less than 1")
   except ValueError:
       print("Your input`s type should be integer")
   except Exception as excp:
       print(excp)
   else:
        numbers.append(int(value))

lcm = numbers[0]

for i in numbers[1:]:
    lcm = lcm * i // gcd(lcm, i)

print("LCM of",numbers, "is:", lcm)












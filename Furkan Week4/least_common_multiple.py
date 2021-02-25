'''
Developer: Furkan Sürücü
Purpose of Software: Reinforcement of learned python code and self-improvement
What does program do?: As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers.
So that I can find the least common multiple (L.C.M.) of my inputs.
'''
from math import gcd
def lcm():
    numbers = []

    while len(numbers) !=4 :
        try:
            x = int(input("Enter a positive number:"))
            if x <= 0:
                raise ValueError("That is not a positive number!")
            else:
                pass
        except ValueError as error:
            print(error)
        else:
            numbers.append(x)
    lcm = numbers[0]
    for i in numbers[1:]:
        lcm = lcm*i//gcd(lcm,i)
    return print("The least common of",numbers[0],numbers[1],
                 numbers[2],numbers[3],"is:",lcm)
lcm()

'''maximum_number = max(numbers)
    while True:
        if maximum_number % numbers[0] == 0 and maximum_number % numbers[1] == 0\
                and maximum_number % numbers[2] == 0 and maximum_number % numbers[3] == 0:
            lcm = maximum_number
            break
        maximum_number +=1
    return print("The least common of",numbers[0],numbers[1],
                 numbers[2],numbers[3],"is:",maximum_number)
lcm()'''

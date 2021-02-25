import math
n = []
while True:
    try:

        for i in range(1,5):
            n1 = int(input(f"Enter number {i} : "))
            n.append(n1)

        l= math.lcm(n[0], n[1], n[2], n[3])

        print(f"the lcm is {l}")
        break

    except :
        print("!!!enter a number!!!")
        continue
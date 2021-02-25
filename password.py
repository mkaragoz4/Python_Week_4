a = ("a b c d e f g h i j k l m n o p r s t u v w y z").split(" ")
b = ("A B C D E F G H I J K L M N O P R S T U V W Y Z").split(" ")
c = ("1 2 3 4 5 6 7 8 9").split(" ")
d = ("# _ _ , + / =").split(" ")
e = (". * ! _ .").split(" ")
from random import choice
password = ""
for i in range(2):
    password += choice(b)
for i in range(1):
    password += choice(d)
for i in  range(4):
    password += choice(a)
for i in range(2):
    password += choice(c)
for i in range(1):
    password += choice(e)
print(password)
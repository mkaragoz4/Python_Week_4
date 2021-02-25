#Random Password generator
#This function Generates 6 character long string :
# which include 2 special char, 2 Upper Case Letter and 2 Integer

from random import choices as ch,randint as ri, shuffle as sh
from tkinter import *

UCL_seq=['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','R','S','T','W','Y','Z']
SC_seq=['!','@','#','$','%','^','&','*','.','-']

def password_generator():
    password =[]
    password.extend((ch(UCL_seq,k=3)))
    password.extend((ch(SC_seq,k=3)))
    for i in range(4) :password.extend(str(ri(0, 9)))
    sh(password)
    return (' '.join(password))

def click():
    text=password_generator()
    label=Label(text=text)
    label.place(x=60,y=50)

#Program starts here

window= Tk()
window.title("Password  Generator")
window.configure(background="black")
window.geometry("220x100")

label=Label(window, text="")
label.place(x=70,y=50)

button=Button(window,text="Hit to Generate",command=click)
button.place(x=65,y=10)

window.mainloop()








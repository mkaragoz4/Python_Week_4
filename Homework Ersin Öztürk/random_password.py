import random
import string
import tkinter as tk



def random_key():
    key = random.sample(string.digits, 2) +\
          random.sample(string.punctuation[0:14], 2) + \
          random.sample(string.ascii_uppercase, 2) + \
          random.sample(string.printable[0:76], 4)
    print(key)
    random.shuffle(key)
    print(key)
    str = ''
    for i in key:
        str += i
    print(str)
    label.config(text=str)
    #return str


window = tk.Tk()

window.title("Random Password")
window.geometry("600x300")


key_application = tk.Frame(window)
key_application.grid()


# label
label_txt = tk.Label(key_application, text="Password:", font="arial 15 bold")
label_txt.grid(padx=110, pady=10)


# label
label = tk.Label(key_application, text="Please push the botton to generate a password", font="arial 12")
label.grid(padx=110, pady=20)


# button
button1 = tk.Button(key_application, text=" GENERATE ", width=50, height=5, command=random_key)
button1.grid(padx=110, pady=40)

window.mainloop()

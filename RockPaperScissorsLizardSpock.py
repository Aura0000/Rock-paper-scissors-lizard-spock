from tkinter import *
import random
import tkinter as tk
import sys


class PrintLogger:  # crearea unei ferestre ca obiect

    def __init__(self, textbox):  # pass reference to text widget
        self.textbox = textbox  # keep ref

    def write(self, text):
        self.textbox.insert(tk.END, text)  # write text to textbox
        # could also scroll to end of textbox here to make sure always visible

    def flush(self):  # needed for file like object
        pass


def NewFile():
    print("Let's play!!!")


def About():
    print("Game Instructions: \n")
    print("Scissors cuts Paper ")
    print("Paper covers Rock")
    print("Rock crushes Lizard")
    print("Lizard poisons Spock")
    print("Spock smashes Scissors")
    print("Scissors decapitates Lizard")
    print("Lizard eats Paper")
    print("Paper disproves Spock")
    print("Spock vaporizes Rock")
    print("Rock crushes Scissors")
    print()


# meniu
root = tk.Tk()
Label(root, text="Rock Paper Scissor Lizard Spock", font="normal 20 bold", fg="red").pack(pady=20)
t = tk.Text()
t.pack()
# create instance of file like object
pl = PrintLogger(t)

# replace sys.stdout with our object
sys.stdout = pl

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=About)

# dimensiune pagina start
root.geometry("700x700")

# titlul
root.title("Rock Paper Scissor Lizard Spock Game")
root.configure(background="gray")
computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor",
    "3": "Lizard",
    "4": "Spock"
}


# Resetare butoane
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    b4["state"] = "active"
    b5["state"] = "active"
    l1.config(text="Player")
    l2.config(text="Computer")
    l3.config(text="")


# Dezactivare butoane
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
    b4["state"] = "disable"
    b5["state"] = "disable"


# cand jucatorul selecteaza rock
def isrock():
    c_v = computer_value[str(random.randint(0, 4))]
    if c_v == "Rock":
        match_result = " Equal Match "
    elif c_v == "Scissor":
        match_result = "Player Win"
    elif c_v == "Lizard":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l3.config(text=match_result)
    l1.config(text="Rock ")
    l2.config(text=c_v)
    button_disable()


# cand jucatorul selecteaza paper
def ispaper():
    c_v = computer_value[str(random.randint(0, 4))]
    if c_v == "Paper":
        match_result = "Equal Match"
    elif c_v == "Rock":
        match_result = " Player Win"
    elif c_v == "Spock":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l3.config(text=match_result)
    l1.config(text="Paper ")
    l2.config(text=c_v)
    button_disable()


# cand jucatorul selecteaza scissor
def isscissor():
    c_v = computer_value[str(random.randint(0, 4))]
    if c_v == "Scissor":
        match_result = "Equal Match"
    elif c_v == "Paper":
        match_result = "Player Win"
    elif c_v == "Lizard":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l3.config(text=match_result)
    l1.config(text="Scissor")
    l2.config(text=c_v)
    button_disable()


# cand jucatorul selecteaza lizard
def islizard():
    c_v = computer_value[str(random.randint(0, 4))]
    if c_v == "Lizard":
        match_result = "Equal Match"
    elif c_v == "Paper":
        match_result = "Player Win"
    elif c_v == "Spock":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l3.config(text=match_result)
    l1.config(text="Lizard")
    l2.config(text=c_v)
    button_disable()


# cand jucatorul selecteaza spock
def isspock():
    c_v = computer_value[str(random.randint(0, 4))]
    if c_v == "Spock":
        match_result = "Equal Match"
    elif c_v == "Scissor":
        match_result = "Player Win"
    elif c_v == "Rock":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l3.config(text=match_result)
    l1.config(text="Spock")
    l2.config(text=c_v)
    button_disable()


# texte ,cadre si butoane


frame = Frame(root)
frame.pack()

l1 = Label(frame, text="Player     ", font=10)

l4 = Label(frame, text="   VS   ", font="normal 10 bold")

l2 = Label(frame, text="     Computer", font=10)

l1.pack(side=LEFT)
l4.pack(side=LEFT)
l2.pack()

l3 = Label(root, text=" ", font="normal 25 bold", bg="white", width=15, borderwidth=2, relief="solid")
l3.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock", font=20, width=10, command=isrock)

b2 = Button(frame1, text="Paper ", font=20, width=10, command=ispaper)

b3 = Button(frame1, text="Scissor", font=20, width=10, command=isscissor)

b4 = Button(frame1, text="Lizard", font=20, width=10, command=islizard)

b5 = Button(frame1, text="Spock", font=20, width=10, command=isspock)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(side=LEFT, padx=10)
b4.pack(side=LEFT, padx=10)
b5.pack(padx=10)

Button(root, text="Reset Game", font=10, fg="red", bg="white", command=reset_game).pack(pady=20)

# Executare

root.mainloop()

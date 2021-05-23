import tkinter as tk
import sys


class PrintLogger():  # create file like object

    def __init__(self, textbox):  # pass reference to text widget
        self.textbox = textbox  # keep ref

    def write(self, text):
        self.textbox.insert(tk.END, text)  # write text to textbox
        # could also scroll to end of textbox here to make sure always visible

    def flush(self):  # needed for file like object
        pass


if __name__ == '__main__':
    def do_something():

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




    root = tk.Tk()
    t = tk.Text()
    t.pack()
    # create instance of file like object
    pl = PrintLogger(t)

    # replace sys.stdout with our object
    sys.stdout = pl


    root.mainloop()

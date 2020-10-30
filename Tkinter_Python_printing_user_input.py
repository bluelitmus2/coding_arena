import tkinter as tk
from tkinter import simpledialog
from tkinter import *

class MyDialog(simpledialog.Dialog):

    def body(self, master):

        Label(master, text="First:").grid(row=0)
        Label(master, text="Second:").grid(row=1)
        Label(master, text="Third:").grid(row=2)
        Label(master, text="Fourth:").grid(row=3)

        self.e1 = Entry(master)
        self.e2 = Entry(master)
        self.e3 = Entry(master)
        self.e4 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)

        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        second = self.e2.get()
        third = self.e3.get()
        fourth =  self.e4.get()


root = tk.Tk()
root.withdraw()
d = MyDialog(root)
print (root)

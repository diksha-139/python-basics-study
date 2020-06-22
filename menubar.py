from tkinter import *
root = Tk()
def display():
    print("hello")
menubar=Menu(root)
menubar.add_cascade(label="New", command=display)
menubar.add_cascade(label="Quit", command=root.quit)
root.config(menu=menubar)
root.mainloop()
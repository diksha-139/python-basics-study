from tkinter import *
import tkinter.messagebox
window = Tk()
window.title("gui tkinter")
label1 = Label(window, text="hello world")
label1.pack()


def fun():
    tkinter.messagebox.showinfo( "Hello", "Red Button clicked" )

b1 = Button( window, text="Red", command=fun, activeforeground="red", activebackground="pink", pady=10 )

b2 = Button( window, text="Blue", activeforeground="blue", activebackground="pink", pady=10 )

b3 = Button( window, text="Green", activeforeground="green", activebackground="pink", pady=10 )

b4 = Button( window, text="Yellow", activeforeground="yellow", activebackground="pink", pady=10 )

b1.pack( side=LEFT )

b2.pack( side=RIGHT )

b3.pack( side=TOP )

b4.pack( side=BOTTOM )

window.geometry("300x300")
window.mainloop()
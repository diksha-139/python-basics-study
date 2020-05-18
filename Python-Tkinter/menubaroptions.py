from tkinter import *

root=Tk()
root.title("menubar program")


def donothing():
    filewin=Toplevel(root)
    filewin.title("nothing")
    button=Button(filewin,text="do nothing")
    button.pack()


menubar=Menu(root)


filemenu=Menu(menubar,tearoff=0)

menubar.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="New",command=donothing)
filemenu.add_command(label="Open",command=donothing)
filemenu.add_command(label="Save",command=donothing)
filemenu.add_command(label="Save As",command=donothing)
filemenu.add_command(label="Close",command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)

editmenu=Menu(menubar,tearoff=0)

menubar.add_cascade(label="Edit",menu=editmenu)

editmenu.add_command(label="Undo",command=donothing)
editmenu.add_separator()

editmenu.add_command(label="Cut",command=donothing)
editmenu.add_command(label="Copy",command=donothing)
editmenu.add_command(label="Paste",command=donothing)
editmenu.add_command(label="Select All",command=donothing)
editmenu.add_command(label="Delete",command=donothing)

helpmenu=Menu(menubar,tearoff=0)

menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="Help Index",command=donothing)
helpmenu.add_command(label="About",command=donothing)


root.config(menu=menubar)

root.mainloop()









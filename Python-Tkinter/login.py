from tkinter import *
data =Tk()

data.title("login page")

label1=Label(data,text="Username:")

label2=Label(data,text="Password:")


e1=Entry(data)

e2=Entry(data)

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
button=Button(data,text="login")
button.grid(row=2,column=0)

data.geometry("350x350")

data.mainloop()
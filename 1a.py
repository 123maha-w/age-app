from tkinter import *

root = Tk()
root.title('age App')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg="#d0efff")
 
lbl1 = Label(frame, text = "Full Name", bg="#3895D3", fg='white', width=12)
lbl2 = Label(frame, text = "date", bg="#3895D3", fg='white', width=12)
lbl3 = Label(frame, text = "month", bg="#3895D3", fg='white', width=12)
lbl4 = Label(frame, text = "year", bg="#3895D3", fg='white', width=12)

name_entry = Entry(frame)
date_entry = Entry(frame)
month_entry = Entry(frame)
year_entry = Entry(frame)

def display():
	name = name_entry.get()
	greet = "Hey "+name
	message =  "\nwe hope you have a good day!"
	textbox.insert(END, greet)
	textbox.insert(END, message)

textbox = Text(bg="#BEBEBE", fg="black")

btn = Button(text = "ok", command=display, bg="red")

frame.place(x=20,y=0)
lbl1.place(x=20, y=80)
name_entry.place(x=150, y=80)

lbl2.place(x=20, y=80)
date_entry.place(x=150, y=80)

lbl3.place(x=20, y=140)
month_entry.place(x=150, y=140)

lbl4.place(x=20, y=20)
year_entry.place(x=150, y=20)

btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()
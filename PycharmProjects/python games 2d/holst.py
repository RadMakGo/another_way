from tkinter import *


def circle():
    c.create_oval(x, y, x + 30, y + 30, fill="yellow", outline='black')


def square():
    c.create_rectangle(x, y, x + 30, y + 30, fill="black", outline='gold')


def triangle():
    c.create_polygon(x, y, x - 15, y + 30, x + 15, y + 30, fill="red", outline='black')


def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)


root = Tk()

c = Canvas(width=1000, height=1000, bg='light blue')
c.pack()
menu = Menu(tearoff=0)
menu.add_command(label='Circle', command=circle)
menu.add_command(label='Square', command=square)
menu.add_command(label='Triangle', command=triangle)

x = 0
y = 0
c.bind('<Button-3>', popup)
root.mainloop()

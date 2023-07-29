from tkinter import *

root = Tk()

entry = Entry(root,width=20)
entry.grid(row=0,column=0)
button = Button(root, text='Преоброзовать')
button.grid(row=1,column=0)
label = Label(root, bg='black', fg='white',width=20)
label.grid()
def strTosortlist(event):
    s = entry.get()
    s = s.split()
    s.sort()
    label['text'] = ' '.join(s)
button.bind('<Button-1>',strTosortlist)

root.mainloop()

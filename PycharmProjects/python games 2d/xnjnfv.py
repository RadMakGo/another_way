from tkinter import *
from datetime import *
temp = 0
after_id =''
def tick():
    global temp, after_id
    after_id = root.after(1000,tick)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    label1.configure(text=str(f_temp))
    temp += 1

def start():
    btn1.grid_forget()

    btn2.grid(row=1, columnspan=2, sticky='ew')
    tick()
def stop():
    btn2.grid_forget()
    btn3.grid(row=1,column=0, sticky='ew')
    btn4.grid(row=1, column=1, sticky='ew')
    root.after_cancel(after_id)
def reset():
    global temp
    temp = 0
    label1.configure(text="00:00")
    btn3.grid_forget()
    btn4.grid_forget()
    btn2.grid_forget()
    btn1.grid_forget()
    btn1.grid(row=1, columnspan=2, sticky='ew')
def continue_sec():
    btn3.grid_forget()
    btn4.grid_forget()
    btn2.grid_forget()
    btn2.grid(row=1,columnspan=2, sticky='ew')
    tick()




root = Tk()
root.title("stopwatch")
label1 = Label(root, width = 5, font=('Ubuntu', 100), text="00:00")
label1.grid(row=0, columnspan=2, sticky='ew')

btn1 = Button(root, text='start', font=('Ubuntu', 30),command=start)
btn1.grid(row=1,columnspan=2, sticky='ew')


btn2 = Button(root, text='stop', font=("Ubuntu", 30), command=stop)

btn3 = Button(root, text='continue', font=('Ubuntu', 30), command=continue_sec)

btn4 = Button(root, text='reset', font=('Ubuntu', 30), command=reset)







root.mainloop()
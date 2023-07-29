from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random, os

def main():
    global logiN, passW
    logiN = 'my login'
    passW = 'my password'

    root = Tk()
    log_pass(root)
    root.mainloop()


def log_pass(window):
    login = Entry(window)
    login.grid(row=0, column=0)

    password = Entry(window)
    password.grid(row=1, column=0)

    check_button = Button(window, text="enter", command=lambda: get_key(login.get(),password.get()))
    check_button.grid(row=2, column=0)

    forget_btn = Button(window, text='do u forgot login/password?', command=lambda: forgetpass())
    forget_btn.grid(row=3,column=0)
def forgetpass():
    forget_sc = Toplevel()
    secret_question = ttk.Combobox(forget_sc, values=['hwo is best programmer?', 'users name?', 'best friends name'])
    secret_question.grid(row=0, column=0)

    secret_answer = Entry(forget_sc)
    secret_answer.grid(row=1, column=0)

    check_btn = Button(forget_sc, text="check", command=lambda: answer(forget_sc,secret_question.get(), secret_answer.get()))
    check_btn.grid(row=2,column=0)

    def answer(window, quest, ans):
        dict_quest ={'hwo is best programmer?': "you",'users name?': 'Tim','best friends name' : 'Kirill'}
        if dict_quest[quest] == ans:
            window.destroy()
            new_log_pass_window = Tk()


            new_log = Entry(new_log_pass_window)
            new_log.grid(row=0,column=0)

            new_pass = Entry(new_log_pass_window)
            new_pass.grid(row=1,column=0)

            new_btn = Button(new_log_pass_window, text='new login and password', command=lambda: new_acc(new_log_pass_window,new_log.get(),new_pass.get()))
            new_btn.grid(row=2,column=0)
            new_log_pass_window.mainloop()

    def new_acc(window,login,password):
        window.destroy()
        global logiN, passW
        logiN = login
        passW = password
    forget_sc.mainloop()


def get_key(login, password):
    if login == logiN and password == passW:
        print('here your daily meme')
        mem_window()
    else:
        print('passwordisincorect')
def mem_window():
    mem_sc = Toplevel()
    directory = os.listdir('memes')
    rand_img = random.choice(directory)
    img = Image.open("memes/" + rand_img)
    img = ImageTk.PhotoImage(img)
    picture = Label(mem_sc, image=img)
    picture.grid(row=0, column=0)
    mem_sc.resizable(height=None, width=None)

    mem_sc.mainloop()
if __name__ == '__main__':
    main()

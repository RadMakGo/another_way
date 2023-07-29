from tkinter import *
import random

class Main(Frame):
    def __init__(self,root):
        super(Main,self).__init__(root)
        self.startUI()
    def startUI(self):
        self.lbl = Label(root, text='Start of game', bg='#20B2AA',
                         font=("Times New Roman", 21, "bold"))
        self.lbl.place(x=150,y=25)
        btn1 = Button(root, text='rock', font=('Times New Roman', 15),
                      command=lambda x=1: self.btn_click(x))
        btn2 = Button(root, text='scissors', font=('Times New Roman', 15),
                      command=lambda x=2: self.btn_click(x))
        btn3 = Button(root, text='paper', font=('Times New Roman', 15),
                      command=lambda x=3: self.btn_click(x))
        btn1.place(x=10,y=100, width=120, height=50)
        btn2.place(x=155,y=100, width=120, height=50)
        btn3.place(x=300,y=100, width=120, height=50)
        self.win = self.drow = self.lose = 0
        self.lb12 = Label(root, justify='left',font=('Times New Roman', 13),
                           text =f'''Wins: {self.win}
losses: {self.lose}
draw: {self.drow}''',
                           bg='#20B2AA')
        self.lb12.place(x=5,y=5)
    def btn_click(self, choise):
        comp_choise = random.randint(1,3)
        if choise == comp_choise:
            self.drow += 1
            self.lbl.configure(text='draw')
        elif choise == 1 and comp_choise == 2 or choise == 2 and comp_choise == 3 or choise == 3 and comp_choise == 1:
            self.win += 1
            self.lbl.configure(text='win')
        else:
            self.lose += 1
            self.lbl.configure(text='losse')
        self.lb12.configure(text=f'''wins: {self.win}
losses: {self.lose}
draw: {self.drow}''')



if __name__ == '__main__':
    root = Tk()
    root.geometry("430x160+200+200")
    root.title("rock, paper, scissors")
    root.resizable(False,False)
    root['bg'] = '#20B2AA'
    app = Main(root)
    app.pack()
    root.mainloop()

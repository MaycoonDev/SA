from tkinter import *
import os

pastaapp= os.path.dirname(__file__)

class cadastro():
    def __init__(self):
        self.app2 = Toplevel()
        self.app2.title('teste')
        self.app2.geometry('300x300')
        self.app2.configure(background = '#f8bdc6')
        self.app2.resizable(False, False)
        self.app2.transient(self.app2)
        self.app2.focus_force()
        self.app2.grab_set()

app = Tk()
app.title('Salão Tiffany')
app.geometry('500x300')
app.configure(background = '#f8bdc6')
img1=PhotoImage(file=pastaapp+"\\form.png")
txt1 = Button(app,text='Cadastra Cliente',font= 'calibri' ,background = '#ffb6c1', foreground = '#000',command= cadastro)
txt1.place(x=10,y=10,width = 150,height = 30)
app.mainloop()

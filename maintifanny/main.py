from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
# import mysql.connector as mysql
#
# def insertcli():
#     nome = nomeinp.get()
#     cpf = cpfinp.get()
#     telefone = telinp.get()
#
#     if nome == '' or cpf == '' or telefone == '':
#         MessageBox.showinfo('Confira os campos','Algum campo esta em falta')
#     else:
#         con = mysql.connect(host='localhost',user='root',password='',database='tiffanytech')
#         cursor = con.cursor()
#         cursor.execute('insert into clientes values(?,?,?)'),(nome,cpf,telefone)
#         cursor.execute('commit')
#         MessageBox.showinfo('Dados inseridos','Cliente cadastrado com sucesso')
#         con.close()


app = Tk()
class aplicativo():
    def __init__(self):
        self.app = app
        self.telamain()
        self.tabel()
        app.mainloop()
    def telamain(self):
        self.app.title('Salão Tiffany')
        self.app.geometry('500x300')
        self.app.configure(background='#f8bdc6')
        self.app.iconbitmap(r'mdchefeicon.ico')

        # Labels/Buttons
        horinzontal = Label(self.app, background='#FFFFFF', foreground='#000')
        vertical = Label(self.app, background='#FFFFFF', foreground='#000')
        verticaltxt = Label(self.app, text='T\n\nI\n\nF\n\nF\n\nA\n\nN\n\nY\n\n\n\nT\n\nE\n\nC\n\nH', background='#FFFFFF',foreground='#000')
        btcad = Button(self.app, text='Form Cliente', font='calibri', background='#ffb6c1', foreground='#000',command=cadastro)
        btcli = Button(self.app, text='Clientes', font='calibri', background='#ffb6c1', foreground='#000', command=clientes)
        btagn = Button(self.app, text='Agendar Horario', font='calibri', background='#ffb6c1', foreground='#000',command=agenda)

        # Configs
        verticaltxt.config(font=("Agency FB", 16, 'bold'))

        # Places
        btcad.place(x=70, y=15, width=150, height=30)
        verticaltxt.place(x=15, y=60, width=35, height=600)
        vertical.place(x=0, y=0, width=70, height=2000)
        horinzontal.place(x=0, y=0, width=2000, height=50)
        btcli.place(x=230, y=15, width=150, height=30)
        btagn.place(x=390, y=15, width=150, height=30)
    def tabel(self):
        self.tableagen = ttk.Treeview(app, height = 30, column = ('col1','col2','col3','col4','col4','col5','col6','col7'))
        self.tableagen.heading('#0', text='')
        self.tableagen.heading('#1', text='Nome do Cliente')
        self.tableagen.heading('#2', text='Serviço')
        self.tableagen.heading('#3', text='Atendente')
        self.tableagen.heading('#4', text='Valor')
        self.tableagen.heading('#5', text='Horario')
        self.tableagen.heading('#6', text='Situação')

        self.tableagen.column('#0',width = 1)
        self.tableagen.column('#1', width=100)
        self.tableagen.column('#2', width=50)
        self.tableagen.column('#3', width=70)
        self.tableagen.column('#4', width=50)
        self.tableagen.column('#5', width=55)
        self.tableagen.column('#6', width=100)

        self.tableagen.place(x=75,y=55,width=450,height=200)

        barrarolagem = Scrollbar(app,orient = 'vertical')
        self.tableagen.configure(yscroll=barrarolagem.set)
        barrarolagem.place(x=526,y=55,width=15,height=200)

class cadastro():
    def __init__(self):
        self.app2 = Toplevel()
        self.app2.title('Cadastra Cliente')
        self.app2.geometry('350x150')
        self.app2.iconbitmap(r'mdchefeicon.ico')
        self.app2.configure(background = '#f8bdc6')
        self.app2.resizable(False, False)
        self.app2.transient(app)
        self.app2.focus_force()
        self.app2.grab_set()

        #labels/button
        nometxt = Label(self.app2,text ='Nome do Cliente',background = '#f8bdc6', foreground = '#000')
        cpftxt = Label(self.app2,text ='CPF do Cliente',background = '#f8bdc6', foreground = '#000')
        teltxt = Label(self.app2,text = 'TEL do Cliente',background = '#f8bdc6', foreground = '#000')
        horinzontal = Label(self.app2, background='#FFFFFF', foreground='#000')
        btcads = Button(self.app2,text='Cadastra Cliente',background = '#ffb6c1', foreground = '#000') #command = insertcli)

        #Inputs
        nomeinp = Entry(self.app2,background = '#FFFFFF', foreground = '#000')
        cpfinp = Entry(self.app2,background = '#FFFFFF', foreground = '#000')
        telinp = Entry(self.app2,background = '#FFFFFF', foreground = '#000')

        #Configs
        nometxt.config(font=('Calibri',10,'bold'))
        cpftxt.config(font=('Calibri',10,'bold'))
        teltxt.config(font=('Calibri',10,'bold'))
        nomeinp.config(font=('Calibri', 10, 'bold'))
        cpfinp.config(font=('Calibri', 10, 'bold'))
        telinp.config(font=('Calibri', 10, 'bold'))
        btcads.config(font=('Calibri', 10, 'bold'))

        #Place
        nometxt.place(x=40,y=15,width=100,height=30)
        cpftxt.place(x=40, y=48, width=100, height=30)
        teltxt.place(x=40, y=81, width=100, height=30)
        nomeinp.place(x=145,y=20,width=150,height=20)
        cpfinp.place(x=145, y=53, width=150, height=20)
        telinp.place(x=145, y=86, width=150, height=20)
        horinzontal.place(x=0, y=0, width=1000, height=15)
        btcads.place(x=50, y=120, width=250, height=20)

class clientes():
    def __init__(self):
        self.app3 = Toplevel()
        self.app3.title('Clientes Cadastrados')
        self.app3.geometry('500x500')
        self.app3.iconbitmap(r'mdchefeicon.ico')
        self.app3.configure(background='#f8bdc6')
        self.app3.transient(app)
        self.app3.focus_force()
        self.app3.grab_set()

        horinzontal = Label(self.app3, background='#FFFFFF', foreground='#000')
        vertical = Label(self.app3, background='#FFFFFF', foreground='#000')
        verticaltxt = Label(self.app3, text='T\n\nI\n\nF\n\nF\n\nA\n\nN\n\nY\n\n\n\nT\n\nE\n\nC\n\nH', background='#FFFFFF',foreground='#000')
        atl = Button(self.app3, text='Atualizar Cadastro', font='calibri', background='#ffb6c1', foreground='#000', command=atualizarcad)
        dell = Button(self.app3,text='Deletar Cadastro',font= 'calibri' ,background = '#ffb6c1', foreground = '#000',command= deletarcad)

        verticaltxt.config(font=("Agency FB", 10, 'bold'))

        verticaltxt.place(x=25, y=60, width=10, height=400)
        vertical.place(x=0, y=0, width=70, height=2000)
        horinzontal.place(x=0, y=0, width=2000, height=50)
        atl.place(x=70,y=15,width = 150,height = 30)
        dell.place(x=230,y=15,width = 150,height = 30)

class atualizarcad():
    def __init__(self):
        self.app4 = Toplevel()
        self.app4.title('Atualizar Cliente')
        self.app4.geometry('315x150')
        self.app4.resizable(False, False)
        self.app4.configure(background='#f8bdc6')
        self.app4.iconbitmap(r'mdchefeicon.ico')
        self.app4.transient(app)
        self.app4.focus_force()
        self.app4.grab_set()

        #Labels/Buttons
        cpfclitxt = Label(self.app4,text = 'Informe o CPF',background = '#f8bdc6', foreground= '#000')
        btbusc = Button(self.app4,text = 'Buscar', background = '#FFFFFF', foreground = '#000')
        nometxt = Label(self.app4, text='Nome do Cliente', background='#f8bdc6', foreground='#000')
        cpftxt = Label(self.app4, text='CPF do Cliente', background='#f8bdc6', foreground='#000')
        teltxt = Label(self.app4, text='TEL do Cliente', background='#f8bdc6', foreground='#000')
        horinzontal = Label(self.app4, background='#FFFFFF', foreground='#000')
        btatl = Button(self.app4, text='Atualizar Cadastro', background='#ffb6c1', foreground='#000')

        #Inputs
        idclinp = Entry(self.app4,background = '#FFFFFF', foreground = '#000')
        nomeinp = Entry(self.app4, background='#FFFFFF', foreground='#000')
        cpfinp = Entry(self.app4, background='#FFFFFF', foreground='#000')
        telinp = Entry(self.app4, background='#FFFFFF', foreground='#000')

        #Configs
        cpfclitxt.config(font=('Calibri', 10, 'bold'))
        idclinp.config(font=('Calibri', 10, 'bold'))
        btbusc.config(font=('Calibri', 10, 'bold'))
        nometxt.config(font=('Calibri', 10, 'bold'))
        cpftxt.config(font=('Calibri', 10, 'bold'))
        teltxt.config(font=('Calibri', 10, 'bold'))
        nomeinp.config(font=('Calibri', 10, 'bold'))
        cpfinp.config(font=('Calibri', 10, 'bold'))
        telinp.config(font=('Calibri', 10, 'bold'))
        btatl.config(font=('Calibri', 10, 'bold'))

        #Place
        cpfclitxt.place(x=1,y=15,width=100,height=30)
        idclinp.place(x=100,y=20,width=100,height=20)
        btbusc.place(x=205,y=20,width=50,height=20)
        nometxt.place(x=40, y=40, width=100, height=30)
        cpftxt.place(x=40, y=65, width=100, height=30)
        teltxt.place(x=40, y=89, width=100, height=30)
        nomeinp.place(x=145, y=45, width=150, height=20)
        cpfinp.place(x=145, y=70, width=150, height=20)
        telinp.place(x=145, y=95, width=150, height=20)
        horinzontal.place(x=0, y=0, width=1000, height=15)
        btatl.place(x=50, y=120, width=250, height=20)

class deletarcad():
    def __init__(self):
        self.app5 = Toplevel()
        self.app5.title('Deletar Cliente')
        self.app5.geometry('315x150')
        self.app5.resizable(False, False)
        self.app5.iconbitmap(r'mdchefeicon.ico')
        self.app5.configure(background='#f8bdc6')
        self.app5.transient(app)
        self.app5.focus_force()
        self.app5.grab_set()

        # Labels/Buttons
        cpfclitxt = Label(self.app5, text='Informe o CPF', background='#f8bdc6', foreground='#000')
        btbusc = Button(self.app5, text='Buscar', background='#FFFFFF', foreground='#000')
        nometxt = Label(self.app5, text='Nome do Cliente', background='#f8bdc6', foreground='#000')
        cpftxt = Label(self.app5, text='CPF do Cliente', background='#f8bdc6', foreground='#000')
        teltxt = Label(self.app5, text='TEL do Cliente', background='#f8bdc6', foreground='#000')
        horinzontal = Label(self.app5, background='#FFFFFF', foreground='#000')
        btatl = Button(self.app5, text='Atualizar Cadastro', background='#ffb6c1', foreground='#000')

        # Inputs
        idclinp = Entry(self.app5, background='#FFFFFF', foreground='#000')
        nomeinp = Entry(self.app5, background='#FFFFFF', foreground='#000')
        cpfinp = Entry(self.app5, background='#FFFFFF', foreground='#000')
        telinp = Entry(self.app5, background='#FFFFFF', foreground='#000')

        # Configs
        cpfclitxt.config(font=('Calibri', 10, 'bold'))
        idclinp.config(font=('Calibri', 10, 'bold'))
        btbusc.config(font=('Calibri', 10, 'bold'))
        nometxt.config(font=('Calibri', 10, 'bold'))
        cpftxt.config(font=('Calibri', 10, 'bold'))
        teltxt.config(font=('Calibri', 10, 'bold'))
        nomeinp.config(font=('Calibri', 10, 'bold'))
        cpfinp.config(font=('Calibri', 10, 'bold'))
        telinp.config(font=('Calibri', 10, 'bold'))
        btatl.config(font=('Calibri', 10, 'bold'))

        # Place
        cpfclitxt.place(x=1, y=15, width=100, height=30)
        idclinp.place(x=100, y=20, width=100, height=20)
        btbusc.place(x=205, y=20, width=50, height=20)
        nometxt.place(x=40, y=40, width=100, height=30)
        cpftxt.place(x=40, y=65, width=100, height=30)
        teltxt.place(x=40, y=89, width=100, height=30)
        nomeinp.place(x=145, y=45, width=150, height=20)
        cpfinp.place(x=145, y=70, width=150, height=20)
        telinp.place(x=145, y=95, width=150, height=20)
        horinzontal.place(x=0, y=0, width=1000, height=15)
        btatl.place(x=50, y=120, width=250, height=20)

class agenda():
    def __init__(self):
        self.app6 = Toplevel()
        self.app6.title('Agendar Horario')
        self.app6.geometry('315x180')
        self.app6.resizable(False, False)
        self.app6.iconbitmap(r'mdchefeicon.ico')
        self.app6.configure(background='#f8bdc6')
        self.app6.transient(app)
        self.app6.focus_force()
        self.app6.grab_set()

        # Labels/Buttons
        clinome = Label(self.app6,text='Nome do Cliente', background='#f8bdc6', foreground='#000')
        serv = Label(self.app6, text='Serviço', background='#f8bdc6', foreground='#000')
        atend = Label(self.app6, text='Nome do Atendente', background='#f8bdc6', foreground='#000')
        valor = Label(self.app6, text='Valor', background='#f8bdc6', foreground='#000')
        hora = Label(self.app6, text='Horario', background='#f8bdc6', foreground='#000')
        btagen = Button(self.app6, text='Realizar Agendamento', background='#ffb6c1', foreground='#000')
        horinzontal = Label(self.app6, background='#FFFFFF', foreground='#000')

        # Inputs
        clinomeinp = Entry(self.app6,background='#FFFFFF', foreground='#000')
        servinp = Entry(self.app6,background='#FFFFFF', foreground='#000')
        atendinp = Entry(self.app6,background='#FFFFFF', foreground='#000')
        valorinp = Entry(self.app6,background='#FFFFFF', foreground='#000')
        horainp = Entry(self.app6,background='#FFFFFF', foreground='#000')

        #Places
        clinome.place(x=20,y=15,width=100,height=30)
        clinomeinp.place(x=140,y=20,width=150, height=20)
        serv.place(x=20,y=40,width=100,height=30)
        servinp.place(x=140,y=45,width=150, height=20)
        atend.place(x=20,y=65,width=110,height=30)
        atendinp.place(x=140,y=70,width=150, height=20)
        valor.place(x=20,y=90,width=110,height=30)
        valorinp.place(x=140,y=95,width=150, height=20)
        hora.place(x=20,y=115,width=110,height=30)
        horainp.place(x=140,y=120,width=150, height=20)
        btagen.place(x=20, y=150, width=275, height=20)
        horinzontal.place(x=0, y=0, width=1000, height=15)

aplicativo()





from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import sqlite3

app = Tk()
class aplicativo():
    def __init__(self):
        self.app = app
        self.telamain()
        self.tabel()
        self.criatabelas()
        app.mainloop()
    def conectadb(self):
        self.conn = sqlite3.connect('tiffanytech.sql')
        self.cursor = self.conn.cursor()
        print('Conectado ao Banco de dados')
    def desconect(self):
        self.conn.close();
        print('Desconectado do Banco de Dados')
    def criatabelas(self):
        self.conectadb()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
                                id integer PRIMARY KEY AUTOINCREMENT,
                                nome VARCHAR(100) NOT NULL,
                                cpf integer(15) NOT NULL,
                                telefone integer(15) NOT NULL
                                );""")
        self.conn.commit(); print('Tabela criada')
        self.desconect()
    def telamain(self):
        self.app.title('Salão Tiffany')
        self.app.geometry('560x263')
        self.app.resizable(False, False)
        self.app.configure(background='#f8bdc6')
        self.app.iconbitmap(r'mdchefeicon.ico')

        # Labels/Buttons
        horinzontal = Label(self.app, background='#FFFFFF', foreground='#000')
        vertical = Label(self.app, background='#FFFFFF', foreground='#000')
        verticaltxt = Label(self.app, text='T\nI\nF\nF\nA\nN\nY\n\nT\nE\nC\nH', background='#FFFFFF',foreground='#000')
        btcad = Button(self.app, text='Form Cliente', font='calibri', background='#ffb6c1', foreground='#000',command=cadastro)
        btcli = Button(self.app, text='Clientes', font='calibri', background='#ffb6c1', foreground='#000', command=clientes)
        btagn = Button(self.app, text='Agendar Horario', font='calibri', background='#ffb6c1', foreground='#000',command=agenda)

        # Configs
        verticaltxt.config(font=("Agency FB", 11, 'bold'))

        # Places
        btcad.place(x=70, y=15, width=150, height=30)
        verticaltxt.place(x=15, y=25, width=35, height=210)
        vertical.place(x=0, y=0, width=70, height=2000)
        horinzontal.place(x=0, y=0, width=2000, height=50)
        btcli.place(x=230, y=15, width=150, height=30)
        btagn.place(x=390, y=15, width=150, height=30)
    def tabel(self):
        tabela= ttk.Treeview(app, height = 30, column = ('col1','col2','col3','col4','col5','col6','col7'))
        tabela.heading('#0', text='')
        tabela.heading('#1', text='Nome do Cliente')
        tabela.heading('#2', text='Serviço')
        tabela.heading('#3', text='Atendente')
        tabela.heading('#4', text='Valor')
        tabela.heading('#5', text='Horario')
        tabela.heading('#6', text='Situação')

        tabela.column('#0',width = 1)
        tabela.column('#1', width=100)
        tabela.column('#2', width=50)
        tabela.column('#3', width=70)
        tabela.column('#4', width=50)
        tabela.column('#5', width=55)
        tabela.column('#6', width=100)

        tabela.place(x=75,y=55,width=450,height=200)

        barrarolagem = Scrollbar(app,orient = 'vertical')
        tabela.configure(yscroll=barrarolagem.set)
        barrarolagem.place(x=526,y=55,width=15,height=200)


class cadastro():
    def __init__(self):
        def insertcli():
            nome = nomeinpcad.get()
            cpf = cpfinpcad.get()
            telefone = telinpcad.get()
            conn = sqlite3.connect('tiffanytech.sql')
            cursor = conn.cursor()
            print('Conectado ao Banco de dados')
            if nome == '' or cpf == '' or telefone == '':
                MessageBox.showinfo('Confira os campos', 'Algum campo esta em falta')
            else:
                print(f'Nome: {nome}\nCPF: {cpf}\nTelefone: {telefone}')
                cursor.execute('insert into clientes (nome,cpf,telefone) values(?,?,?)', (nome, cpf, telefone))
                conn.commit()
                conn.close()
                MessageBox.showinfo('Dados inseridos', 'Cliente cadastrado com sucesso')

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
        btcads = Button(self.app2,text='Cadastra Cliente',background = '#ffb6c1', foreground = '#000', command =insertcli)

        #Inputs
        nomeinpcad = Entry(self.app2,background = '#FFFFFF', foreground = '#000')
        cpfinpcad = Entry(self.app2,background = '#FFFFFF', foreground = '#000')
        telinpcad = Entry(self.app2,background = '#FFFFFF', foreground = '#000')

        #Configs
        nometxt.config(font=('Calibri',10,'bold'))
        cpftxt.config(font=('Calibri',10,'bold'))
        teltxt.config(font=('Calibri',10,'bold'))
        nomeinpcad.config(font=('Calibri', 10, 'bold'))
        cpfinpcad.config(font=('Calibri', 10, 'bold'))
        telinpcad.config(font=('Calibri', 10, 'bold'))
        btcads.config(font=('Calibri', 10, 'bold'))

        #Place
        nometxt.place(x=40,y=15,width=100,height=30)
        cpftxt.place(x=40, y=48, width=100, height=30)
        teltxt.place(x=40, y=81, width=100, height=30)
        nomeinpcad.place(x=145,y=20,width=150,height=20)
        cpfinpcad.place(x=145, y=53, width=150, height=20)
        telinpcad.place(x=145, y=86, width=150, height=20)
        horinzontal.place(x=0, y=0, width=1000, height=15)
        btcads.place(x=50, y=120, width=250, height=20)

class clientes():
    def __init__(self):
        self.app3 = Toplevel()
        self.app3.title('Clientes Cadastrados')
        self.app3.geometry('500x263')
        self.app3.resizable(False, False)
        self.app3.iconbitmap(r'mdchefeicon.ico')
        self.app3.configure(background='#f8bdc6')
        self.app3.transient(app)
        self.app3.focus_force()
        self.app3.grab_set()
        self.tabelcli()

        horinzontal = Label(self.app3, background='#FFFFFF', foreground='#000')
        vertical = Label(self.app3, background='#FFFFFF', foreground='#000')
        verticaltxt = Label(self.app3, text='T\nI\nF\nF\nA\nN\nY\n\nT\nE\nC\nH', background='#FFFFFF',foreground='#000')
        atl = Button(self.app3, text='Atualizar Cadastro', font='calibri', background='#ffb6c1', foreground='#000', command=atualizarcad)
        dell = Button(self.app3,text='Deletar Cadastro',font= 'calibri' ,background = '#ffb6c1', foreground = '#000',command= deletarcad)

        verticaltxt.config(font=("Agency FB", 11, 'bold'))

        verticaltxt.place(x=15, y=25, width=35, height=210)
        vertical.place(x=0, y=0, width=70, height=2000)
        horinzontal.place(x=0, y=0, width=2000, height=50)
        atl.place(x=70,y=15,width = 150,height = 30)
        dell.place(x=230,y=15,width = 150,height = 30)

    def tabelcli(self):
        tabelacli= ttk.Treeview(self.app3, height=30,column=('col1', 'col2', 'col3', 'col4','col5'))
        tabelacli.heading('#0', text='')
        tabelacli.heading('#1', text='id')
        tabelacli.heading('#2', text='Nome do Cliente')
        tabelacli.heading('#3', text='CPF')
        tabelacli.heading('#4', text='Telefone')

        tabelacli.column('#0', width=1)
        tabelacli.column('#1', width=50)
        tabelacli.column('#2', width=100)
        tabelacli.column('#3', width=100)
        tabelacli.column('#4', width=100)

        tabelacli.place(x=75,y=55, width=390, height=200)

        barrarolagem2 = Scrollbar(self.app3, orient='vertical')
        tabelacli.configure(yscroll=barrarolagem2.set)
        barrarolagem2.place(x=466, y=55, width=15, height=200)

class atualizarcad():
    def __init__(self):
        def buscacliat():
            conn = sqlite3.connect('tiffanytech.sql')
            cursor = conn.cursor()
            print('Conectado ao Banco de dados')
            cpfbusc = cpfclinpat.get()
            cursor.execute('SELECT * FROM clientes WHERE cpf = (?)', (cpfbusc,))
            for i in cursor.fetchall():
                velhonome['text'] = i[1]
                velhocpf['text'] = i[2]
                velhotel['text'] = i[3]

                conn.commit()
                conn.close()

        def atucli():
            conn = sqlite3.connect('tiffanytech.sql')
            cursor = conn.cursor()
            print('Conectado ao Banco de dados')
            cpfbusc = cpfclinpat.get()
            cursor.execute('SELECT * FROM clientes WHERE cpf = (?)', (cpfbusc,))
            for a in cursor.fetchall():
                nome = a[1]
                cpf = a[2]
                tel = a[3]

                nomenovo = nomeinpat.get()
                cpfnovo = cpfinpat.get()
                telnovo = telinpat.get()

            if not nomenovo:
                nomenovo = nome
            if not cpfnovo:
                cpfnovo = cpf
            if not telnovo:
                telnovo = tel

            cursor.execute(f'''UPDATE clientes
                                SET nome = ? , cpf = ? , telefone = ?
                                WHERE cpf = ?''', (nomenovo, cpfnovo, telnovo, cpfbusc))

            conn.commit()
            conn.close()

        self.app4 = Toplevel()
        self.app4.title('Atualizar Cliente')
        self.app4.geometry('600x150')
        self.app4.resizable(False, False)
        self.app4.configure(background='#f8bdc6')
        self.app4.iconbitmap(r'mdchefeicon.ico')
        self.app4.transient(app)
        self.app4.focus_force()
        self.app4.grab_set()

        #Labels/Buttons
        cpfclitxt = Label(self.app4,text = 'Informe o CPF',background = '#f8bdc6', foreground= '#000')
        btbusc = Button(self.app4,text = 'Buscar', background = '#FFFFFF', foreground = '#000',command = buscacliat)
        nometxt = Label(self.app4, text='Nome do Cliente', background='#f8bdc6', foreground='#000')
        cpftxt = Label(self.app4, text='CPF do Cliente', background='#f8bdc6', foreground='#000')
        teltxt = Label(self.app4, text='TEL do Cliente', background='#f8bdc6', foreground='#000')
        horinzontal = Label(self.app4, background='#FFFFFF', foreground='#000')
        btatl = Button(self.app4, text='Atualizar Cadastro', background='#ffb6c1', foreground='#000',command = atucli)
        velhocpf = Label(self.app4, text='', background='#f8bdc6', foreground='#000')
        velhotel = Label(self.app4, text='', background='#ffffff', foreground='#000')
        velhonome = Label(self.app4, text='', background='#ffffff', foreground='#000')

        #Inputs
        cpfclinpat = Entry(self.app4,background = '#FFFFFF', foreground = '#000')
        nomeinpat = Entry(self.app4, background='#FFFFFF', foreground='#000')
        cpfinpat = Entry(self.app4, background='#f8bdc6', foreground='#000')
        telinpat = Entry(self.app4, background='#FFFFFF', foreground='#000')

        #Configs
        cpfclitxt.config(font=('Calibri', 10, 'bold'))
        cpfclinpat.config(font=('Calibri', 10, 'bold'))
        btbusc.config(font=('Calibri', 10, 'bold'))
        nometxt.config(font=('Calibri', 10, 'bold'))
        cpftxt.config(font=('Calibri', 10, 'bold'))
        teltxt.config(font=('Calibri', 10, 'bold'))
        nomeinpat.config(font=('Calibri', 10, 'bold'))
        cpfinpat.config(font=('Calibri', 10, 'bold'))
        telinpat.config(font=('Calibri', 10, 'bold'))
        btatl.config(font=('Calibri', 10, 'bold'))
        velhotel.config(font=('Calibri', 10, 'bold'))
        velhocpf.config(font=('Calibri', 10, 'bold'))
        velhonome.config(font=('Calibri', 10, 'bold'))

        #Place
        cpfclitxt.place(x=1,y=15,width=100,height=30)
        cpfclinpat.place(x=100,y=20,width=100,height=20)
        btbusc.place(x=205,y=20,width=50,height=20)
        nometxt.place(x=40, y=40, width=100, height=30)
        cpftxt.place(x=40, y=65, width=100, height=30)
        teltxt.place(x=40, y=89, width=100, height=30)
        nomeinpat.place(x=145, y=45, width=150, height=20)
        cpfinpat.place(x=145, y=70, width=150, height=20)
        telinpat.place(x=145, y=95, width=150, height=20)
        horinzontal.place(x=0, y=0, width=1000, height=15)
        btatl.place(x=50, y=120, width=250, height=20)
        velhonome.place(x=300, y=45, width=150, height=20)
        velhocpf.place(x=300, y=70, width=150, height=20)
        velhotel.place(x=300, y=95, width=150, height=20)

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
        idclinpdel = Entry(self.app5, background='#FFFFFF', foreground='#000')
        nomeinpdel = Entry(self.app5, background='#FFFFFF', foreground='#000')
        cpfinpdel = Entry(self.app5, background='#FFFFFF', foreground='#000')
        telinpdel = Entry(self.app5, background='#FFFFFF', foreground='#000')

        # Configs
        cpfclitxt.config(font=('Calibri', 10, 'bold'))
        idclinpdel.config(font=('Calibri', 10, 'bold'))
        btbusc.config(font=('Calibri', 10, 'bold'))
        nometxt.config(font=('Calibri', 10, 'bold'))
        cpftxt.config(font=('Calibri', 10, 'bold'))
        teltxt.config(font=('Calibri', 10, 'bold'))
        nomeinpdel.config(font=('Calibri', 10, 'bold'))
        cpfinpdel.config(font=('Calibri', 10, 'bold'))
        telinpdel.config(font=('Calibri', 10, 'bold'))
        btatl.config(font=('Calibri', 10, 'bold'))

        # Place
        cpfclitxt.place(x=1, y=15, width=100, height=30)
        idclinpdel.place(x=100, y=20, width=100, height=20)
        btbusc.place(x=205, y=20, width=50, height=20)
        nometxt.place(x=40, y=40, width=100, height=30)
        cpftxt.place(x=40, y=65, width=100, height=30)
        teltxt.place(x=40, y=89, width=100, height=30)
        nomeinpdel.place(x=145, y=45, width=150, height=20)
        cpfinpdel.place(x=145, y=70, width=150, height=20)
        telinpdel.place(x=145, y=95, width=150, height=20)
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
        clinomeinpag = Entry(self.app6,background='#FFFFFF', foreground='#000')
        servinpag = Entry(self.app6,background='#FFFFFF', foreground='#000')
        atendinpag = Entry(self.app6,background='#FFFFFF', foreground='#000')
        valorinpag = Entry(self.app6,background='#FFFFFF', foreground='#000')
        horainpag = Entry(self.app6,background='#FFFFFF', foreground='#000')

        #Places
        clinome.place(x=20,y=15,width=100,height=30)
        clinomeinpag.place(x=140,y=20,width=150, height=20)
        serv.place(x=20,y=40,width=100,height=30)
        servinpag.place(x=140,y=45,width=150, height=20)
        atend.place(x=20,y=65,width=110,height=30)
        atendinpag.place(x=140,y=70,width=150, height=20)
        valor.place(x=20,y=90,width=110,height=30)
        valorinpag.place(x=140,y=95,width=150, height=20)
        hora.place(x=20,y=115,width=110,height=30)
        horainpag.place(x=140,y=120,width=150, height=20)
        btagen.place(x=20, y=150, width=275, height=20)
        horinzontal.place(x=0, y=0, width=1000, height=15)

aplicativo()
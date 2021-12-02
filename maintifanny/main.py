from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import sqlite3

app = Tk()

class funcs():
    def limpacampocad(self):
        self.nomeinpcad.delete(0, END)
        self.cpfinpcad.delete(0, END)
        self.telinpcad.delete(0, END)

    def limpacampoat(self):
        self.cpfclinpat.delete(0, END)
        self.nomeinpat.delete(0, END)
        self.cpfinpat.delete(0, END)
        self.telinpat.delete(0, END)
        self.velhonome['text'] = ''
        self.velhocpf['text'] = ''
        self.velhotel['text'] = ''

    def limpacampodel(self):
        self.velhonome['text'] = ''
        self.velhocpf['text'] = ''
        self.velhotel['text'] = ''
        self.cpfclinpat.delete(0,END)

    def limpaagnd(self):
        self.clinomeinpag.delete(0,END)
        self.servinpag.delete(0,END)
        self.atendinpag.delete(0,END)
        self.valorinpag.delete(0,END)
        self.horainpag.delete(0,END)
        self.situang.delete(0,END)


    def conectadb(self):
        self.conn = sqlite3.connect('tiffanytech.sql')
        self.cursor = self.conn.cursor()
        print('Conectado ao Banco de dados')

    def desconect(self):
        self.conn.close()
        print('Desconectado do Banco de Dados')

    def criatabelas(self):
        self.conectadb()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
                            id integer PRIMARY KEY AUTOINCREMENT,
                            nome VARCHAR(100) NOT NULL,
                            cpf integer(15) NOT NULL,
                            telefone integer(15) NOT NULL
                            );""")
        self.conn.commit()
        self.desconect()
        self.conectadb()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS agendamento (
                            nome VARCHAR(100) NOT NULL,
                            servico VARCHAR(100) NOT NULL,
                            atendente VARCHAR(100) NOT NULL,
                            valor FLOAT(15) NOT NULL,
                            horario DATETIME NOT NULL,
                            situacao VARCHAR(100) NOT NULL
                            );""")

        self.conn.commit() ; print('Tabelas criada')
        self.desconect()

    def insertcli(self):
        self.nome = self.nomeinpcad.get()
        self.cpf = self.cpfinpcad.get()
        self.telefone = self.telinpcad.get()
        self.conectadb()
        if self.nome == '' or self.cpf == '' or self.telefone == '':
            MessageBox.showinfo('Confira os campos', 'Algum campo esta em falta')
        else:
            print(f'Nome: {self.nome}\nCPF: {self.cpf}\nTelefone: {self.telefone}')
            self.cursor.execute('insert into clientes (nome,cpf,telefone) values(?,?,?)', (self.nome, self.cpf, self.telefone))
            self.conn.commit()
            self.desconect()
            self.limpacampocad()
            MessageBox.showinfo('Dados inseridos', 'Cliente cadastrado com sucesso')
            self.lista()

    def lista(self):
        self.tabelacli.delete(*self.tabelacli.get_children())
        self.conectadb()
        lista = self.cursor.execute('SELECT id, nome, cpf, telefone FROM clientes ORDER BY id ')
        for a in lista:
            self.tabelacli.insert('', END, values=a)
        self.desconect()

    def listagn(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conectadb()
        lista = self.cursor.execute('SELECT nome, servico,atendente, valor,  horario, situacao FROM agendamento ORDER BY nome ASC; ')
        for a in lista:
            self.tabela.insert('', END, values=a)
        self.desconect()

    def buscacliat(self):
        self.conectadb()
        self.cpfbusc = self.cpfclinpat.get()
        self.cursor.execute('SELECT * FROM clientes WHERE cpf = (?)', (self.cpfbusc,))
        for i in self.cursor.fetchall():
            self.velhonome['text'] = i[1]
            self.velhocpf['text'] = i[2]
            self.velhotel['text'] = i[3]
            self.conn.commit()
        self.desconect()

    def atucli(self):
        self.conectadb()
        self.cpfbusc = self.cpfclinpat.get()
        self.cursor.execute('SELECT * FROM clientes WHERE cpf = (?)', (self.cpfbusc,))
        for a in self.cursor.fetchall():
            self.nome = a[1]
            self.cpf = a[2]
            self.tel = a[3]

            self.nomenovo = self.nomeinpat.get()
            self.cpfnovo = self.cpfinpat.get()
            self.telnovo = self.telinpat.get()

        if not self.nomenovo:
            self.nomenovo = self.nome
        if not self.cpfnovo:
            self.cpfnovo = self.cpf
        if not self.telnovo:
            self.telnovo = self.tel

        self.cursor.execute(f'''UPDATE clientes
                            SET nome = ? , cpf = ? , telefone = ?
                            WHERE cpf = ?''', (self.nomenovo, self.cpfnovo, self.telnovo, self.cpfbusc))
        self.conn.commit()
        MessageBox.showinfo('Concluido', 'Os Dados do Cliente Foram Atualizados')
        self.limpacampoat()
        self.desconect()

    def deletarcadbusc(self):
        self.conectadb()
        self.cpfdel = self.cpfclinpat.get()
        self.cursor.execute('DELETE FROM clientes WHERE cpf = ?', (self.cpfdel,))
        self.conn.commit()
        MessageBox.showinfo('Concluido', 'Cliente Deletado Com Sucesso')
        self.limpacampodel()
        self.desconect()
        self.lista()

    def realizaagn(self):
        self.conectadb()
        self.nomeagn = self.clinomeinpag.get()
        self.servagn = self.servinpag.get()
        self.atendagn = self.atendinpag.get()
        self.valoragn = self.valorinpag.get()
        self.horaagn = self.horainpag.get()
        self.situa = self.situang.get()
        if self.nomeagn == '' or self.servagn == '' or self.atendagn == '' or self.valoragn == '' or self.horaagn == '' or self.situa == '':
            MessageBox.showinfo('Confira os campos', 'Algum campo esta em falta')
        else:
            self.cursor.execute('INSERT INTO agendamento (nome,servico,atendente,valor,horario,situacao) VALUES (?,?,?,?,?,?)',
                           (self.nomeagn, self.servagn, self.atendagn, self.valoragn, self.horaagn,self.situa))
            MessageBox.showinfo('Status de Agendamento', 'Horario Marcado com Sucesso')

        self.conn.commit()
        self.desconect()
        self.listagn()
        self.limpaagnd()

class aplicativo(funcs):
    def __init__(self):
        self.app = app

        self.telamain()
        self.tabel()
        self.criatabelas()
        self.listagn()
        self.app.mainloop()

    def telamain(self):
        self.app.title('Salão Tiffany')
        self.app.geometry('585x263')
        self.app.resizable(False, False)
        self.app.configure(background='#f8bdc6')
        self.app.iconbitmap('mdchefeicon.ico')

        # Labels/Buttons
        self.horinzontal = Label(self.app, background='#FFFFFF', foreground='#000')
        self.vertical = Label(self.app, background='#FFFFFF', foreground='#000')
        self.verticaltxt = Label(self.app, text='T\nI\nF\nF\nA\nN\nY\n\nT\nE\nC\nH', background='#FFFFFF',foreground='#000')
        self.btcad = Button(self.app, text='Form Cliente', font='calibri', background='#ffb6c1', foreground='#000',command=cadastro)
        self.btcli = Button(self.app, text='Clientes', font='calibri', background='#ffb6c1', foreground='#000', command=clientes)
        self.btagn = Button(self.app, text='Agendar Horario', font='calibri', background='#ffb6c1', foreground='#000',command=agenda)
        self.image = PhotoImage(file='refresh.png')
        self.image = self.image.subsample(2, 2)
        self.btref = Button(self.app,font=('Calibri',10,'bold'),image = self.image ,background = '#FFFFFF', foreground = '#000', command = self.listagn)

        # Configs
        self.verticaltxt.config(font=("Agency FB", 11, 'bold'))

        # Places
        self.btcad.place(x=70, y=15, width=150, height=30)
        self.verticaltxt.place(x=15, y=25, width=35, height=210)
        self.vertical.place(x=0, y=0, width=70, height=2000)
        self.horinzontal.place(x=0, y=0, width=2000, height=50)
        self.btcli.place(x=230, y=15, width=150, height=30)
        self.btagn.place(x=390, y=15, width=150, height=30)
        self.btref.place(x=545, y=15,width=30,height=30)

    def tabel(self):
        self.tabela = ttk.Treeview(app, height=30, column=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7'))
        self.tabela.heading('#0', text='')
        self.tabela.heading('#1', text='Nome do Cliente')
        self.tabela.heading('#2', text='Serviço')
        self.tabela.heading('#3', text='Atendente')
        self.tabela.heading('#4', text='Valor')
        self.tabela.heading('#5', text='Horario')
        self.tabela.heading('#6', text='Situação')

        self.tabela.column('#0', width=1)
        self.tabela.column('#1', width=100)
        self.tabela.column('#2', width=50)
        self.tabela.column('#3', width=70)
        self.tabela.column('#4', width=50)
        self.tabela.column('#5', width=55)
        self.tabela.column('#6', width=100)

        self.tabela.place(x=75, y=55, width=450, height=200)

        self.barrarolagem = Scrollbar(self.app, orient='vertical')
        self.tabela.configure(yscroll=self.barrarolagem.set)
        self.barrarolagem.place(x=526, y=55, width=15, height=200)

class cadastro(funcs):
    def __init__(self):
        self.telacad()
        self.lista()
    def telacad(self):
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
        self.nometxt = Label(self.app2,text ='Nome do Cliente',background = '#f8bdc6', foreground = '#000')
        self.cpftxt = Label(self.app2,text ='CPF do Cliente',background = '#f8bdc6', foreground = '#000')
        self.teltxt = Label(self.app2,text = 'TEL do Cliente',background = '#f8bdc6', foreground = '#000')
        self.horinzontal = Label(self.app2, background='#FFFFFF', foreground='#000')
        self.btcads = Button(self.app2,text='Cadastra Cliente',background = '#ffb6c1', foreground = '#000', command = self.insertcli)


        #Inputs
        self.nomeinpcad = Entry(self.app2,background = '#FFFFFF', foreground = '#000')
        self.cpfinpcad = Entry(self.app2,background = '#FFFFFF', foreground = '#000')
        self.telinpcad = Entry(self.app2,background = '#FFFFFF', foreground = '#000')

        #Configs
        self.nometxt.config(font=('Calibri',10,'bold'))
        self.cpftxt.config(font=('Calibri',10,'bold'))
        self.teltxt.config(font=('Calibri',10,'bold'))
        self.nomeinpcad.config(font=('Calibri', 10, 'bold'))
        self.cpfinpcad.config(font=('Calibri', 10, 'bold'))
        self.telinpcad.config(font=('Calibri', 10, 'bold'))
        self.btcads.config(font=('Calibri', 10, 'bold'))

        #Place
        self.nometxt.place(x=40,y=15,width=100,height=30)
        self.cpftxt.place(x=40, y=48, width=100, height=30)
        self.teltxt.place(x=40, y=81, width=100, height=30)
        self.nomeinpcad.place(x=145,y=20,width=150,height=20)
        self.cpfinpcad.place(x=145, y=53, width=150, height=20)
        self.telinpcad.place(x=145, y=86, width=150, height=20)
        self.horinzontal.place(x=0, y=0, width=1000, height=15)
        self.btcads.place(x=50, y=120, width=250, height=20)

class clientes(funcs):
    def __init__(self):
        self.tela3()
        self.tabelcli()

        self.lista()
    def tela3(self):
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

        self.horinzontal = Label(self.app3, background='#FFFFFF', foreground='#000')
        self.vertical = Label(self.app3, background='#FFFFFF', foreground='#000')
        self.verticaltxt = Label(self.app3, text='T\nI\nF\nF\nA\nN\nY\n\nT\nE\nC\nH', background='#FFFFFF',foreground='#000')
        self.atl = Button(self.app3, text='Atualizar Cadastro', font='calibri', background='#ffb6c1', foreground='#000', command=atualizarcad)
        self.dell = Button(self.app3,text='Deletar Cadastro',font= 'calibri' ,background = '#ffb6c1', foreground = '#000',command= deletarcad)
        self.image = PhotoImage(file='refresh.png')
        self.image = self.image.subsample(2, 2)
        self.btref = Button(self.app3, text='Recarregar', font=('Calibri', 10, 'bold'), image= self.image ,background='#ffffff', foreground='#000', command= self.lista)

        self.verticaltxt.config(font=("Agency FB", 11, 'bold'))

        self.verticaltxt.place(x=15, y=25, width=35, height=210)
        self.vertical.place(x=0, y=0, width=70, height=2000)
        self.horinzontal.place(x=0, y=0, width=2000, height=50)
        self.atl.place(x=70,y=15,width = 150,height = 30)
        self.dell.place(x=230,y=15,width = 150,height = 30)
        self.btref.place(x=400, y=15, width=30, height=30)

    def tabelcli(self):
        self.tabelacli= ttk.Treeview(self.app3, height=30,column=('col1', 'col2', 'col3', 'col4','col5'))
        self.tabelacli.heading('#0', text='')
        self.tabelacli.heading('#1', text='id')
        self.tabelacli.heading('#2', text='Nome do Cliente')
        self.tabelacli.heading('#3', text='CPF')
        self.tabelacli.heading('#4', text='Telefone')

        self.tabelacli.column('#0', width=1)
        self.tabelacli.column('#1', width=50)
        self.tabelacli.column('#2', width=100)
        self.tabelacli.column('#3', width=100)
        self.tabelacli.column('#4', width=100)

        self.tabelacli.place(x=75,y=55, width=390, height=200)

        self.barrarolagem2 = Scrollbar(self.app3, orient='vertical')
        self.tabelacli.configure(yscroll=self.barrarolagem2.set)
        self.barrarolagem2.place(x=466, y=55, width=15, height=200)

class atualizarcad(funcs):
    def __init__(self):
        self.tela4()
    def tela4(self):
        self.app4 = Toplevel()
        self.app4.title('Atualizar Cliente')
        self.app4.geometry('470x150')
        self.app4.resizable(False, False)
        self.app4.configure(background='#f8bdc6')
        self.app4.iconbitmap(r'mdchefeicon.ico')
        self.app4.transient(app)
        self.app4.focus_force()
        self.app4.grab_set()

        #Labels/Buttons
        self.cpfclitxt = Label(self.app4,text = 'Informe o CPF',background = '#f8bdc6', foreground= '#000')
        self.btbusc = Button(self.app4,text = 'Buscar', background = '#FFFFFF', foreground = '#000',command = self.buscacliat)
        self.nometxt = Label(self.app4, text='Nome do Cliente', background='#f8bdc6', foreground='#000')
        self.cpftxt = Label(self.app4, text='CPF do Cliente', background='#f8bdc6', foreground='#000')
        self.teltxt = Label(self.app4, text='TEL do Cliente', background='#f8bdc6', foreground='#000')
        self.horinzontal = Label(self.app4, background='#FFFFFF', foreground='#000')
        self.btatl = Button(self.app4, text='Atualizar Cadastro', background='#ffb6c1', foreground='#000',command = self.atucli)
        self.velhocpf = Label(self.app4, text='', background='#ffffff', foreground='#000')
        self.velhotel = Label(self.app4, text='', background='#ffffff', foreground='#000')
        self.velhonome = Label(self.app4, text='', background='#ffffff', foreground='#000')
        self.titulo = Label(self.app4, text='Antigo Registro', background='#f8bdc6', foreground='#000')

        #Inputs
        self.cpfclinpat = Entry(self.app4,background = '#FFFFFF', foreground = '#000')
        self.nomeinpat = Entry(self.app4, background='#FFFFFF', foreground='#000')
        self.cpfinpat = Entry(self.app4, background='#ffffff', foreground='#000')
        self.telinpat = Entry(self.app4, background='#FFFFFF', foreground='#000')

        #Configs
        self.cpfclitxt.config(font=('Calibri', 10, 'bold'))
        self.cpfclinpat.config(font=('Calibri', 10, 'bold'))
        self.btbusc.config(font=('Calibri', 10, 'bold'))
        self.nometxt.config(font=('Calibri', 10, 'bold'))
        self.cpftxt.config(font=('Calibri', 10, 'bold'))
        self.teltxt.config(font=('Calibri', 10, 'bold'))
        self.nomeinpat.config(font=('Calibri', 10, 'bold'))
        self.cpfinpat.config(font=('Calibri', 10, 'bold'))
        self.telinpat.config(font=('Calibri', 10, 'bold'))
        self.btatl.config(font=('Calibri', 10, 'bold'))
        self.velhotel.config(font=('Calibri', 10, 'bold'))
        self.velhocpf.config(font=('Calibri', 10, 'bold'))
        self.velhonome.config(font=('Calibri', 10, 'bold'))
        self.titulo.config(font=('Calibri', 10, 'bold'))

        #Place
        self.cpfclitxt.place(x=1,y=15,width=100,height=30)
        self.cpfclinpat.place(x=100,y=20,width=100,height=20)
        self.btbusc.place(x=205,y=20,width=50,height=20)
        self.nometxt.place(x=40, y=40, width=100, height=30)
        self.cpftxt.place(x=40, y=65, width=100, height=30)
        self.teltxt.place(x=40, y=89, width=100, height=30)
        self.nomeinpat.place(x=145, y=45, width=150, height=20)
        self.cpfinpat.place(x=145, y=70, width=150, height=20)
        self.telinpat.place(x=145, y=95, width=150, height=20)
        self.horinzontal.place(x=0, y=0, width=1000, height=15)
        self.btatl.place(x=50, y=120, width=400, height=20)
        self.velhonome.place(x=300, y=45, width=150, height=20)
        self.velhocpf.place(x=300, y=70, width=150, height=20)
        self.velhotel.place(x=300, y=95, width=150, height=20)
        self.titulo.place(x=325,y=15,width=100,height=30)

class deletarcad(funcs):
    def __init__(self):
        self.tela5()
    def tela5(self):
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
        self.cpfclitxt = Label(self.app5, text='Informe o CPF', background='#f8bdc6', foreground='#000')
        self.btbusc = Button(self.app5, text='Buscar', background='#FFFFFF', foreground='#000',command = self.buscacliat)
        self.nometxt = Label(self.app5, text='Nome do Cliente', background='#f8bdc6', foreground='#000')
        self.cpftxt = Label(self.app5, text='CPF do Cliente', background='#f8bdc6', foreground='#000')
        self.teltxt = Label(self.app5, text='TEL do Cliente', background='#f8bdc6', foreground='#000')
        self.horinzontal = Label(self.app5, background='#FFFFFF', foreground='#000')
        self.btatl = Button(self.app5, text='Deletar Cadastro', background='#ffb6c1', foreground='#000', command = self.deletarcadbusc)
        self.velhonome = Label(self.app5, text='', background='#ffffff', foreground='#000')
        self.velhocpf = Label(self.app5, text='', background='#ffffff', foreground='#000')
        self.velhotel = Label(self.app5, text='', background='#ffffff', foreground='#000')

        # Inputs
        self.cpfclinpat = Entry(self.app5, background='#FFFFFF', foreground='#000')

        # Configs
        self.cpfclitxt.config(font=('Calibri', 10, 'bold'))
        self.cpfclinpat.config(font=('Calibri', 10, 'bold'))
        self.btbusc.config(font=('Calibri', 10, 'bold'))
        self.nometxt.config(font=('Calibri', 10, 'bold'))
        self.cpftxt.config(font=('Calibri', 10, 'bold'))
        self.teltxt.config(font=('Calibri', 10, 'bold'))
        self.velhonome.config(font=('Calibri', 10, 'bold'))
        self.velhocpf.config(font=('Calibri', 10, 'bold'))
        self.velhotel.config(font=('Calibri', 10, 'bold'))
        self.btatl.config(font=('Calibri', 10, 'bold'))

        # Place
        self.cpfclitxt.place(x=1, y=15, width=100, height=30)
        self.cpfclinpat.place(x=100, y=20, width=100, height=20)
        self.btbusc.place(x=205, y=20, width=50, height=20)
        self.nometxt.place(x=40, y=40, width=100, height=30)
        self.cpftxt.place(x=40, y=65, width=100, height=30)
        self.teltxt.place(x=40, y=89, width=100, height=30)
        self.velhonome.place(x=145, y=45, width=150, height=20)
        self.velhocpf.place(x=145, y=70, width=150, height=20)
        self.velhotel.place(x=145, y=95, width=150, height=20)
        self.horinzontal.place(x=0, y=0, width=1000, height=15)
        self.btatl.place(x=50, y=120, width=250, height=20)

class agenda(funcs):
    def __init__(self):
        self.tela6()
    def tela6(self):
        self.app6 = Toplevel()
        self.app6.title('Agendar Horario')
        self.app6.geometry('315x215')
        self.app6.resizable(False, False)
        self.app6.iconbitmap(r'mdchefeicon.ico')
        self.app6.configure(background='#f8bdc6')
        self.app6.transient(app)
        self.app6.focus_force()
        self.app6.grab_set()

        # Labels/Buttons
        self.clinome = Label(self.app6,text='Nome do Cliente', background='#f8bdc6', foreground='#000')
        self.serv = Label(self.app6, text='Serviço', background='#f8bdc6', foreground='#000')
        self.atend = Label(self.app6, text='Nome do Atendente', background='#f8bdc6', foreground='#000')
        self.valor = Label(self.app6, text='Valor', background='#f8bdc6', foreground='#000')
        self.hora = Label(self.app6, text='Horario', background='#f8bdc6', foreground='#000')
        self.btagen = Button(self.app6, text='Realizar Agendamento', background='#ffb6c1', foreground='#000', command = self.realizaagn)
        self.horinzontal = Label(self.app6, background='#FFFFFF', foreground='#000')
        self.situtxt = Label(self.app6, text='Situação', background='#f8bdc6', foreground='#000')

        # Inputs
        self.clinomeinpag = Entry(self.app6,background='#FFFFFF', foreground='#000')
        self.servinpag = Entry(self.app6,background='#FFFFFF', foreground='#000')
        self.atendinpag = Entry(self.app6,background='#FFFFFF', foreground='#000')
        self.valorinpag = Entry(self.app6,background='#FFFFFF', foreground='#000')
        self.horainpag = Entry(self.app6,background='#FFFFFF', foreground='#000')
        self.situang = Entry(self.app6,background='#FFFFFF', foreground='#000')

        #Configs
        self.clinome.config(font=('Calibri', 10, 'bold'))
        self.serv.config(font=('Calibri', 10, 'bold'))
        self.atend.config(font=('Calibri', 10, 'bold'))
        self.valor.config(font=('Calibri', 10, 'bold'))
        self.hora.config(font=('Calibri', 10, 'bold'))
        self.btagen.config(font=('Calibri', 10, 'bold'))
        self.situang.config(font=('Calibri', 10, 'bold'))
        self.situtxt.config(font=('Calibri', 10, 'bold'))
        self.clinomeinpag.config(font=('Calibri', 10, 'bold'))
        self.servinpag.config(font=('Calibri', 10, 'bold'))
        self.atendinpag.config(font=('Calibri', 10, 'bold'))
        self.valorinpag.config(font=('Calibri', 10, 'bold'))
        self.horainpag.config(font=('Calibri', 10, 'bold'))

        #Places
        self.situtxt.place(x=5, y=150, width=150, height=20)
        self.situang.place(x=140, y=150, width=150, height=20)
        self.clinome.place(x=20,y=15,width=100,height=30)
        self.clinomeinpag.place(x=140,y=20,width=150, height=20)
        self.serv.place(x=20,y=40,width=100,height=30)
        self.servinpag.place(x=140,y=45,width=150, height=20)
        self.atend.place(x=20,y=65,width=110,height=30)
        self.atendinpag.place(x=140,y=70,width=150, height=20)
        self.valor.place(x=20,y=90,width=110,height=30)
        self.valorinpag.place(x=140,y=95,width=150, height=20)
        self.hora.place(x=20,y=115,width=110,height=30)
        self.horainpag.place(x=140,y=120,width=150, height=20)
        self.btagen.place(x=20, y=180, width=275, height=20)
        self.horinzontal.place(x=0, y=0, width=1000, height=15)

aplicativo()

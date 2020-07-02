from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import tix
from tkinter import ttk
import sqlite3

root = Tk()
# ----- BACK - END -----------
class funcs():
    def conectarBD(self):
        self.conn = sqlite3.connect('./tarefas.db')
        self.cursor = self.conn.cursor()
        print('Connecting DataBase................../')

    def desconectarBD(self):
        self.conn.close()
        print('Desconnecting DataBase.............../')

    def montarTabelaBD(self):
        self.conectarBD()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tarefas (
            code INTEGER PRIMARY KEY,
            titulo CHAR(50),
            descricao CHAR(200),
            prazo CHAR(20)       
            );
        """)

        self.conn.commit()
        print('DataBase has been Created............/')

        self.desconectarBD()

    def variaveisTarefa(self):
        self.titulo = self.tituloEntry.get()
        self.descricao = self.descricaoEntry.get('1.0', 'end')
        self.prazo = self.prazoEntry.get()

    def inserirTarefaNoBD(self):
        self.variaveisTarefa()
        self.conectarBD()

        self.cursor.execute("""
            INSERT INTO tarefas (titulo, descricao, prazo)
                VALUES (?, ?, ?);
        """, (self.titulo, self.descricao, self.prazo))

        self.desconectarBD()

    def mostrarTarefaAFazer(self):
        self.conectarBD()

        titulo = self.cursor.execute("""
            SELECT titulo FROM tarefas;
        """)


        self.tituloF1.insert(END, titulo)


        self.desconectarBD()
        self.windowpopup.destroy()

    def botaoSalvar(self):
        self.inserirTarefaNoBD()
        self.mostrarTarefaAFazer()

# ------ FRONT - END ---------
class Aplication(funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets()
        self.Menu()
        self.montarTabelaBD()
        self.root.mainloop()

    def tela(self):
        self.root.title('📜 Scrum Task Board')
        self.root.geometry('800x600')
        self.root.config(background='#c1c1c1')
        self.root.minsize(width=750, height=550)

    def frames(self):
        # To do;;;
        self.frame1 = Frame(self.root, bd=4, bg='#e0e0e0', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame1.place(relx=0.01, rely=0.1, relwidth=0.85, relheight=0.26)
        # ---
        self.tituloF1 = Entry(self.frame1, bd=0, bg='#e5e5e5',
                             fg='#0c0c0c', font=('Tahoma', 14, 'bold'),
                             justify='center')
        self.tituloF1.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.25)

        self.descricF1 = Text(self.frame1, bd=0, bg='#e5e5e5',
                             fg='#0c0c0c', font=('Tahoma', 13))
        self.descricF1.place(relx=0.02, rely=0.35, relwidth=0.5, relheight=0.5)

        self.prazoF1 = Entry(self.frame1, bd=0, bg='#e5e5e5',
                             fg='#0c0c0c', font=('Tahoma', 13), justify='center')
        self.prazoF1.place(relx=0.6, rely=0.5, relwidth=0.3, relheight=0.2)

        # =========================================================
        # Do;;;
        self.frame2 = Frame(self.root, bd=4, bg='#e0e0e0', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame2.place(relx=0.01, rely=0.4, relwidth=0.85, relheight=0.26)

        # ---
        self.tituloF2 = Entry(self.frame2, bd=0, bg='#e5e5e5',
                              fg='#0c0c0c', font=('Tahoma', 14, 'bold'),
                              justify='center')
        self.tituloF2.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.25)

        self.descricF2 = Text(self.frame2, bd=0, bg='#e5e5e5',
                              fg='#0c0c0c', font=('Tahoma', 13))
        self.descricF2.place(relx=0.02, rely=0.35, relwidth=0.5, relheight=0.5)

        self.prazoF2 = Entry(self.frame2, bd=0, bg='#e5e5e5',
                             fg='#0c0c0c', font=('Tahoma', 13), justify='center')
        self.prazoF2.place(relx=0.6, rely=0.5, relwidth=0.3, relheight=0.2)

        # =========================================================
        # Finish;;;
        self.frame3 = Frame(self.root, bd=4, bg='#e0e0e0', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame3.place(relx=0.01, rely=0.7, relwidth=0.85, relheight=0.26)

        # ---
        self.tituloF3 = Entry(self.frame3, bd=0, bg='#e5e5e5',
                              fg='#0c0c0c', font=('Tahoma', 14, 'bold'),
                              justify='center')
        self.tituloF3.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.25)

        self.descricF3 = Text(self.frame3, bd=0, bg='#e5e5e5',
                              fg='#0c0c0c', font=('Tahoma', 13))
        self.descricF3.place(relx=0.02, rely=0.35, relwidth=0.5, relheight=0.5)

        self.prazoF3 = Entry(self.frame3, bd=0, bg='#e5e5e5',
                             fg='#0c0c0c', font=('Tahoma', 13), justify='center')
        self.prazoF3.place(relx=0.6, rely=0.5, relwidth=0.3, relheight=0.2)

    def widgets(self):

        self.novobut = Button(self.root, text='Nova Tarefa', fg='#fff', font=('Tahoma', 11, 'bold'),
                              bd=0, bg='#0e5fef', activebackground='#aaeeff',
                              command=self.popUp)
        self.novobut.place(relx=0.01, rely=0.02, relwidth=0.85, relheight=0.06)
        # =========================================================
        # Botão Apagar Tarefa;;;
        self.apagarbut = Button(self.root, text='Apagar', fg='#fff', font=('Tahoma', 10, 'bold'),
                                bd=1, bg='#c02222', activebackground='#fe4422')
        self.apagarbut.place(relx=0.88, rely=0.12, relwidth=0.1, relheight=0.06)

        # =========================================================
        # Botão Fazer;;;
        self.fazerbut = Button(self.root, text='Fazer', fg='#fff', font=('Tahoma',10,'bold'),
                               bd=1, bg='#11c033', activebackground='#118844')
        self.fazerbut.place(relx=0.88, rely=0.28, relwidth=0.1, relheight=0.06)

        # =========================================================
        # Botão Feito;;;
        self.feitobut = Button(self.root, text='Feito', fg='#fff', font=('Tahoma', 10, 'bold'),
                               bd=1, bg='#118855', activebackground='#109933', activeforeground='#222222')
        self.feitobut.place(relx=0.88, rely=0.5, relwidth=0.1, relheight=0.06)

        # =========================================================
        # Botão ver O que já foi feito;
        self.prontasbut = Button(self.root, text='Ver o que\njá foi feito', fg='#0f0f0f', font=('Tahoma', 9, 'bold'),
                                 bd=1, bg='#e0e0e0', activebackground='lightblue',
                                 command=self.lista_Prontos)
        self.prontasbut.place(relx=0.88 , rely=0.88 , relwidth=0.1 , relheight=0.06)

    def popUp(self):
        self.windowpopup = Toplevel()
        self.windowpopup.title('📚 Nova Tarefa')
        self.windowpopup.geometry('500x300')
        self.windowpopup.config(background='#c5c5c5')
        self.windowpopup.resizable(False, False)
        self.windowpopup.transient(self.root)
        self.windowpopup.focus_force()
        self.windowpopup.grab_set()


        # ----- TITULO DA NOVA TAREFA ------------
        self.tituloTar = Label(self.windowpopup, text='Título', bg='#c5c5c5', font=('Tahoma', 14, 'bold'),
                                fg='#0c0c0c')
        self.tituloTar.place(relx=0.02,rely=0.09)

        self.tituloEntry = Entry(self.windowpopup, bg='#e0e0e0', borderwidth=0, font=('Tahoma', 12),
                                 fg='#0c0c0c', bd=1)
        self.tituloEntry.place(relx=0.02, rely=0.19, relwidth=0.96, relheight=0.1)

        # ------ CAIXA DE DESCRIÇÃO ----------
        self.descricaoTar = Label(self.windowpopup, text='Descrição', bg='#c5c5c5', font=('Tahoma', 14, 'bold'),
                               fg='#0c0c0c')
        self.descricaoTar.place(relx=0.02, rely=0.33)

        self.descricaoEntry = Text(self.windowpopup, bg='#e0e0e0', borderwidth=0,
                                 font=('Hack', 12), fg='#0c0c0c', bd=1)
        self.descricaoEntry.place(relx=0.02, rely=0.43, relwidth=0.5, relheight=0.4)

        # ------ DATA PRAZO ------
        self.prazo = Label(self.windowpopup, text='Prazo', bg='#c5c5c5', font=('Tahoma', 14, 'bold'),
                           fg='#0c0c0c')
        self.prazo.place(relx=0.62, rely=0.43)

        self.prazoEntry = Entry(self.windowpopup, bg='#e0e0e0', borderwidth=0, font=('Tahoma', 12),
                                fg='#0c0c0c', justify='center', bd=1)
        self.prazoEntry.place(relx=0.61, rely=0.53, relheight=0.1)

        # --- BOTÃO SALVAR ---
        self.salvar_bt = Button(self.windowpopup, text='Salvar', fg='#fff', font=('Tahoma', 10, 'bold'),
                               bd=1, bg='#118855', activebackground='#109933', activeforeground='#222222',
                                command=self.botaoSalvar)
        self.salvar_bt.place(relx=0.7, rely=0.73, relwidth=0.2, relheight=0.1)
    
    def lista_de_Tarefas(self):
        self.lista_tarefas = Toplevel()
        self.lista_tarefas.title('Lista de Tarefas')
        self.lista_tarefas.geometry('500x600')
        self.lista_tarefas.config(background='#c1c1c1')
        self.lista_tarefas.minsize(width=350, height=450)


        # --- LISTA DE TAREFAS ---
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", bd=0, font=('Tahoma', 11))
        self.style.configure("mystyle.Treeview.Heading", font=('Tahoma', 11, 'bold'))

        self.listaUser = ttk.Treeview(
            self.lista_tarefas, height=3,
            column=('col1', 'col2', 'col3', 'col4'),
            style='mystyle.Treeview'
        )
        self.listaUser.heading('#0', text='')
        self.listaUser.heading('#1', text='code')
        self.listaUser.heading('#2', text='Título')
        self.listaUser.heading('#3', text='Descrição')
        self.listaUser.heading('#4', text='Prazo')

        self.listaUser.column('#0', width=0)
        self.listaUser.column('#1', width=35)
        self.listaUser.column('#2', width=120)
        self.listaUser.column('#3', width=150)
        self.listaUser.column('#4', width=100)

        self.listaUser.place(relx=0.015, rely=0.15, relwidth=0.93, relheight=0.84)

        self.scrollLista = Scrollbar(self.lista_tarefas, orient='vertical')
        self.listaUser.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.95, rely=0.15, relwidth=0.035, relheight=0.84)

    def lista_Prontos(self):
        self.lista_tarefas_prontas = Toplevel()
        self.lista_tarefas_prontas.title('Tarefas Feitas 👍')
        self.lista_tarefas_prontas.geometry('500x600')
        self.lista_tarefas_prontas.config(background='#c5c5c5')
        self.lista_tarefas_prontas.minsize(width=490, height=590)
        self.lista_tarefas_prontas.focus_force()
        self.lista_tarefas_prontas.grab_set()

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", background='#b5b5b5', font=('Tahoma', 11))
        self.style.configure("mystyle.Treeview.Heading", bg='#b9b9b9', font=('Tahoma', 11, 'bold'))

        self.listaUser = ttk.Treeview(
            self.lista_tarefas_prontas, height=3,
            column=('col1', 'col2', 'col3', 'col4'),
            style='mystyle.Treeview'
        )
        self.listaUser.heading('#0', text='')
        self.listaUser.heading('#1', text='code')
        self.listaUser.heading('#2', text='Título')
        self.listaUser.heading('#3', text='Descrição')
        self.listaUser.heading('#4', text='Prazo')

        self.listaUser.column('#0', width=0)
        self.listaUser.column('#1', width=35)
        self.listaUser.column('#2', width=120)
        self.listaUser.column('#3', width=150)
        self.listaUser.column('#4', width=100)

        self.listaUser.place(relx=0.015, rely=0.15, relwidth=0.93, relheight=0.84)

        self.scrollLista = Scrollbar(self.lista_tarefas_prontas, orient='vertical')
        self.listaUser.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.95, rely=0.15, relwidth=0.035, relheight=0.84)

    def Menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu1 = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit():
            self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu1)
        menubar.add_cascade(label="Tarefas", menu=filemenu2)

        filemenu1.add_command(label="Sair", command=Quit)

        filemenu2.add_command(label='Lista de Tarefas', command=self.lista_de_Tarefas)



Aplication()

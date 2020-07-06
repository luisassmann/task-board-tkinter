from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import tix
from tkinter import ttk
import sqlite3
from server import *


root = Tk()

# ------ FRONT - END ---------
class Aplication(funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets()
        self.lista_de_Tarefas()
        self.montarTabelaBD()
        self.inserir_na_lista()
        self.root.mainloop()

    def tela(self):
        self.root.title('📜 Scrum Task Board')
        self.root.geometry('800x600')
        self.root.config(background='#c1c1c1')
        self.root.minsize(width=750, height=550)

    def frames(self):
        # Criação de duas tabelas Notebook para melhor organ. de espaço;;;
        self.abas = ttk.Notebook(self.root)
        self.tela_inicial = Frame(self.abas)
        self.lista_de_tarefas_ = Frame(self.abas)

        self.tela_inicial.configure(background="#c1c1c1")
        self.lista_de_tarefas_.configure(background='#c1c1c1')

        self.abas.add(self.tela_inicial, text='Painel')
        self.abas.add(self.lista_de_tarefas_, text='Lista de Tarefas')

        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)

        # To do;;;
        self.frame1 = Frame(self.tela_inicial, bd=4, bg='#e0e0e0', highlightthickness=3,
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
        self.frame2 = Frame(self.tela_inicial, bd=4, bg='#e0e0e0', highlightthickness=3,
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
        self.frame3 = Frame(self.tela_inicial, bd=4, bg='#e0e0e0', highlightthickness=3,
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

        # =========================================================
        # Segunda tela;;;

        self.frame4 = Frame(self.lista_de_tarefas_, bd=4, bg='#e5e5e5', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame4.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.35)


        self.frame5 = Frame(self.lista_de_tarefas_, bd=4, bg='#e5e5e5', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame5.place(relx=0.01, rely=0.38, relwidth=0.98, relheight=0.6)

    def widgets(self):

        self.novobut = Button(self.tela_inicial, text='Nova Tarefa', fg='#fff', font=('Roboto', 11, 'bold'),
                              bd=0, bg='#0e5fef', activebackground='#aaeeff',
                              command=self.popUp)
        self.novobut.place(relx=0.01, rely=0.02, relwidth=0.85, relheight=0.06)
        # =========================================================
        # Botão Apagar Tarefa;;;
        self.apagarbut = Button(self.tela_inicial, text='Apagar', fg='#fff', font=('Roboto', 10, 'bold'),
                                bd=1, bg='#c02222', activebackground='#fe4422')
        self.apagarbut.place(relx=0.88, rely=0.12, relwidth=0.1, relheight=0.06)

        # =========================================================
        # Botão Fazer;;;
        self.fazerbut = Button(self.tela_inicial, text='Fazer', fg='#fff', font=('Roboto',10,'bold'),
                               bd=1, bg='#11c033', activebackground='#118844')
        self.fazerbut.place(relx=0.88, rely=0.28, relwidth=0.1, relheight=0.06)

        # =========================================================
        # Botão Feito;;;
        self.feitobut = Button(self.tela_inicial, text='Feito', fg='#fff', font=('Roboto', 10, 'bold'),
                               bd=1, bg='#118855', activebackground='#109933', activeforeground='#222222')
        self.feitobut.place(relx=0.88, rely=0.5, relwidth=0.1, relheight=0.06)

        # =========================================================
        # Botão ver O que já foi feito;
        self.prontasbut = Button(self.tela_inicial, text='Ver o que\njá foi feito', fg='#0f0f0f', font=('Roboto', 9, 'bold'),
                                 bd=1, bg='#e0e0e0', activebackground='lightblue')
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
                                command=self.inserirTarefaNoBD)
        self.salvar_bt.place(relx=0.7, rely=0.73, relwidth=0.2, relheight=0.1)

    def lista_de_Tarefas(self):
        # --- LISTA DE TAREFAS ---
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", bd=0, font=('Tahoma', 11))
        self.style.configure("mystyle.Treeview.Heading", font=('Tahoma', 11, 'bold'))

        self.listaTarefas = ttk.Treeview(
            self.lista_de_tarefas_, height=3,
            column=('col1', 'col2', 'col3', 'col4'),
            style='mystyle.Treeview'
        )
        self.listaTarefas.heading('#0', text='')
        self.listaTarefas.heading('#1', text='code')
        self.listaTarefas.heading('#2', text='Título')
        self.listaTarefas.heading('#3', text='Descrição')
        self.listaTarefas.heading('#4', text='Prazo')

        self.listaTarefas.column('#0', width=0)
        self.listaTarefas.column('#1', width=35)
        self.listaTarefas.column('#2', width=120)
        self.listaTarefas.column('#3', width=150)
        self.listaTarefas.column('#4', width=100)

        self.listaTarefas.place(relx=0.03, rely=0.4, relwidth=0.93, relheight=0.55)

        self.scrollLista = Scrollbar(self.lista_de_tarefas_, orient='vertical')
        self.listaTarefas.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.945, rely=0.4, relwidth=0.035, relheight=0.55)

        self.listaTarefas.bind('<Double-1>', self.show_in_task)


Aplication()

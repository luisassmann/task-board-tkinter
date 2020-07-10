from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import tix
from tkinter import ttk
import sqlite3


root = Tk()
titulo = ''
tarefa_TODO = {
    "codigo": "",
    "titulo": "",
    "descricao": "",
    "prazo": ""
}

tarefa_DO = {
    "codigo": "",
    "titulo": "",
    "descricao": "",
    "prazo": ""
}

tarefa_DONE = {
    "codigo": "",
    "titulo": "",
    "descricao": "",
    "prazo": ""
}


class funcs():
    def limpar_NovaTarefa(self):
        self.entryTitulo.delete(0, END)
        self.entryDescricao.delete('1.0', 'end')
        self.entryPrazo.delete(0, END)

    def limpar_Lista_entrys(self):
        self.ListacodeEntry.delete(0, END)
        self.ListaTituloEntry.delete(0, END)
        self.ListaDescricaoEntry.delete('1.0', 'end')
        self.ListaPrazoEntry.delete(0, END)

    def conectarDB(self):
        self.conn = sqlite3.connect('./tarefas.db')
        self.cursor = self.conn.cursor()
        print('Banco de Dados Conectado............................../')

    def desconectarDB(self):
        self.cursor.close()
        print('Banco de Dados Desconectado.........................../')

    def montarTable(self):
        self.conectarDB()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                code INTEGER PRIMARY KEY,
                titulo CHAR(50) NOT NULL,
                descricao CHAR(200),
                prazo CHAR(40)
            );
        """)

        self.conn.commit()
        print('Banco de Dados Criado................................./')

        self.desconectarDB()

    def valores_Tarefa(self):
        self.code = self.ListacodeEntry.get()
        self.titulo = self.entryTitulo.get().strip().capitalize()
        self.descricao = self.entryDescricao.get('1.0', 'end').strip()
        self.prazo = self.entryPrazo.get().strip()

    def inserirTarefa_Lista(self):
        self.valores_Tarefa()
        self.conectarDB()

        aviso_msg = 'É Necessário colocar ao menos um título na tarefa! ⚠'

        if self.titulo == '' or len(self.titulo) <= 1:
            messagebox.showwarning('Sem Título - Aviso!', aviso_msg)

        else:
            self.cursor.execute("""
                INSERT INTO tarefas (titulo, descricao, prazo)
                    VALUES (?, ?, ?)
            """,
            (self.titulo, self.descricao, self.prazo))

        self.conn.commit()
        self.desconectarDB()
        self.limpar_NovaTarefa()
        print('Nova Tarefa Adicionada................................/')
        self.Colocar_na_Lista()

    def Colocar_na_Lista(self):
        self.listaTarefas.delete(*self.listaTarefas.get_children())
        self.conectarDB()

        lista = self.cursor.execute("""
            SELECT code, titulo, descricao, prazo FROM tarefas
                ORDER BY code ASC;
        """)

        for val in lista:
            self.listaTarefas.insert('', END, values=val)

        self.desconectarDB()
        print('Tarefa(s) está na lista.............................../')

        self.desconectarDB()

    def Selecionar_da_Lista(self, event):
        self.limpar_Lista_entrys()
        self.listaTarefas.selection()

        for dado in self.listaTarefas.selection():
            col1, col2, col3, col4 = self.listaTarefas.item(dado, 'values')
            self.ListacodeEntry.insert(END, col1)
            self.ListaTituloEntry.insert(END, col2)
            self.ListaDescricaoEntry.insert('1.0', col3)
            self.ListaPrazoEntry.insert(END, col4)

    def DeleteTarefaLista(self):
        self.valores_Tarefa()
        self.conectarDB()

        self.cursor.execute("""
            DELETE FROM tarefas WHERE code = ?
        """,(
            self.code
        ))
        self.conn.commit()

        self.desconectarDB()
        self.limpar_Lista_entrys()
        self.Colocar_na_Lista()
        print('Tarefa Deletada......................................./')

    def AlterarTarefaLista(self):
        self.codigo = self.ListacodeEntry.get()
        self.titulo = self.ListaTituloEntry.get().strip()
        self.descricao = self.ListaDescricaoEntry.get('1.0', 'end').strip()
        self.prazo = self.ListaPrazoEntry.get().strip()
        self.conectarDB()

        self.cursor.execute("""
            UPDATE tarefas SET titulo = ?, descricao = ?, prazo = ?
                WHERE code = ?;
        """,(self.titulo, self.descricao, self.prazo, self.codigo))

        self.conn.commit()

        self.limpar_Lista_entrys()
        self.Colocar_na_Lista()
        self.desconectarDB()

    def BuscarTarefaLista(self):
        self.conectarDB()
        self.listaTarefas.delete(*self.listaTarefas.get_children())


        self.ListaTituloEntry.insert(END, '%')
        titulo = self.ListaTituloEntry.get()

        self.cursor.execute("""
            SELECT code, titulo, descricao, prazo FROM tarefas
                WHERE titulo LIKE '%s' ORDER BY code ASC;
        """ % titulo)

        self.BuscaTarefa = self.cursor.fetchall()
        for t in self.BuscaTarefa:
            self.listaTarefas.insert('', END, values=t)


        self.limpar_Lista_entrys()
        self.desconectarDB()

    def colocar_no_Painel_1(self):
        self.lista = self.listaTarefas.get_children()

        i = 1
        for v in self.lista:
            listaV1 = self.listaTarefas.item(v)["values"]
            if i == 1:
                break

        for c in listaV1:
            tarefa_TODO[]

# ------ FRONT - END ---------
class Aplication(funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets()
        self.lista_de_Tarefas()
        self.montarTable()
        self.Colocar_na_Lista()
        self.colocar_no_Painel_1()
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
        self.novaTarefa = Frame(self.abas)
        self.lista_de_tarefas_ = Frame(self.abas)


        self.tela_inicial.configure(background="#c1c1c1")
        self.novaTarefa.configure(background="#c1c1c1")
        self.lista_de_tarefas_.configure(background='#c1c1c1')

        self.abas.add(self.tela_inicial, text='  PAINEL  ')
        self.abas.add(self.novaTarefa, text="   NOVA TAREFA   ")
        self.abas.add(self.lista_de_tarefas_, text='  LISTA DE TAREFAS  ')

        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)

        # To do;;;
        self.frame1 = Frame(self.tela_inicial, bd=4, bg='#e0e0e0', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame1.place(relx=0.01, rely=0.1, relwidth=0.85, relheight=0.26)
        # ---
        self.tituloF1 = Label(self.frame1, text=tarefa_TODO["titulo"], bg='#e5e5e5',
                             fg='#0c0c0c', font=('Roboto', 14, 'bold'),
                             justify='center')
        self.tituloF1.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.25)

        self.descricF1 = Label(self.frame1, text=tarefa_TODO["descricao"], bg='#e5e5e5',
                             fg='#0c0c0c', font=('Roboto', 13))
        self.descricF1.place(relx=0.02, rely=0.35, relwidth=0.5, relheight=0.5)

        self.prazoF1 = Label(self.frame1, text=tarefa_TODO["prazo"], bg='#e5e5e5',
                             fg='#0c0c0c', font=('Roboto', 13), justify='center')
        self.prazoF1.place(relx=0.6, rely=0.5, relwidth=0.3, relheight=0.2)

        # =========================================================
        # Do;;;
        self.frame2 = Frame(self.tela_inicial, bd=4, bg='#e0e0e0', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame2.place(relx=0.01, rely=0.4, relwidth=0.85, relheight=0.26)

        # ---
        self.tituloF2 = Label(self.frame2, text='', bg='#e5e5e5',
                              fg='#0c0c0c', font=('Roboto', 14, 'bold'),
                              justify='center')
        self.tituloF2.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.25)

        self.descricF2 = Label(self.frame2, text='', bg='#e5e5e5',
                              fg='#0c0c0c', font=('Roboto', 13))
        self.descricF2.place(relx=0.02, rely=0.35, relwidth=0.5, relheight=0.5)

        self.prazoF2 = Label(self.frame2, text='', bg='#e5e5e5',
                             fg='#0c0c0c', font=('Roboto', 13), justify='center')
        self.prazoF2.place(relx=0.6, rely=0.5, relwidth=0.3, relheight=0.2)

        # =========================================================
        # Finish;;;
        self.frame3 = Frame(self.tela_inicial, bd=4, bg='#e0e0e0', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame3.place(relx=0.01, rely=0.7, relwidth=0.85, relheight=0.26)

        # ---
        self.tituloF3 = Label(self.frame3, text='', bg='#e5e5e5',
                              fg='#0c0c0c', font=('Roboto', 14, 'bold'),
                              justify='center')
        self.tituloF3.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.25)

        self.descricF3 = Label(self.frame3, text='', bg='#e5e5e5',
                              fg='#0c0c0c', font=('Roboto', 13))
        self.descricF3.place(relx=0.02, rely=0.35, relwidth=0.5, relheight=0.5)

        self.prazoF3 = Label(self.frame3, text='', bg='#e5e5e5',
                             fg='#0c0c0c', font=('Roboto', 13), justify='center')
        self.prazoF3.place(relx=0.6, rely=0.5, relwidth=0.3, relheight=0.2)

        # =========================================================
        # LISTA DE TAREFAS;;;

        self.frame4 = Frame(self.lista_de_tarefas_, bd=4, bg='#e5e5e5', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame4.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.35)


        self.Listacode = Label(self.frame4, text='code', bg='#e5e5e5',
                               font=('Roboto', 12))
        self.Listacode.place(relx=0.018, rely=0.01)
        self.ListacodeEntry = Entry(self.frame4, borderwidth=0, bg='#c4c4c4', fg='#000',
                                    font=('Roboto', 12, 'bold'), justify='center')
        self.ListacodeEntry.place(relx=0.018, rely=0.15, relwidth=0.05, relheight=0.14)


        self.ListaTitulo = Label(self.frame4, text='Título', bg='#e5e5e5',
                                 font=('Roboto', 12))
        self.ListaTitulo.place(relx=0.1, rely=0.01)
        self.ListaTituloEntry = Entry(self.frame4, borderwidth=1, bg='#fff', fg='#000',
                                      font=('Roboto', 12))
        self.ListaTituloEntry.place(relx=0.088, rely=0.15, relwidth=0.72, relheight=0.14)


        self.ListaDescricao = Label(self.frame4, text='Descrição', bg='#e5e5e5',
                                 font=('Roboto', 12))
        self.ListaDescricao.place(relx=0.03, rely=0.3)
        self.ListaDescricaoEntry = Text(self.frame4, borderwidth=1, bg='#fff', fg='#000',
                                      font=('Roboto', 12))
        self.ListaDescricaoEntry.place(relx=0.01, rely=0.44, relwidth=0.5, relheight=0.5)


        self.ListaPrazo = Label(self.frame4, text='Prazo', bg='#e5e5e5',
                                 font=('Roboto', 12))
        self.ListaPrazo.place(relx=0.55, rely=0.3)
        self.ListaPrazoEntry = Entry(self.frame4, borderwidth=1, bg='#fff', fg='#000',
                                      font=('Roboto', 12))
        self.ListaPrazoEntry.place(relx=0.53, rely=0.44, relwidth=0.28, relheight=0.14)


        self.alterar_botao = Button(self.frame4, text='Alterar', bd=1, bg='#115599',
                                    font=('Roboto', 12, 'bold'), fg='#fff',
                                    command=self.AlterarTarefaLista)
        self.alterar_botao.place(relx=0.84, rely=0.1, relwidth=0.14, relheight=0.2)


        self.buscar_botao = Button(self.frame4, text='Buscar', bd=1, bg='#11c099',
                                    font=('Roboto', 12, 'bold'), fg='#fff',
                                   command=self.BuscarTarefaLista)
        self.buscar_botao.place(relx=0.84, rely=0.4, relwidth=0.14, relheight=0.2)


        self.limpar_botao = Button(self.frame4, text='Limpar', bd=1, bg='#a0a0a0',
                                    font=('Roboto', 12, 'bold'), fg='#222222',
                                   command=self.limpar_Lista_entrys)
        self.limpar_botao.place(relx=0.84, rely=0.7, relwidth=0.14, relheight=0.2)


        self.apagar_botao = Button(self.frame4, text='Apagar', bd=1, bg='#c02222',
                                   font=('Roboto', 12, 'bold'), fg='#fff',
                                   command=self.DeleteTarefaLista)
        self.apagar_botao.place(relx=0.6, rely=0.7, relwidth=0.14, relheight=0.2)


        self.frame5 = Frame(self.lista_de_tarefas_, bd=4, bg='#e5e5e5', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame5.place(relx=0.01, rely=0.38, relwidth=0.98, relheight=0.6)

        # NOVA TAREFA ;;;
        self.frame6 = Frame(self.novaTarefa, bd=4, bg='#e0e009', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame6.place(relx=0.15, rely=0.07, relwidth=0.7, relheight=0.15)

        self.labNova_Tarefa = Label(self.frame6, text='Nova Tarefa', bg='#e0e009',
                                    font=('Bradley Hand ITC', 36))
        self.labNova_Tarefa.place(relx=0.3, rely=0.03)



        self.frame7 = Frame(self.novaTarefa, bd=4, bg='#e0e0e0', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame7.place(relx=0.15, rely=0.23, relwidth=0.7, relheight=0.5)



        self.labelTitulo = Label(self.frame7, text='Título', bg='#e0e0e0',
                                 font=('Roboto', 14))
        self.labelTitulo.place(relx=0.08, rely=0.03)
        self.entryTitulo = Entry(self.frame7, borderwidth=1, bg='#fff', fg='#000',
                                 font=('Roboto', 12))
        self.entryTitulo.place(relx=0.05, rely=0.13, relwidth=0.9, relheight=0.1)


        self.labelDescricao = Label(self.frame7, text='Descrição', bg='#e0e0e0',
                                 font=('Roboto', 14))
        self.labelDescricao.place(relx=0.08, rely=0.3)
        self.entryDescricao = Text(self.frame7, borderwidth=1, bg='#fff', fg='#000',
                                 font=('Roboto', 12))
        self.entryDescricao.place(relx=0.05, rely=0.4, relwidth=0.55, relheight=0.4)


        self.labelPrazo = Label(self.frame7, text='Prazo', bg='#e0e0e0',
                                font=('Roboto', 14))
        self.labelPrazo.place(relx=0.65, rely=0.3)
        self.entryPrazo = Entry(self.frame7, borderwidth=1, bg='#fff', fg='#000',
                                font=('Roboto', 12))
        self.entryPrazo.place(relx=0.65, rely=0.4, relwidth=0.3, relheight=0.1)

        # ----------------------
        # ========= BOTÃO SALVAR
        self.Salvar = Button(self.frame7, text='Salvar', bd=1, bg='#33ff66', fg='#000',
                             font=('Roboto', 12, 'bold'), activebackground='blue',
                             command=self.inserirTarefa_Lista)
        self.Salvar.place(relx=0.65, rely=0.64, relwidth=0.3, relheight=0.15)

    def widgets(self):

        self.novobut = Button(self.tela_inicial, text='TAREFAS', fg='#fff', font=('Roboto', 11, 'bold'),
                              bd=0, bg='#0e5fef', activebackground='#aaeeff',
                              command=self.novaTarefa)
        self.novobut.place(relx=0.01, rely=0.02, relwidth=0.85, relheight=0.06)
        # =========================================================
        # Botão Apagar Tarefa;;;
        self.apagarbut = Button(self.tela_inicial, text='Apagar', fg='#fff', font=('Roboto', 11, 'bold'),
                                bd=1, bg='#c02222', activebackground='#fe4422')
        self.apagarbut.place(relx=0.88, rely=0.12, relwidth=0.1, relheight=0.06)

        # =========================================================
        # Botão Fazer;;;
        self.fazerbut = Button(self.tela_inicial, text='Fazer', fg='#fff', font=('Roboto',11,'bold'),
                               bd=1, bg='#11c033', activebackground='#118844')
        self.fazerbut.place(relx=0.88, rely=0.28, relwidth=0.1, relheight=0.06)

        # =========================================================
        # Botão Feito;;;
        self.feitobut = Button(self.tela_inicial, text='Feito', fg='#fff', font=('Roboto', 11, 'bold'),
                               bd=1, bg='#118855', activebackground='#109933', activeforeground='#222222')
        self.feitobut.place(relx=0.88, rely=0.5, relwidth=0.1, relheight=0.06)

    def lista_de_Tarefas(self):
        # --- LISTA DE TAREFAS ---
        self.style = ttk.Style()
        self.style.theme_use('vista')
        self.style.configure("mystyle.Treeview", bd=0, font=('Roboto', 12),
                             fieldbackground='#c1c1c1')
        self.style.configure("mystyle.Treeview.Heading", font=('Roboto', 14, 'bold'))
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

        self.listaTarefas = ttk.Treeview(
            self.lista_de_tarefas_, height=3,
            column=('col1', 'col2', 'col3', 'col4'),
            style='mystyle.Treeview'
        )
        self.listaTarefas.tag_configure('odd', background='#E8E8E8')
        self.listaTarefas.tag_configure('even', background='#DFDFDF')
        self.listaTarefas.heading('#0', text='##')
        self.listaTarefas.heading('#1', text='code')
        self.listaTarefas.heading('#2', text='Título')
        self.listaTarefas.heading('#3', text='Descrição')
        self.listaTarefas.heading('#4', text='Prazo')

        self.listaTarefas.column('#0', width=1)
        self.listaTarefas.column('#1', width=30, anchor='center')
        self.listaTarefas.column('#2', width=120)
        self.listaTarefas.column('#3', width=180)
        self.listaTarefas.column('#4', width=100, anchor='center')

        self.listaTarefas.place(relx=0.03, rely=0.4, relwidth=0.93, relheight=0.55)

        self.scrollLista = Scrollbar(self.lista_de_tarefas_, orient='vertical')
        self.listaTarefas.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.945, rely=0.4, relwidth=0.035, relheight=0.55)

        self.listaTarefas.bind('<Double-1>', self.Selecionar_da_Lista)


Aplication()

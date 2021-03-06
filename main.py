from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import tix
from tkinter import ttk
import sqlite3
from src.funcs import *
from src.cache import *

root = Tk()

class Aplication(funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets()
        self.lista_de_Tarefas()
        self.lista_tarefas_prontas_()
        self.montarTable()
        self.montar_tabela_prontas()
        self.Colocar_na_Lista()
        self.colocar_lista_prontas()
        self.Tarefa_a_fazer()
        self.Tarefa_fazendo()
        self.Tarefa_feita()
        self.show_in_frame_1()
        self.root.mainloop()

    def tela(self):
        self.root.title('📜 Task Board')
        self.root.geometry('800x600')
        self.root.config(background='#c1c1c1')
        self.root.minsize(width=750, height=550)

    def frames(self):
        # Criação de duas tabelas Notebook para melhor organ. de espaço;;;
        self.abas = ttk.Notebook(self.root)
        
        self.tela_inicial = Frame(self.abas)
        self.novaTarefa = Frame(self.abas)
        self.lista_de_tarefas_ = Frame(self.abas)
        self.lista_tarefas_prontas = Frame(self.abas)


        self.tela_inicial.configure(background="#c1c1c1")
        self.novaTarefa.configure(background="#c1c1c1")
        self.lista_de_tarefas_.configure(background='#c1c1c1')
        self.lista_tarefas_prontas.configure(background='#c1c1c1')

        self.abas.add(self.tela_inicial, text='  PAINEL  ')
        self.abas.add(self.novaTarefa, text="   ==> NOVA TAREFA <==   ")
        self.abas.add(self.lista_de_tarefas_, text='  LISTA DE TAREFAS  ')
        self.abas.add(self.lista_tarefas_prontas, text='  TAREFAS CONCLUÍDAS  ')

        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)

        # To do;;;
        self.frame1 = Frame(self.tela_inicial, bd=4, bg='#e0e0e0', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame1.place(relx=0.01, rely=0.08, relwidth=0.85, relheight=0.26)
        # ---

        # =========================================================
        # Do;;;
        self.frame2 = Frame(self.tela_inicial, bd=4, bg='#e0e0e0', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame2.place(relx=0.01, rely=0.405, relwidth=0.85, relheight=0.26)

        # ---

        # =========================================================
        # Finish;;;
        self.frame3 = Frame(self.tela_inicial, bd=4, bg='#e0e0e0', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame3.place(relx=0.01, rely=0.73, relwidth=0.85, relheight=0.26)
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

        # ------------------------------------------------
        self.frame_prontas = Frame(self.lista_tarefas_prontas, bd=4, bg='#e5e5e5', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame_prontas.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.35)
        # ================================================================================
        self.label_code_prontas = Label(self.frame_prontas, text="code", bg='#e5e5e5',
                                        font=('Roboto', 12))
        self.label_code_prontas.place(relx=0.018, rely=0.01)
        self.entry_code_prontas = Entry(self.frame_prontas, borderwidth=0, bg='#c4c4c4', fg='#000',
                                    font=('Roboto', 12, 'bold'), justify='center')
        self.entry_code_prontas.place(relx=0.018, rely=0.15, relwidth=0.05, relheight=0.14)


        self.label_tit_prontas = Label(self.frame_prontas, text='Título', bg='#e5e5e5',
                                 font=('Roboto', 12))
        self.label_tit_prontas.place(relx=0.1, rely=0.01)
        self.entry_tit_prontas = Entry(self.frame_prontas, borderwidth=1, bg='#fff', fg='#000',
                                      font=('Roboto', 12))
        self.entry_tit_prontas.place(relx=0.088, rely=0.15, relwidth=0.72, relheight=0.14)


        self.label_desc_prontas = Label(self.frame_prontas, text='Descrição', bg='#e5e5e5',
                                 font=('Roboto', 12))
        self.label_desc_prontas.place(relx=0.03, rely=0.3)
        self.entry_desc_prontas = Text(self.frame_prontas, borderwidth=1, bg='#fff', fg='#000',
                                      font=('Roboto', 12))
        self.entry_desc_prontas.place(relx=0.01, rely=0.44, relwidth=0.5, relheight=0.5)


        self.label_prazo_prontas = Label(self.frame_prontas, text='Prazo', bg='#e5e5e5',
                                 font=('Roboto', 12))
        self.label_prazo_prontas.place(relx=0.55, rely=0.3)
        self.entry_prazo_prontas = Entry(self.frame_prontas, borderwidth=1, bg='#fff', fg='#000',
                                      font=('Roboto', 12))
        self.entry_prazo_prontas.place(relx=0.53, rely=0.44, relwidth=0.28, relheight=0.14)


        self.buscar_botao_prontas = Button(self.frame_prontas, text='Buscar', bd=1, bg='#11c099',
                                    font=('Roboto', 12, 'bold'), fg='#fff', 
                                    command=self.buscar_tar_pronta)
        self.buscar_botao_prontas.place(relx=0.84, rely=0.1, relwidth=0.14, relheight=0.2)


        self.limpar_botao_prontas = Button(self.frame_prontas, text='Limpar', bd=1, bg='#a0a0a0',
                                    font=('Roboto', 12, 'bold'), fg='#222222',
                                    command=self.limpar_prontas_entrys)
        self.limpar_botao_prontas.place(relx=0.84, rely=0.4, relwidth=0.14, relheight=0.2)


        self.apagar_botao_prontas = Button(self.frame_prontas, text='Excluir Definitivamente', bd=1, bg='#c02222',
                                   font=('Roboto', 12, 'bold'), fg='#fff', 
                                   command=self.excluir_pronta)
        self.apagar_botao_prontas.place(relx=0.6, rely=0.7, relwidth=0.38, relheight=0.2)


        # ================================================================================
        self.frame_ta_prontas = Frame(self.lista_tarefas_prontas, bd=4, bg='#e5e5e5', highlightthickness=3,
                                highlightbackground='#556666')
        self.frame_ta_prontas.place(relx=0.01, rely=0.38, relwidth=0.98, relheight=0.6)

    def widgets(self):
        self.afazerbut = Button(self.tela_inicial, text='A Fazer', fg='#fff', font=('Roboto', 11, 'bold'),
                              bd=0, bg='#0e5fef', activebackground='#aaeeff')
        self.afazerbut.place(relx=0.01, rely=0.018, relwidth=0.85, relheight=0.06)
        self.progressobut = Button(self.tela_inicial, text='Em Progresso', fg='#fff', font=('Roboto', 11, 'bold'),
                              bd=0, bg='#0e5fef', activebackground='#aaeeff')
        self.progressobut.place(relx=0.01, rely=0.3425, relwidth=0.85, relheight=0.06)
        self.feitosbut = Button(self.tela_inicial, text='Feito', fg='#fff', font=('Roboto', 11, 'bold'),
                              bd=0, bg='#0e5fef', activebackground='#aaeeff')
        self.feitosbut.place(relx=0.01, rely=0.6677, relwidth=0.85, relheight=0.06)
        # =========================================================
        # Botão Apagar Tarefa;;;
        self.apagarbut = Button(self.tela_inicial, text='Apagar', fg='#fff', font=('Roboto', 11, 'bold'),
                                bd=1, bg='#c02222', activebackground='#fe4422',
                                command=self.apagar_tarefa_tela_ini)
        self.apagarbut.place(relx=0.88, rely=0.12, relwidth=0.1, relheight=0.06)

        # =========================================================
        # Botão Fazer;;;
        self.fazerbut = Button(self.tela_inicial, text='Fazer', fg='#fff', font=('Roboto',11,'bold'),
                               bd=1, bg='#11c033', activebackground='#118844',
                               command=self.goto_frame_2)
        self.fazerbut.place(relx=0.88, rely=0.28, relwidth=0.1, relheight=0.06)

        # =========================================================
        # Botão Feito;;;
        self.feitobut = Button(self.tela_inicial, text='Feito', fg='#fff', font=('Roboto', 11, 'bold'),
                               bd=1, bg='#118855', activebackground='#109933', activeforeground='#222222',
                               command=self.goto_frame_3)
        self.feitobut.place(relx=0.88, rely=0.5, relwidth=0.1, relheight=0.06)

        # ====================================
        # Botão Sair;;;
        self.sairbut = Button(self.tela_inicial, text='Sair', fg='#fff', font=('Roboto', 11, 'bold'),
                               bd=1, bg='#e03232', activebackground='#109933', activeforeground='#222222',
                               command=self.root.destroy)
        self.sairbut.place(relx=0.88, rely=0.92, relwidth=0.1, relheight=0.06)

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
            column=('col1', 'col2', 'col3', 'col4', 'col5'),
            style='mystyle.Treeview'
        )
        self.listaTarefas.tag_configure('odd', background='#E8E8E8')
        self.listaTarefas.tag_configure('even', background='#DFDFDF')
        self.listaTarefas.heading('#0', text='##')
        self.listaTarefas.heading('#1', text='code')
        self.listaTarefas.heading('#2', text='Título')
        self.listaTarefas.heading('#3', text='Descrição')
        self.listaTarefas.heading('#4', text='Prazo')
        self.listaTarefas.heading('#5', text='Status')

        self.listaTarefas.column('#0', width=1)
        self.listaTarefas.column('#1', width=30, anchor='center')
        self.listaTarefas.column('#2', width=120)
        self.listaTarefas.column('#3', width=180)
        self.listaTarefas.column('#4', width=75, anchor='center')
        self.listaTarefas.column('#5', width=25)

        self.listaTarefas.place(relx=0.03, rely=0.4, relwidth=0.93, relheight=0.55)

        self.scrollLista = Scrollbar(self.lista_de_tarefas_, orient='vertical')
        self.listaTarefas.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.945, rely=0.4, relwidth=0.035, relheight=0.55)

        self.listaTarefas.bind('<Double-1>', self.Selecionar_da_Lista)

    def lista_tarefas_prontas_(self):
        # --- LISTA DE TAREFAS ---
        self.style = ttk.Style()
        self.style.theme_use('vista')
        self.style.configure("mystyle.Treeview", bd=0, font=('Roboto', 12),
                             fieldbackground='#c1c1c1')
        self.style.configure("mystyle.Treeview.Heading", font=('Roboto', 14, 'bold'))
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

        self.listaTarefas_prontas = ttk.Treeview(
            self.lista_tarefas_prontas, height=3,
            column=('col1', 'col2', 'col3', 'col4', 'col5'),
            style='mystyle.Treeview'
        )
        self.listaTarefas_prontas.tag_configure('odd', background='#E8E8E8')
        self.listaTarefas_prontas.tag_configure('even', background='#DFDFDF')
        self.listaTarefas_prontas.heading('#0', text='##')
        self.listaTarefas_prontas.heading('#1', text='code')
        self.listaTarefas_prontas.heading('#2', text='Título')
        self.listaTarefas_prontas.heading('#3', text='Descrição')
        self.listaTarefas_prontas.heading('#4', text='Prazo')
        self.listaTarefas_prontas.heading('#5', text='Status')

        self.listaTarefas_prontas.column('#0', width=1)
        self.listaTarefas_prontas.column('#1', width=30, anchor='center')
        self.listaTarefas_prontas.column('#2', width=120)
        self.listaTarefas_prontas.column('#3', width=180)
        self.listaTarefas_prontas.column('#4', width=75, anchor='center')
        self.listaTarefas_prontas.column('#5', width=25)

        self.listaTarefas_prontas.place(relx=0.03, rely=0.4, relwidth=0.93, relheight=0.55)

        self.scrollLista = Scrollbar(self.lista_tarefas_prontas, orient='vertical')
        self.listaTarefas_prontas.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.945, rely=0.4, relwidth=0.035, relheight=0.55)

        self.listaTarefas_prontas.bind('<Double-1>', self.selecionar_tarefas_prontas)

    def Tarefa_a_fazer(self):
        self.tituloF1 = Entry(self.frame1, bg='#e0e0e0',
                              fg='#0c0c0c', font=('Roboto', 14, 'bold'),
                              justify='center', bd=0)
        self.tituloF1.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.25)

        self.descricF1 = Text(self.frame1, bg='#e0e0e0', borderwidth=0,
                               fg='#0c0c0c', font=('Roboto', 13))
        self.descricF1.place(relx=0.02, rely=0.35, relwidth=0.5, relheight=0.5)

        self.prazoF1 = Entry(self.frame1, bg='#e0e0e0',
                             fg='#0c0c0c', font=('Roboto', 13), justify='center', bd=0)
        self.prazoF1.place(relx=0.6, rely=0.5, relwidth=0.3, relheight=0.2)

    def Tarefa_fazendo(self):
        self.variaveis_tarefas()
        self.tituloF2 = Entry(self.frame2, bg='#e0e0e0',
                              fg='#0c0c0c', font=('Roboto', 14, 'bold'),
                              justify='center', bd=0)
        self.tituloF2.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.25)

        self.descricF2 = Text(self.frame2, bg='#e0e0e0', borderwidth=0,
                               fg='#0c0c0c', font=('Roboto', 13))
        self.descricF2.place(relx=0.02, rely=0.35, relwidth=0.5, relheight=0.5)

        self.prazoF2 = Entry(self.frame2, bg='#e0e0e0',
                             fg='#0c0c0c', font=('Roboto', 13), justify='center', bd=0)
        self.prazoF2.place(relx=0.6, rely=0.5, relwidth=0.3, relheight=0.2)

    def Tarefa_feita(self):
        self.tituloF3 = Entry(self.frame3, bg='#e0e0e0',
                              fg='#0c0c0c', font=('Roboto', 14, 'bold'),
                              justify='center', bd=0)
        self.tituloF3.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.25)

        self.descricF3 = Text(self.frame3, bg='#e0e0e0', borderwidth=0,
                               fg='#0c0c0c', font=('Roboto', 13))
        self.descricF3.place(relx=0.02, rely=0.35, relwidth=0.5, relheight=0.5)

        self.prazoF3 = Entry(self.frame3, bg='#e0e0e0',
                             fg='#0c0c0c', font=('Roboto', 13), justify='center', bd=0)
        self.prazoF3.place(relx=0.6, rely=0.5, relwidth=0.3, relheight=0.2)


Aplication()

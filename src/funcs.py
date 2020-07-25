# Aqui vou colocar todas as funções do back-end;;;

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import tix
from tkinter import ttk
import sqlite3
from src.cache import *

class funcs(task):
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
        #print('Banco de Dados Conectado............................../')

    def desconectarDB(self):
        self.cursor.close()
        #print('Banco de Dados Desconectado.........................../')

    def montarTable(self):
        self.conectarDB()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                code INTEGER PRIMARY KEY,
                titulo CHAR(50) NOT NULL,
                descricao CHAR(200),
                prazo CHAR(40),
                status CHAR(20)
            );
        """)

        self.conn.commit()
        #print('Banco de Dados Criado................................./')

        self.desconectarDB()

    def valores_Tarefa(self):
        self.code = self.ListacodeEntry.get()
        self.titulo = self.entryTitulo.get().strip().capitalize()
        self.descricao = self.entryDescricao.get('1.0', 'end').strip()
        self.prazo = self.entryPrazo.get().strip()
        self.status = '0'

    def inserirTarefa_Lista(self):
        self.valores_Tarefa()
        self.conectarDB()

        aviso_msg = 'É Necessário colocar ao menos um título na tarefa! ⚠'

        if self.titulo == '' or len(self.titulo) <= 1:
            messagebox.showwarning('Sem Título - Aviso!', aviso_msg)

        else:
            self.cursor.execute("""
                INSERT INTO tarefas (titulo, descricao, prazo, status)
                    VALUES (?, ?, ?, ?)
            """,
            (self.titulo, self.descricao, self.prazo, self.status))

        self.conn.commit()
        self.desconectarDB()
        self.limpar_NovaTarefa()
        #print('Nova Tarefa Adicionada................................/')
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
        #print('Tarefa(s) está na lista.............................../')

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
        #print('Tarefa Deletada......................................./')

    def AlterarTarefaLista(self):
        self.codigo = self.ListacodeEntry.get()
        self.titulo = self.ListaTituloEntry.get().strip()
        self.descricao = self.ListaDescricaoEntry.get('1.0', 'end').strip()
        self.prazo = self.ListaPrazoEntry.get().strip()
        self.conectarDB()

        self.cursor.execute("""
            UPDATE tarefas SET titulo = ?, descricao = ?, prazo = ?
                WHERE code = ?;
        """, (self.titulo, self.descricao, self.prazo, self.codigo))

        self.conn.commit()

        self.limpar_Lista_entrys()
        self.Colocar_na_Lista()
        self.desconectarDB()
        self.colocar_no_Painel_1()

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

    def show_in_frame_1(self):
        self.conectarDB()
        self.variaveis_tarefas()

        self.cursor.execute("""
            SELECT code, titulo, descricao, prazo, status FROM tarefas
                ORDER BY code ASC;
        """)
        registro = self.cursor.fetchall()
        lista_of_1 = []
        x = 1
        for c in registro:
            if c[4] == '0':
                c[4] == '1'
            lista_of_1 = c[:]
            #print(len(c))
            if x == 1:
                break
        
        #print(lista_of_1)
        
        # the order of lista_of_1 => 0 == code;; 1 == titulo;; 2 == descricao;;
        # 3 == descricao;; 4 == status;;;
        self.tarefa_TODO["codigo"] = lista_of_1[0]
        self.tarefa_TODO["titulo"] = lista_of_1[1]
        self.tarefa_TODO["descricao"] = lista_of_1[2]
        self.tarefa_TODO["prazo"] = lista_of_1[3]
        self.tarefa_TODO["status"] = lista_of_1[4]

        

        self.desconectarDB()

    def goto_frame_2(self):
        # Transfer the values of the tarefa_TODO to tarefa_DO;;
        self.variaveis_tarefas()
        
        # --------------------------------
        self.tarefa_DO["codigo"] = self.tarefa_TODO["codigo"]
        self.tarefa_DO["titulo"] = self.tarefa_TODO["titulo"]
        self.tarefa_DO["descricao"] = self.tarefa_TODO["descricao"]
        self.tarefa_DO["prazo"] = self.tarefa_TODO["prazo"]
        self.tarefa_DO["status"] = self.tarefa_TODO["status"]

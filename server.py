import sqlite3
from tkinter import *


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

        self.conn.commit()
        self.inserir_na_lista()
        self.desconectarBD()

    def inserir_na_lista(self):
        self.listaTarefas.delete(*self.listaTarefas.get_children())
        self.conectarBD()

        lista = self.cursor.execute("""
            SELECT code, titulo, descricao, prazo FROM tarefas
            ORDER BY code ASC;
        """)

        for tar in lista:
            self.listaTarefas.insert("", END, values=tar)

        self.desconectarBD()

    def show_in_task(self, event):
        self.listaTarefas.selection()

        for t in self.listaTarefas.selection():
            col1, col2, col3, col4 = self.listaTarefas.item(t, 'values')
            self.tituloF1.insert(END, col2)
            self.descricF1.insert('1.0', col3)
            self.prazoF1.insert(END, col4)


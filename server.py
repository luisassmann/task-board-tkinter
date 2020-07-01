"""
Here is a local to config a database.
"""
from tkinter import *
import sqlite3


class database():
    def limpar(self):
        self.tituloF1.delete(0, END)
        self.descricF1.delete('1.0', 'end')
        self.prazoF1.delete(0, END)

    def conectarDB(self):
        self.conn = sqlite3.connect('./tasks.db')
        self.cursor = self.conn.cursor()
        print('Conectando ao Banco de Dados...')

    def desconectarDB(self):
        self.conn.close()
        print('Desconectando o Banco de Dados...')


    def montaTabelas(self):
        self.conectarDB()

        # -- Criação da Tabela --

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                code INTEGER PRIMARY KEY,
                titulo CHAR(40) NOT NULL,
                telefone,
                prazo
            );
        """)

        self.conn.commit(), print("Banco de Dados Criado...")
        self.desconectarDB()



class funcs(database):
    def toF1(self):
        self.titulo = self.tituloEntry.get()
        self.descri = self.descricaoEntry.get('1.0', 'end')
        self.data = self.prazoEntry.get()

        self.tituloF1.delete(0, END)
        self.tituloF1.insert(0, )

        self.descricF1.delete('1.0', 'end')
        self.descricF1.insert('1.0', )

        self.prazoF1.delete(0, END)
        self.prazoF1.insert(0, )

        self.windowpopup.destroy()

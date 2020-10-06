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

    def limpar_F1(self):
        # Clean the entrys;;
        self.tituloF1.delete(0, END)
        self.descricF1.delete('1.0', 'end')
        self.prazoF1.delete(0, END)

    def limpar_F2(self):
        self.tituloF2.delete(0, END)
        self.descricF2.delete('1.0', 'end')
        self.prazoF2.delete(0, END)

    def limpar_F3(self):
        self.tituloF3.delete(0, END)
        self.descricF3.delete('1.0', 'end')
        self.prazoF3.delete(0, END)

    def conectarDB(self):
        self.conn = sqlite3.connect('./tarefas.db')
        self.cursor = self.conn.cursor()

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

    def valores_tar_prontas(self):
        self.code_pro = self.entry_code_prontas.get()
        self.titulo_pro = self.entry_tit_prontas.get().strip()
        self.desc_pro = self.entry_desc_prontas.get('1.0', 'end')
        self.prazo_pro = self.entry_prazo_prontas.get()

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
        self.Colocar_na_Lista()

    def Colocar_na_Lista(self):
        self.listaTarefas.delete(*self.listaTarefas.get_children())
        self.conectarDB()

        lista = self.cursor.execute("""
            SELECT code, titulo, descricao, prazo, status FROM tarefas
                ORDER BY code ASC;
        """)

        for val in lista:
            self.listaTarefas.insert('', END, values=val)

        self.desconectarDB()

    def Selecionar_da_Lista(self, event):
        self.limpar_Lista_entrys()
        self.listaTarefas.selection()

        for dado in self.listaTarefas.selection():
            col1, col2, col3, col4, col5 = self.listaTarefas.item(dado, 'values')
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
        self.show_in_frame_1()

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
        self.show_in_frame_1()

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

    def conectar_prontasDB(self):
        self.conn_prontas = sqlite3.connect('./prontas.db')
        self.cursor_prontas = self.conn_prontas.cursor()

    def desconectar_prontasDB(self):
        self.cursor_prontas.close()

    def montar_tabela_prontas(self):
        self.conectar_prontasDB()

        self.cursor_prontas.execute("""
            CREATE TABLE IF NOT EXISTS prontas (
                code INTEGER PRIMARY KEY,
                titulo CHAR(50) NOT NULL,
                descricao CHAR(200),
                prazo CHAR(40),
                status CHAR(20)
            );
        """)

        self.desconectar_prontasDB()

    def colocar_lista_prontas(self):
        self.listaTarefas_prontas.delete(*self.listaTarefas_prontas.get_children())
        self.conectar_prontasDB()

        lista = self.cursor_prontas.execute("""
            SELECT code, titulo, descricao, prazo, status FROM prontas
                ORDER BY code ASC;
        """)

        for val in lista:
            self.listaTarefas_prontas.insert('', END, values=val)

        self.desconectar_prontasDB()

    def limpar_prontas_entrys(self):
        self.entry_code_prontas.delete(0, END)
        self.entry_tit_prontas.delete(0, END)
        self.entry_desc_prontas.delete('1.0', 'end')
        self.entry_prazo_prontas.delete(0, END)

    def selecionar_tarefas_prontas(self, event):
        self.limpar_prontas_entrys()
        self.listaTarefas_prontas.selection()

        for valor in self.listaTarefas_prontas.selection():
            col1, col2, col3, col4, col5 = self.listaTarefas_prontas.item(valor, 'value')
            self.entry_code_prontas.insert(END, col1)
            self.entry_tit_prontas.insert(END, col2)
            self.entry_desc_prontas.insert('1.0', col3)
            self.entry_prazo_prontas.insert(END, col4)

    def excluir_pronta(self):
        self.valores_tar_prontas()
        self.conectar_prontasDB()

        self.cursor_prontas.execute("""
            DELETE FROM prontas WHERE code = ?;
        """, (self.code_pro,))
        self.conn_prontas.commit()

        self.limpar_prontas_entrys()
        self.desconectar_prontasDB()
        self.colocar_lista_prontas()

    def buscar_tar_pronta(self):
        self.conectar_prontasDB()
        self.listaTarefas_prontas.delete(*self.listaTarefas_prontas.get_children())

        self.entry_tit_prontas.insert(END, '%')
        titulo = self.entry_tit_prontas.get()

        self.cursor_prontas.execute("""
            SELECT code, titulo, descricao, prazo FROM prontas
                WHERE titulo LIKE '%s' ORDER BY code ASC;
        """ % titulo)

        self.BuscaTarefa = self.cursor_prontas.fetchall()
        for t in self.BuscaTarefa:
            self.listaTarefas_prontas.insert('', END, values=t)


        self.limpar_prontas_entrys()
        self.desconectar_prontasDB()

    def show_in_frame_1(self):
        self.conectarDB()
        self.variaveis_tarefas()
        self.Tarefa_a_fazer()
        self.limpar_F1()
        
        self.cursor.execute("""
            SELECT code, titulo, descricao, prazo, status FROM tarefas
                ORDER BY code ASC;
        """)
        registro = self.cursor.fetchall()
        self.lista_of_1 = []
        x = 1
        for c in registro:
            if c[4] == '0':
                c[4] == '1'
            self.lista_of_1 = c[:]
            if x == 1:
                break

        self.tarefa_TODO["codigo"] = self.lista_of_1[0]
        self.tarefa_TODO["titulo"] = self.lista_of_1[1]
        self.tarefa_TODO["descricao"] = self.lista_of_1[2]
        self.tarefa_TODO["prazo"] = self.lista_of_1[3]
        self.tarefa_TODO["status"] = self.lista_of_1[4]

        self.tituloF1.insert(END, self.tarefa_TODO["titulo"])
        self.descricF1.insert('1.0', self.tarefa_TODO["descricao"])
        self.prazoF1.insert(END, self.tarefa_TODO["prazo"])
        self.desconectarDB()

    def goto_frame_2(self):
        self.show_in_frame_1()
        self.Tarefa_fazendo()

        self.conectarDB()
        self.cursor.execute("""
            SELECT code, titulo, descricao, prazo, status FROM tarefas
                ORDER BY code ASC;
        """)
        registro = self.cursor.fetchall()
        self.lista_of_2 = []
        x = 1
        for c in registro:
            if c[4] == '0':
                c[4] == '1'
            self.lista_of_2 = c[:]
            if x == 1:
                break
        self.desconectarDB()

        self.limpar_F1()
        self.limpar_F2()

        self.tituloF2.insert(END, self.lista_of_2[1])
        self.descricF2.insert('1.0', self.lista_of_2[2])
        self.prazoF2.insert(END, self.lista_of_2[3])
        
        self.conectarDB()

        self.cursor.execute("""
            SELECT * FROM tarefas WHERE code = ?;
        """, (self.lista_of_2[0] + 1,))

        self.lista_of_3 = self.cursor.fetchone()
        self.desconectarDB()

        self.limpar_F1()
        self.tituloF1.insert(END, self.lista_of_3[1])
        self.descricF1.insert('1.0', self.lista_of_3[2])
        self.prazoF1.insert(END, self.lista_of_3[3])

    def goto_frame_3(self):
        self.show_in_frame_1()
        self.goto_frame_2()
        self.Tarefa_feita()

        self.limpar_F3()

        self.tituloF3.insert(END, self.lista_of_2[1])
        self.descricF3.insert('1.0', self.lista_of_2[2])
        self.prazoF3.insert(END, self.lista_of_2[3])

        self.limpar_F2()

        self.tituloF2.insert(END, self.lista_of_3[1])
        self.descricF2.insert('1.0', self.lista_of_3[2])
        self.prazoF2.insert(END, self.lista_of_3[3])

        self.limpar_F1()

        self.conectarDB()
        self.cursor.execute("""
            SELECT * FROM tarefas WHERE code = ?;
        """, (self.lista_of_3[0] + 1,))
        self.lista_of_4 = self.cursor.fetchone()
        self.desconectarDB()
        
        self.tituloF1.insert(END, self.lista_of_4[1])
        self.descricF1.insert('1.0', self.lista_of_4[2])
        self.prazoF1.insert(END, self.lista_of_4[3])

        # Inserir a tarefa feita no banco de dados 'prontas.db';;;
        # Os dados da tarefa feita esta na lista 'self.lista_of_2';;;
        self.conectar_prontasDB()

        self.cursor_prontas.execute("""
            INSERT INTO prontas (titulo, descricao, prazo, status)
                VALUES(?, ?, ?, ?)
        """,
        (self.lista_of_2[1], self.lista_of_2[2], self.lista_of_2[3], self.lista_of_2[4]))
        self.conn_prontas.commit()

        self.desconectar_prontasDB()

        # Deletar a tarefa feita da lista de tarefas principal;;;
        self.conectarDB()
        self.cursor.execute("""
            DELETE FROM tarefas WHERE code = ?
        """, (self.lista_of_2[0],))
        self.conn.commit()
        self.desconectarDB()
        self.Colocar_na_Lista()
        self.colocar_lista_prontas()

    def apagar_tarefa_tela_ini(self):
        # Possível mudança desse método para não mudar a legibilidade
        # Das telas
        self.show_in_frame_1()
        self.conectarDB()

        self.cursor.execute("""
            DELETE FROM tarefas WHERE code = ?;
            """, (self.lista_of_1[0],))
        self.conn.commit()

        self.Colocar_na_Lista()
        self.show_in_frame_1()
        self.desconectarDB()
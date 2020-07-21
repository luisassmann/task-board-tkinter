from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import tix
from tkinter import ttk
import sqlite3

# Is only for template this funcs;;;
class task():
    def padrao_tarefas(self):
        self.tarefaF1 = {
            "codigo": "",
            "titulo": "Adicione uma tarefa",
            "descricao": "Vá para guia NOVA TAREFA\npreencha os campos\ne salve-a",
            "prazo": "^_~",
            "status": '0'
        }

        self.tarefaF2 = {
            "codigo": "",
            "titulo": "",
            "descricao": "",
            "prazo": "",
            "status": '0'
        }

        self.tarefaF3 = {
            "codigo": "",
            "titulo": "",
            "descricao": "",
            "prazo": "",
            "status": '0'
        }

    def variaveis_tarefas(self):
        self.tarefa_TODO = {
            "codigo": "",
            "titulo": "",
            "descricao": "",
            "prazo": "",
            "status": '0'
        }

        self.tarefa_DO = {
            "codigo": "ff",
            "titulo": "",
            "descricao": "",
            "prazo": "",
            "status": '0'
        }

        self.tarefa_DONE = {
            "codigo": "",
            "titulo": "",
            "descricao": "",
            "prazo": "",
            "status": '0'
        }
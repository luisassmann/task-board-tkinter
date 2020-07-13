from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import tix
from tkinter import ttk
import sqlite3

# Is only for template this funcs;;;
class task():
    def variaveis_tarefas(self):
        self.tarefa_TODO = {
            "codigo": "",
            "titulo": "",
            "descricao": "",
            "prazo": ""
        }

        self.tarefa_DO = {
            "codigo": "",
            "titulo": "",
            "descricao": "",
            "prazo": ""
        }

        self.tarefa_DONE = {
            "codigo": "",
            "titulo": "",
            "descricao": "",
            "prazo": ""
        }
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import tix
from tkinter import ttk

root = Tk()

class novaTar():
    def __init__(self):
        self.root = root
        self.tela()
        self.Nova_Tarefa()
        self.root.mainloop()

    def tela(self):
        self.root.title('📚 Nova Tarefa')
        self.root.geometry('500x300')
        self.root.config(background='#c5c5c5')
        self.root.resizable(False, False)

    def Nova_Tarefa(self):

        # ----- TITULO DA NOVA TAREFA ------------
        self.tituloTar = Label(self.root, text='Título', bg='#c5c5c5', font=('Tahoma', 14, 'bold'),
                               fg='#0c0c0c')
        self.tituloTar.place(relx=0.02, rely=0.09)

        self.tituloEntry = Entry(self.root, bg='#e0e0e0', borderwidth=0, font=('Tahoma', 12),
                                 fg='#0c0c0c', bd=1)
        self.tituloEntry.place(relx=0.02, rely=0.19, relwidth=0.96, relheight=0.1)

        # ------ CAIXA DE DESCRIÇÃO ----------
        self.descricaoTar = Label(self.root, text='Descrição', bg='#c5c5c5', font=('Tahoma', 14, 'bold'),
                                  fg='#0c0c0c')
        self.descricaoTar.place(relx=0.02, rely=0.33)

        self.descricaoEntry = Text(self.root, bg='#e0e0e0', borderwidth=0,
                                   font=('Hack', 12), fg='#0c0c0c', bd=1)
        self.descricaoEntry.place(relx=0.02, rely=0.43, relwidth=0.5, relheight=0.4)

        # ------ DATA PRAZO ------
        self.prazo = Label(self.root, text='Prazo', bg='#c5c5c5', font=('Tahoma', 14, 'bold'),
                           fg='#0c0c0c')
        self.prazo.place(relx=0.62, rely=0.43)

        self.prazoEntry = Entry(self.root, bg='#e0e0e0', borderwidth=0, font=('Tahoma', 12),
                                fg='#0c0c0c', justify='center', bd=1)
        self.prazoEntry.place(relx=0.61, rely=0.53, relheight=0.1)

        # --- BOTÃO SALVAR ---
        self.salvar_bt = Button(self.root, text='Salvar', fg='#fff', font=('Tahoma', 10, 'bold'),
                                bd=1, bg='#118855', activebackground='#109933', activeforeground='#222222')
        self.salvar_bt.place(relx=0.7, rely=0.73, relwidth=0.2, relheight=0.1)

novaTar()
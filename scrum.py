from tkinter import *
from PIL import ImageTk, Image

root = Tk()

class Aplication():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets()
        self.root.mainloop()

    def tela(self):
        self.root.title('Scrum Task Board')
        self.root.geometry('800x600')
        self.root.config(background='#668899')
        self.root.minsize(width=750, height=550)

    def frames(self):
        # To do;;;
        self.frame1 = Frame(self.root,
                            bd=4,
                            bg='#223333',
                            highlightthickness=3,
                            highlightbackground='#556666')
        self.frame1.place(relx=0.01,
                          rely=0.01,
                          relwidth=0.85,
                          relheight=0.26)
        # =========================================================
        # Do;;;
        self.frame2 = Frame(self.root,
                            bd=4,
                            bg='#223333',
                            highlightthickness=3,
                            highlightbackground='#556666')
        self.frame2.place(relx=0.01,
                          rely=0.33,
                          relwidth=0.85,
                          relheight=0.26)
        # =========================================================
        # Finish;;;
        self.frame3 = Frame(self.root,
                            bd=4,
                            bg='#223333',
                            highlightthickness=3,
                            highlightbackground='#556666')
        self.frame3.place(relx=0.01,
                          rely=0.66,
                          relwidth=0.85,
                          relheight=0.26)

    def widgets(self):
        # Botão Apagar Tarefa;;;
        self.apagarbut = Button(self.root,
                                text='Apagar',
                                fg='#fff',
                                font=(
                                    'arial',
                                    10,
                                    'bold'
                                ),
                                bd=4,
                                bg='#442222',
                                activebackground='#fe4422')
        self.apagarbut.place(relx=0.88,
                             rely=0.02,
                             relwidth=0.1,
                             relheight=0.06)

        # =========================================================
        # Botão Fazer;;;
        self.fazerbut = Button(self.root,
                               text='Fazer',
                               fg='#fff',
                               font=(
                                   'arial',
                                   10,
                                   'bold'
                               ),
                               bd=4,
                               bg='#114433',
                               activebackground='#118844')
        self.fazerbut.place(relx=0.88,
                            rely=0.18,
                            relwidth=0.1,
                            relheight=0.06)

        # =========================================================
        # Botão Feito;;;
        self.feitobut = Button(self.root,
                               text='Feito',
                               fg='#fff',
                               font=(
                                   'arial',
                                   10,
                                   'bold'
                               ),
                               bd=4,
                               bg='#118855',
                               activebackground='#109933',
                               activeforeground='#222222')
        self.feitobut.place(relx=0.88,
                            rely=0.425,
                            relwidth=0.1,
                            relheight=0.06)


Aplication()

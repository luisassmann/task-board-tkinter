from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# ------ BACK - END ----------


# ------ FRONT - END ---------
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
                          rely=0.1,
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
                          rely=0.4,
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
                          rely=0.7,
                          relwidth=0.85,
                          relheight=0.26)

    def widgets(self):
        # Botão Novo:
        self.novobut = Button(self.root,
                              text='Novo',
                              fg='#fff',
                              font=(
                                  'arial',
                                  11,
                                  'bold'
                              ),
                              bd=0,
                              bg='#225588',
                              activebackground='#aaeeff',
                              command=self.popUp)
        self.novobut.place(relx=0.01,
                             rely=0.02,
                             relwidth=0.85,
                             relheight=0.06)
        # =========================================================
        # Botão Apagar Tarefa;;;
        self.apagarbut = Button(self.root,
                                text='Apagar',
                                fg='#fff',
                                font=(
                                    'arial',
                                    10,
                                    'bold'
                                ),
                                bd=1,
                                bg='#442222',
                                activebackground='#fe4422')
        self.apagarbut.place(relx=0.88,
                             rely=0.12,
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
                               bd=1,
                               bg='#114433',
                               activebackground='#118844')
        self.fazerbut.place(relx=0.88,
                            rely=0.28,
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
                               bd=1,
                               bg='#118855',
                               activebackground='#109933',
                               activeforeground='#222222')
        self.feitobut.place(relx=0.88,
                            rely=0.5,
                            relwidth=0.1,
                            relheight=0.06)

    def popUp(self):
        self.windowpopup = Toplevel()
        self.windowpopup.title('Nova Tarefa')
        self.windowpopup.geometry('500x300')
        self.windowpopup.config(background='#668899')
        self.windowpopup.minsize(width=450, height=250)


        # -----
        self.tituloTar = Label(self.windowpopup,
                                text='Título',
                                bg='#668899',
                                font=(
                                    'arial',
                                    14,
                                    'bold'
                                ),
                                fg='#003355')
        self.tituloTar.place(relx=0.02,
                            rely=0.09)

        self.tituloEntry = Entry(self.windowpopup,
                                 bg='#eeeeff',
                                 borderwidth=0,
                                 font=(
                                     'arial',
                                     12,
                                 ),
                                 fg='#003355',
                                 )
        self.tituloEntry.place(relx=0.02,
                               rely=0.19,
                               relwidth=0.96,
                               relheight=0.1)


Aplication()

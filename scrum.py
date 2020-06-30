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
        self.root.config(background='#141414')
        self.root.minsize(width=750, height=550)

    def frames(self):
        # To do;;;
        self.frame1 = Frame(self.root, bd=4, bg='#223333', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame1.place(relx=0.01, rely=0.1, relwidth=0.85, relheight=0.26)

        self.tituloF = Entry(self.frame1, text='miss', bd=0, bg='#223344',
                             fg='#fff', font=('arial', 14, 'bold'),
                             justify='center')
        self.tituloF.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.25)

        # =========================================================
        # Do;;;
        self.frame2 = Frame(self.root, bd=4, bg='#223333', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame2.place(relx=0.01, rely=0.4, relwidth=0.85, relheight=0.26)
        # =========================================================
        # Finish;;;
        self.frame3 = Frame(self.root, bd=4, bg='#223333', highlightthickness=3,
                            highlightbackground='#556666')
        self.frame3.place(relx=0.01, rely=0.7, relwidth=0.85, relheight=0.26)

    def widgets(self):
        # Botão Novo:
        self.novobut = Button(self.root, text='Novo', fg='#fff', font=('arial', 11, 'bold'),
                              bd=0, bg='#225588', activebackground='#aaeeff',
                              command=self.popUp)
        self.novobut.place(relx=0.01, rely=0.02, relwidth=0.85, relheight=0.06)
        # =========================================================
        # Botão Apagar Tarefa;;;
        self.apagarbut = Button(self.root, text='Apagar', fg='#fff', font=('arial', 10, 'bold'),
                                bd=1, bg='#442222', activebackground='#fe4422')
        self.apagarbut.place(relx=0.88, rely=0.12, relwidth=0.1, relheight=0.06)

        # =========================================================
        # Botão Fazer;;;
        self.fazerbut = Button(self.root, text='Fazer', fg='#fff', font=('arial',10,'bold'),
                               bd=1, bg='#114433', activebackground='#118844')
        self.fazerbut.place(relx=0.88, rely=0.28, relwidth=0.1, relheight=0.06)

        # =========================================================
        # Botão Feito;;;
        self.feitobut = Button(self.root, text='Feito', fg='#fff', font=('arial', 10, 'bold'),
                               bd=1, bg='#118855', activebackground='#109933', activeforeground='#222222')
        self.feitobut.place(relx=0.88, rely=0.5, relwidth=0.1, relheight=0.06)

    def popUp(self):
        self.windowpopup = Toplevel()
        self.windowpopup.title('Nova Tarefa')
        self.windowpopup.geometry('500x300')
        self.windowpopup.config(background='#141414')
        self.windowpopup.resizable(False, False)
        self.windowpopup.transient(self.root)
        self.windowpopup.focus_force()
        self.windowpopup.grab_set()


        # ----- TITULO DA NOVA TAREFA ------------
        self.tituloTar = Label(self.windowpopup, text='Título', bg='#141414', font=('arial', 14, 'bold'),
                                fg='#fff')
        self.tituloTar.place(relx=0.02,rely=0.09)

        self.tituloEntry = Entry(self.windowpopup, bg='#223333', borderwidth=0, font=('arial', 12),
                                 fg='#c4c4c4', bd=1)
        self.tituloEntry.place(relx=0.02, rely=0.19, relwidth=0.96, relheight=0.1)

        # ------ CAIXA DE DESCRIÇÃO ----------
        self.descricaoTar = Label(self.windowpopup, text='Descrição', bg='#141414', font=('arial', 14, 'bold'),
                               fg='#fff')
        self.descricaoTar.place(relx=0.02, rely=0.33)

        self.descricaoEntry = Text(self.windowpopup, bg='#223333', borderwidth=0,
                                 font=('Hack', 12), fg='#c4c4c4', bd=1)
        self.descricaoEntry.place(relx=0.02, rely=0.43, relwidth=0.5, relheight=0.4)

        # ------ DATA PRAZO ------
        self.prazo = Label(self.windowpopup, text='Prazo', bg='#141414', font=('arial', 14, 'bold'),
                           fg='#fff')
        self.prazo.place(relx=0.62, rely=0.43)

        self.prazoEntry = Entry(self.windowpopup, bg='#223333', borderwidth=0, font=('arial', 12),
                                fg='#c4c4c4', justify='center', bd=1)
        self.prazoEntry.place(relx=0.61, rely=0.53, relheight=0.1)

        # --- BOTÃO SALVAR ---
        self.salvar_bt = Button(self.windowpopup, text='Salvar', fg='#fff', font=('arial', 10, 'bold'),
                               bd=1, bg='#118855', activebackground='#109933', activeforeground='#222222')
        self.salvar_bt.place(relx=0.7, rely=0.73, relwidth=0.2, relheight=0.1)


Aplication()

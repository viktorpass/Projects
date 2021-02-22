from tkinter import *
import os
from tkinter import messagebox

class Application:
    def __init__(self,master=None):
        self.container = Frame(master)
        self.container["pady"] = 20
        self.container.pack()

        # NOME
        self.msg = Label(self.container,text = "SHUTDOWN MACHINE")
        self.msg["font"] = ("arial","20","bold")
        self.msg.pack(side = TOP)

        # TEXTO PARA O INPUT
        self.timeLabel = Label(self.container,text = "\n QUANTOS MINUTOS PARA O SHUTDOWN? \n")
        self.timeLabel["font"] = ("arial","14")
        self.timeLabel.pack(side = TOP)

        # COLETA DE DADOS
        self.time = Entry(self.container)
        self.time["width"] = 25
        self.time.pack()

        #BOTAO CANCEL
        self.cancel = Button(self.container)
        self.cancel["text"] = "CANCEL SHUTDOWN"
        self.cancel["font"] = ("arial", "10")
        self.cancel["command"] = self.stop_shutdown
        self.cancel.pack(side = BOTTOM)

        # IMAGEM
        self.imagem = PhotoImage(file="scoppey.png")
        self.imag = Label(self.container, image=self.imagem)
        self.imag.pack(side=BOTTOM)

        #BOTAO DE INPUT
        self.enter = Button(self.container)
        self.enter["text"] = "ENTER SHUTDOWN"
        self.enter["font"] = ("arial","10")
        self.enter["command"] = self.shutdown
        self.enter.pack()

    #FUNCAO DESLIGAR
    def shutdown(self):
        time = self.time.get()
        time = int(time)
        time_final = (60 * time)
        os.system(f'shutdown -s -t {time_final}')
        messagebox.showinfo("SHUTDOWN MACHINE","SCOPPEY MIOJO ESTARÁ DESLIGANDO O SEU COMPUTADOR")

    #FUNCAO CANCELAR SHUTDOWN
    def stop_shutdown(self):
        os.system("shutdown -a")
        messagebox.showinfo("SHUTDOWN MACHINE", "SCOPPEY MIOJO CANCELOU O SHUTDOWN")





root = Tk()
Application(root)
root.mainloop()
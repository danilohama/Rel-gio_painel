from datetime import datetime
from tkinter import *



def painel():
    app = Tk()
    app.geometry("440x180")
    app.title("Relógio HCC ")
    app.resizable(width=FALSE, height=FALSE)
    app.config(background='yellow')

    def cronometro():    
        tempo = datetime.now()    
        hora = tempo.strftime("%H:%M:%S")
        dia_semana = tempo.strftime("%A")
        dia = tempo.day
        mes = tempo.strftime("%B")
        ano = tempo.strftime("%Y")

        L1.config(text=hora, background="yellow")
        L1.after(200, cronometro)

        L2.config(text=dia_semana + " " +str(dia) + " / " + str(mes)+ " / " + str(ano), background="yellow")
        
    L1 = Label(app, text="",font=("DIGITALDREAMFATSKEW 80"))
    L1.grid(row=1, column=0, sticky=NW, padx=5)

    L2 = Label(app, text="",font=("Arial 20"))
    L2.grid(row=0, column=0, sticky=NW, padx=5)

    cronometro()
    
    app.mainloop()
painel()
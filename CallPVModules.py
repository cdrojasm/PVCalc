import tkinter
from tkinter import *
from tkinter import ttk


raiz=Tk()
raiz.title("PVCalcTool")
raiz.iconbitmap("Isotipo.ico")
raiz.config(bg="white",width="400",height='400')

def CalcPV():
    HSP=int(LocEnt_1.get())
    TEMP=int(LocEnt_2.get())
    Label1.config(text=str(HSP+TEMP))

PVModNames = ('Jinko Solar 535Wp','Jinko Solar 200Wp','Jinko Solar 900Wp','Jinko Solar 125Wp')

MainTit = Label (raiz,text="Calculo de sistemas Solares")
LocEnt_1 = Entry(raiz)
LocEnt_2 = Entry(raiz)

SelectPV=tkinter.StringVar()
PVOpt = ttk.Combobox(raiz, textvariable=SelectPV)
PVOpt ['values'] = PVModNames
PVOpt ['state'] = 'readonly'
PVOpt.pack(fill='x', padx = 5, pady = 5)

Label1 = Label(raiz,text="Primera Linea")
CalcBot=Button(raiz,text="Calculo \n PV System",command=CalcPV)

MainTit.pack()
LocEnt_1.pack()
LocEnt_2.pack()
Label1.pack()
CalcBot.pack()


raiz.mainloop()


from tkinter import *
from tkinter import messagebox
from controller import funciones

#Interfaz o view
def int_principal():
    ventana=Tk()
    ventana.title("Calculadora básica")
    ventana.geometry("600x400")
    ventana.resizable(False,False)

    n1=IntVar()
    n2=IntVar()
    numero1=Entry(ventana,textvariable=n1,width=5,justify="right")
    numero1.pack(side="top",anchor="center")

    numero2=Entry(ventana,textvariable=n2,width=5,justify="right")
    numero2.pack(side="top",anchor="center")

    btn_suma=Button(ventana,text=" + ",command=lambda: funciones.operaciones(n1.get(),n2.get(),"+"))
    btn_suma.pack()

    btn_resta=Button(ventana,text=" - ",command=lambda: funciones.operaciones(n1.get(),n2.get(),"-"))
    btn_resta.pack()

    btn_mult=Button(ventana,text=" * ",command=lambda: funciones.operaciones(n1.get(),n2.get(),"x"))
    btn_mult.pack()

    btn_division=Button(ventana,text=" / ",command=lambda: funciones.operaciones(n1.get(),n2.get(),"/"))
    btn_division.pack()

    btn_salir=Button(ventana,text="salir",command=ventana.quit)
    btn_salir.pack()

    ventana.mainloop()
"""
Crear una calculadora:
1.-  Dos campos de texto
2.-  4 botones para las operaciones
3.-  mostrar el resultado en una alerta
"""
from tkinter import *
from tkinter import messagebox

#Control de la aplicacion o Controller
def operaciones(n1,n2,signo):
    if signo=="+":
        ope=n1+n2
        tipo="Suma"
    elif signo=="-":
        ope=n1-n2
        tipo="Resta"
    elif signo=="x":
        ope=n1*n2
        tipo="Multiplicacion"
    elif signo=="/":
        ope=n1/n2
        tipo="Division"
    messagebox.showinfo(title=tipo,message=f"{n1}{signo}{n2} = {ope}")


#Interfaz o view
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

btn_suma=Button(ventana,text=" + ",command=lambda: operaciones(n1.get(),n2.get(),"+"))
btn_suma.pack()

btn_resta=Button(ventana,text=" - ",command=lambda: operaciones(n1.get(),n2.get(),"-"))
btn_resta.pack()

btn_mult=Button(ventana,text=" * ",command=lambda: operaciones(n1.get(),n2.get(),"x"))
btn_mult.pack()

btn_division=Button(ventana,text=" / ",command=lambda: operaciones(n1.get(),n2.get(),"/"))
btn_division.pack()

btn_salir=Button(ventana,text="salir",command=ventana.quit)
btn_salir.pack()

ventana.mainloop()
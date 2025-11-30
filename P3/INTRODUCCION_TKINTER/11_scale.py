from tkinter import *

def mostrar():
    resultado.config(text=f"Valor seleccionado por el usuario: {valor.get()}")

ventana=Tk()
ventana.title("Scale")
ventana.geometry("500x500")

valor=IntVar()
escala=Scale(ventana,from_=0, to=100, orient="horizontal",variable=valor)
escala.pack()

btn_mostrar=Button(ventana,text="Mostrar valor",command=mostrar)
btn_mostrar.pack()

resultado=Label(ventana,text="")
resultado.pack()

ventana.mainloop()
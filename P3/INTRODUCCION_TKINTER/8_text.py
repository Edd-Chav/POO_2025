from tkinter import *

def mostrarComentario():
    mostrarContenido=comentario.get("1.0",END).strip()
    resultado.config(text=f"Comentario: {mostrarContenido}")

ventana=Tk()
ventana.title("Text")
ventana.geometry("800x600")

lbl_1=Label(ventana,text="Escriba su comentario")
lbl_1.pack()

comentario=Text(ventana,width=40,height=5)
comentario.pack()

btn_1=Button(ventana,text="Mostrar comentario", command=mostrarComentario)
btn_1.pack()

resultado=Label(ventana,text="")
resultado.pack()
ventana.mainloop()
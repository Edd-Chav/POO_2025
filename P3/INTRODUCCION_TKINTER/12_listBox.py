from tkinter import *

ventana=Tk()
ventana.title("List box")
ventana.geometry("500x500")

def  mostrar():
    valor=lista.get(lista.curselection())
    resultado.config(text=f"Seleccionaste: {valor}")

lista=Listbox(ventana,width=50,height=5,selectmode="single")
lista.pack()

opciones=["Azul","Rojo","Negro","Amarillo"]

for i in opciones:
    lista.insert(END,i)
    

btn_mostrar=Button(ventana,text="Mostrar seleccion del usuario",command=mostrar)
btn_mostrar.pack()

resultado=Label(ventana,text="")
resultado.pack()


ventana.mainloop()
from tkinter import *

ventana=Tk()
ventana.title("Uso de label")
ventana.geometry("800x600")

#Etiqueta o label
etiqueta1=Label(ventana, text="Nombre de la Persona", font=("papyrus", 20)).pack()

marco1=Frame(ventana, bg="#DA8500", width=200, height=100).pack()
etiqueta2=Label(marco1, text="Soy una etiqeuta dentro de un marco", font=("papyrus", 15)).pack()



ventana.mainloop()
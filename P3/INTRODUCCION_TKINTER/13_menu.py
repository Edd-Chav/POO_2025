from tkinter import *

def mensaje(tipo):
    resultado.config(text=f"{tipo}")

ventana=Tk()
ventana.title("menu")
ventana.geometry("500x500")

menuBar=Menu(ventana)
ventana.config(menu=menuBar)

archivoMenu = Menu(menuBar , tearoff=1)
menuBar.add_cascade(label="Archivo" , menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo",command=lambda: mensaje("Nuevo Archivo") )
archivoMenu.add_command(label="Guardar Archivo",command=lambda:mensaje("Archivo guardado"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir",command=ventana.quit)

edicionMenu=Menu(menuBar,tearoff=1)
menuBar.add_cascade(label="Editar",menu=edicionMenu)
edicionMenu.add_command(label="Copiar",command=lambda: mensaje("Copiar"))
edicionMenu.add_command(label="Recortar",command=lambda: mensaje("Recortar"))
edicionMenu.add_separator()
edicionMenu.add_command(label="Salir",command=ventana.destroy)

resultado=Label(ventana,text="")
resultado.pack()

ventana.mainloop()
from tkinter import *

ventana=Tk()
ventana.title("Uso de Frame")
ventana.geometry("800x600")


#Marcos o Frame
marco=Frame(ventana,width=300,height=300,bg="Silver",border=2, relief=SOLID)
marco.pack_propagate(False)
marco.pack(pady=100)

marco2=Frame(ventana,width=200,height=100,bg="Red", border=2, relief=GROOVE).pack(padx=50,pady=50)

ventana.mainloop()

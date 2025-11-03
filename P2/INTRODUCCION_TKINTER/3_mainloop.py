from tkinter import *

ventana=Tk()
ventana.geometry("800x600")
ventana.title("Main-loop")


marco=Frame(ventana)
marco.config(width=600, height=400, bg="#C69605", border=100, relief= RAISED)
marco.pack(side=BOTTOM, anchor=CENTER)


ventana.mainloop()
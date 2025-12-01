from tkinter import *
from view import view1

class App:
    def _init_(self,ventana):
        vista=view1.View(ventana)
    
if __name__=="main_":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
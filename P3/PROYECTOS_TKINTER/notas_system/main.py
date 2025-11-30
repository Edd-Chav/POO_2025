"""
1.-  Implementar el MVC
2.-  Paradigma POO
3.-  App de escritorio con interfaz gráfica
"""
from tkinter import *
from view import view_1

class App:
    def __init__(self,ventana):
        vista=view_1.View(ventana)
    
if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
    

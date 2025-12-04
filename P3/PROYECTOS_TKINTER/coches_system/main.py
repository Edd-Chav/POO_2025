"""
1.- Implementar el MVC
2.- Paradigma POO
3.- App de escritorio con interfaz gráfica
"""
from tkinter import *
from view import view1

class App:
    def __init__(self,ventana):
        vista=view1.View(ventana)
    
if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
<<<<<<< HEAD
    8
=======
    

>>>>>>> 26b6cb7826b7ad429f2a5ba8d40e9ac1753205af

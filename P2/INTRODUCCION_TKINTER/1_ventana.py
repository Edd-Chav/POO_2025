"""
Tkinter trabaja a traves de interfaces, es una biblioteca de Python que permite crear aplicaciones en python para escritorio
"""
#from tkinter import *

# ventana=Tk()

import tkinter as tk

ventana=tk.Tk()

ventana.title("Mi primer aplicacioon grafica :)")
ventana.geometry("800x600")
ventana.resizable(True,True) #Metodo para redimencionar el tamaño de la ventana
ventana.mainloop() #Metodo que permite tener la ventana abierta e interactuar con ella



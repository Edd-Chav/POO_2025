"""
Tkinter trabaja a traves de interfaces, es una biblioteca de Python que permite crear aplicaciones en python para escritorio
"""
import tkinter as tk

ventana=tk.Tk()

ventana.title("Mi primer App Grafica en Tkinter con python")
ventana.geometry("800x600")
ventana.resizable(True,True) #metodo para redimensionar el tamaño de la ventana 
ventana.mainloop() # metodo que permite tenerla ventana abierta e interactuar con ella
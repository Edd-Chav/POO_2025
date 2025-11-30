from tkinter import *

def Entrar():
    label_titulo.config(
        text="Bienvenido",
        bg="pink",#color de fondo
        fg="purple",#color d eletra
        width=50,#ancho
        height=4,#altura
        font=("Arial",30,"bold"),#tipo de letra
        border=2,#borde
        relief=GROOVE #relieve
)
    
def Borrar():
    label_titulo.config(
        text="Acceso al sistema",
        bg="lightblue",#color de fondo
        fg="darkblue",#color d eletra
        width=50,#ancho
        height=4,#altura
        font=("Helvetica",30,"italic"),#tipo de letra
        border=2,#borde
        relief=GROOVE#relieve
    )

    #Reset los entry y eliminar el label
    txt_nombre.delete(0,END)
    txt_contraseña.delete(0,END)
    txt_nombre.focus()
    lbl_resultado.destroy()

def Salir():
    ventana.quit()

ventana=Tk() 
ventana.title("Entry")
ventana.geometry("500x500")

label_titulo=Label(ventana, text="Acceso al sistema")
label_titulo.config(
    bg="lightblue",#color de fondo
    fg="darkblue",#color d eletra
    width=50,#ancho
    height=4,#altura
    font=("Helvetica",30,"italic"),#tipo de letra
    border=2,#borde
    relief=GROOVE#relieve
)
label_titulo.pack()

marco_principal=Frame(ventana,width=800,height=300)
marco_principal.pack()

label_nombre=Label(marco_principal,text="Ingrese el nombre: ")
label_nombre.grid(row=0,column=0,padx=5,pady=5)

nombre=StringVar()
txt_nombre=Entry(marco_principal,textvariable=nombre)
txt_nombre.focus()
txt_nombre.grid(row=0,column=1,padx=5,pady=5)

label_contraseña=Label(marco_principal,text="Ingrese la contraseña: ")
label_contraseña.grid(row=1,column=0,padx=5,pady=5)

txt_contraseña=Entry(marco_principal,show="*")
txt_contraseña.grid(row=1,column=1,padx=5,pady=5)

marco_botones=Frame(ventana,width=800,height=100)
marco_botones.pack()

boton_entrar=Button(marco_botones,text="Entrar",command=Entrar)
boton_entrar.grid(row=0,column=0,padx=5,pady=5)

boton_borrarr=Button(marco_botones,text="Borrar",command=Borrar)
boton_borrarr.grid(row=0,column=1,padx=5,pady=5)

btn_salir=Button(marco_botones,text="Salir",command=Salir)
btn_salir.grid(row=0,column=2,padx=5,pady=5)

lbl_resultado=Label(ventana,text="")
lbl_resultado.pack(pady=5)

ventana.mainloop()
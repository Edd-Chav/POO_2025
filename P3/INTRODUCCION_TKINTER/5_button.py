from tkinter import *

"""def cambiarTexto():
    mensaje_cambiante.config(
        text="Se cambio el texto anterior"
    )

def regresarTexto():
    mensaje_cambiante.config(
        text="Texto Original"
    )"""

def iniciarSesion():
    ventana2=Toplevel()
    ventana2.title("Inicio de sesion")
    ventana2.geometry("800x600")

    label_saludo=Label(ventana2,text="Bienvenido ha iniciado sesion")
    label_saludo.pack(pady=10)

    ventana2.mainloop()

ventana=Tk()
ventana.title("Uso de Botones")
ventana.geometry("800x600")

frame_principal=Frame(ventana)
frame_principal.config(
    bg="silver",
    width=800,
    height=50,
    border=2,
    relief=GROOVE
)
frame_principal.pack(pady=10)

"""label_titulo=Label(frame_principal, text="Uso de Botones")
label_titulo.config(
    bg="silver",
    width=20
)

frame_principal.pack_propagate(False)

label_titulo.pack(pady=10)

mensaje_cambiante=Label(ventana,text="Texto Original")
mensaje_cambiante.pack()

boton_cambiar=Button(ventana,text="Cambiar Texto",command=cambiarTexto)#Command es la accion a realizar
boton_cambiar.pack()

boton_regresar=Button(ventana,text="Regresar texto",command=regresarTexto)
boton_regresar.pack()"""

#textos con nombre y contraseña y luego un boton de iniciar sesion, y cuando de click un mensjae que diga bienvenido inicio sesion en otra ventana

label_nombre=Label(ventana, text="Nombre: ")
label_nombre.config(
    bg="silver",
    width=20
)
label_nombre.pack(pady=10)

label_contraseña=Label(ventana, text="Contraseña: ")
label_contraseña.config(
    bg="silver",
    width=20
)
label_contraseña.pack(pady=10)


boton_inicio=Button(ventana,text="Iniciar sesion",command=iniciarSesion)
boton_inicio.pack()


ventana.mainloop()
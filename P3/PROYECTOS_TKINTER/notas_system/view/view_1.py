from tkinter import *
from tkinter import messagebox
from controller import controlador_1

class View:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.title("..: Notas System :..")
        ventana.geometry("800x600")
        ventana.resizable(False,False)
        self.menu_principal(ventana)
    
    @staticmethod    
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
    
    @staticmethod
    def menu_principal(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menú Principal ::..",justify="center")
        lbl_titulo.pack(pady=10)
        btn_registro=Button(ventana,text="1.- Registro",justify="center",command=lambda: View.registro(ventana))
        btn_registro.pack(pady=15)
        btn_login=Button(ventana,text="2.- Login",justify="center", command=lambda: View.login(ventana))
        btn_login.pack(pady=15)
        btn_salir=Button(ventana,text="3.- Salir",justify="center",command=ventana.quit)
        btn_salir.pack(pady=15)
    
    @staticmethod
    def registro(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Registro en el Sistema ::..",justify="center")
        lbl_titulo.pack(pady=10)
        
        lbl_nombre=Label(ventana,text="¿Cual es tu nombre?: ",justify="center")
        lbl_nombre.pack(pady=10)
        
        txt_nombre=Entry(ventana)
        txt_nombre.focus()
        txt_nombre.pack(pady=15)
        
        lbl_apellidos=Label(ventana,text="¿Cuales son tus apellidos?: ",justify="center")
        lbl_apellidos.pack(pady=10)
        
        txt_apellidos=Entry(ventana)
        txt_apellidos.pack(pady=15)
        
        lbl_email=Label(ventana,text="Ingresa tu email: ",justify="center")
        lbl_email.pack(pady=10)
        
        txt_email=Entry(ventana)
        txt_email.pack(pady=15)
        
        lbl_password=Label(ventana,text="Ingresa tu contraseña: ",justify="center")
        lbl_password.pack(pady=10)
        
        txt_password=Entry(ventana,show="*")
        txt_password.pack(pady=15)
        
        btn_registrar=Button(ventana,text="Registrar",command=lambda:
        { 
            controlador_1.Controller.registo(txt_nombre.get(),txt_apellidos.get(),txt_email.get(),txt_password.get()),
            View.login(ventana)
        }
            )
        btn_registrar.pack(pady=15)
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=15)
    
    @staticmethod    
    def login(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Inicio de Sesión ::..",justify="center")
        lbl_titulo.pack(pady=10)
        
        lbl_email=Label(ventana,text="Ingresa tu email: ",justify="center")
        lbl_email.pack(pady=15)
        
        txt_email=Entry(ventana)
        txt_email.pack(pady=15)
        txt_email.focus()
        lbl_password=Label(ventana,text="Ingresa tu contraseña: ",justify="center")
        lbl_password.pack(pady=10)
        
        txt_password=Entry(ventana,show="*")
        txt_password.pack(pady=15)
        
        btn_entrar=Button(ventana,text="Entrar",justify="center",command= lambda: controlador_1.Controller.inicio_sesion(ventana,txt_email.get(),txt_password.get()))
        btn_entrar.pack(pady=15)
        
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=10)
    
    @staticmethod    
    def menu_notas(ventana,usuario_id,nombre,apellidos):
        global id_user, nom_usuario,ap_usuario
        id_user=usuario_id
        nom_usuario=nombre
        ap_usuario=apellidos 
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f"..:: Bienvenido {nombre} {apellidos}, has iniciado sesión::..",justify="center")
        lbl_titulo.pack(pady=10)
        btn_crear=Button(ventana,text="1.- Crear",justify="center",command=lambda: View.crear_notas(ventana))
        btn_crear.pack(pady=15)
        btn_mostrar=Button(ventana,text="2. Mostrar",justify="center", command=lambda: View.mostrar_notas(ventana))
        btn_mostrar.pack(pady=15)
        btn_cambiar=Button(ventana,text="3. Cambiar",justify="center", command=lambda:View.cambiar_notas(ventana))
        btn_cambiar.pack(pady=15)
        btn_eliminar=Button(ventana,text="4. Eliminar",justify="center", command=lambda: View.eliminar_notas(ventana))
        btn_eliminar.pack(pady=15)
        
        btn_volver=Button(ventana,text="5.- Regresar",command=lambda: View.login(ventana))
        btn_volver.pack(pady=15)
   
    @staticmethod
    def crear_notas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Crear Nota ::..",justify="center")
        lbl_titulo.pack(pady=10)
        
        lbl_titulo_nota=Label(ventana,text="Titulo : ",justify="center")
        lbl_titulo_nota.pack(pady=10)
        
        txt_nota=Entry(ventana)
        txt_nota.pack(pady=10)
        txt_nota.focus()
        
        lbl_descripcion=Label(ventana,text="Descripción ",justify="center")
        lbl_descripcion.pack(pady=10)
        
        txt_descripcion=Entry(ventana)
        txt_descripcion.pack(pady=10)
        
        btn_guardar=Button(ventana,text="Guardar",justify="center",command= lambda: controlador_1.Controller.crear_nota(id_user,txt_nota.get(),txt_descripcion.get()))
        btn_guardar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_notas(ventana,id_user,nom_usuario,ap_usuario))
        btn_volver.pack(pady=10)
    
    @staticmethod    
    def mostrar_notas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f"{nom_usuario} {ap_usuario}, tus notas son:  ",justify="center")
        lbl_titulo.pack(pady=10)
        
        filas=""
        registros=controlador_1.Controller.mostrar_notas(id_user)
        num_nota=1
        if len(registros)>0:
            for fila in registros:
                filas=filas+f"Nota: {num_nota} \nID: {fila[0]}.- Titulo: {fila[2]}. Fecha de creacion: {fila[4]} \n Descripción: {fila[3]}"
                num_nota+=1
        else:
            messagebox.showinfo(icon="warning",message="No existen notas para este usuario")
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_notas(ventana,id_user,nom_usuario,ap_usuario) )
        btn_volver.pack(pady=10)
    
    @staticmethod    
    def cambiar_notas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f".::{nom_usuario} {ap_usuario}, vamos a modificar una nota ::.",justify="center")
        lbl_titulo.pack(pady=10)
        
        lbl_id=Label(ventana, text="ID de la Nota a Cambiar: ",justify="center")
        lbl_id.pack(pady=10)
        
        txt_id=Entry(ventana)
        txt_id.pack(pady=10)
        txt_id.focus()
        
        lbl_nuevo_titulo=Label(ventana,text="Nuevo Titulo: ",justify="center")
        lbl_nuevo_titulo.pack(pady=10)
        
        txt_nuevo_titulo=Entry(ventana)
        txt_nuevo_titulo.pack(pady=10)
        
        lbl_descripcion=Label(ventana,text="Nueva descripción: ",justify="center")
        lbl_descripcion.pack(pady=10)
        
        txt_descripcion=Entry(ventana)
        txt_descripcion.pack(pady=10)
        
        btn_guardar=Button(ventana,text="Guardar", command= lambda: controlador_1.Controller.cambiar_notas(txt_id.get(),txt_nuevo_titulo.get(),txt_descripcion.get()))
        btn_guardar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_notas(ventana,id_user,nom_usuario,ap_usuario))
        btn_volver.pack(pady=10)
   
    @staticmethod    
    def eliminar_notas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f".::{nom_usuario} {ap_usuario}, vamos a eliminar una nota ::.",justify="center")
        lbl_titulo.pack(pady=10)
        
        lbl_id=Label(ventana, text="ID de la Nota a eliminar: ",justify="center")
        lbl_id.pack(pady=10)
        
        txt_id=Entry(ventana)
        txt_id.pack(pady=10)
        txt_id.focus()
        
        btn_eliminar=Button(ventana,text="Eliminar", command= lambda: controlador_1.Controller.eliminar_nota(txt_id.get()))
        btn_eliminar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_notas(ventana,id_user,nom_usuario,ap_usuario) )
        btn_volver.pack(pady=10)
        
        
   
        
from tkinter import messagebox
from model import usuario, nota
from view import view_1

class Controller:
    @staticmethod
    def registo(nombre,apellidos,email,password):
        resultado=usuario.Usuario.registrar(nombre, apellidos,email,password)
        if resultado:
            messagebox.showinfo(icon="info",message=f"{nombre} {apellidos}, se registro correctamente con el email {email}",title="Usuarios")
        else:
            messagebox.showinfo(icon="warning",message=f" Por favor intentelo de nuevo, no fue posible insertar el registro", title="Usuarios")
            
    @staticmethod
    def inicio_sesion(ventana,email,password):
        registro=usuario.Usuario.iniciar_sesion(email,password)
        if registro:
            messagebox.showinfo(icon="info",message=f"{registro[1]} {registro[2]}, Iniciaste sesión correctamente",title="Usuarios")
            view_1.View.menu_notas(ventana, registro[0],registro[1],registro[2])
        else:
            messagebox.showwarning(icon="warning",message="Email y/o contraseña incorrectas... vuelva a intentarlo ...")
        
    @staticmethod
    def crear_nota(usuario_id,titulo,descripcion):
        resultado=nota.Nota.crear(usuario_id,titulo,descripcion)
        Controller.respuesta_sql(resultado)
            
    @staticmethod
    def mostrar_notas(usuario_id):
        registro=nota.Nota.mostrar(usuario_id)
        return registro
    
    @staticmethod
    def eliminar_nota(id):
        resultado=nota.Nota.eliminar(id)
        Controller.respuesta_sql(resultado)
    
    @staticmethod
    def cambiar_notas(id,titulo,descripcion):
        resultado=nota.Nota.actualizar(id,titulo,descripcion)
        Controller.respuesta_sql(resultado)    
    
    @staticmethod
    def respuesta_sql(resultado):
        if resultado:
            messagebox.showinfo(message=f" Acción Realizada con Éxito ",icon="info")
        else:
            messagebox.showinfo(message="\n\t...No fue posible realizar la acción correctamente, vuelva a intentar...",icon="info")
     
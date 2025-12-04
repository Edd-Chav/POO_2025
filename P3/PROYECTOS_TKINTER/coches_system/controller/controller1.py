
from model import cochesBD
from view import view1
from tkinter import messagebox


"""


"""

class Controller:
    @staticmethod
    def registro_auto(marca,color,modelo,velocidad,caballaje,plazas):
        resultado = cochesBD.Autos.insertar(marca, color, modelo, velocidad, caballaje, plazas)
        Controller.respuesta_sql(resultado)
        
    @staticmethod
    def consultar_autos():
        autos = cochesBD.Autos.consultar()
        return autos

    @staticmethod
    def cambiar_auto(marca, color, modelo, velocidad, caballaje, plazas,id):
        resultado = cochesBD.Autos.actualizar(marca, color, modelo, velocidad, caballaje, plazas,id)
        Controller.respuesta_sql(resultado)

    @staticmethod
    def borrar_auto(id):
        resultado = cochesBD.Autos.eliminar(id)
        Controller.respuesta_sql(resultado)

    @staticmethod
    def insertar_camionetas(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        resultado = cochesBD.Camionetas.insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
        Controller.respuesta_sql(resultado)

    @staticmethod
    def consultar_camionetas():
        camionetas = cochesBD.Camionetas.consultar()
        return camionetas

    @staticmethod
    def cambiar_camionetas(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id):
        resultado = cochesBD.Camionetas.actualizar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id)
        Controller.respuesta_sql(resultado)

    @staticmethod
    def borrar_camionetas(id):
        resultado = cochesBD.Camionetas.eliminar(id)
        Controller.respuesta_sql(resultado)

    @staticmethod
    def respuesta_sql(resultado):
        if resultado:
            messagebox.showinfo(message=f" Acción Realizada con Éxito ",icon="info")
        else:
            messagebox.showinfo(message="\n\t...No fue posible realizar la acción correctamente, vuelva a intentar...",icon="info")


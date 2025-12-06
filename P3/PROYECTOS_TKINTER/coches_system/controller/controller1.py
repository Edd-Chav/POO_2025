from model import cochesBD
from view import view1
from tkinter import messagebox

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
    def respuesta_sql(resultado):
        if resultado:
            messagebox.showinfo(message=f" Acción Realizada con Éxito ",icon="info")
        else:
            messagebox.showinfo(message="\n\t...No fue posible realizar la acción correctamente, vuelva a intentar...",icon="info")

    @staticmethod
    def registro_camioneta(marca,color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        resultado = cochesBD.Camionetas.insertar(marca,color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
        Controller.respuesta_sql(resultado)
        
    @staticmethod
    def consultar_camionetas():
        camioneta = cochesBD.Camionetas.consultar()
        return camioneta

    @staticmethod
    def cambiar_camioneta(marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada, id):
        resultado = cochesBD.Camionetas.actualizar(marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada, id)
        Controller.respuesta_sql(resultado)

    @staticmethod
    def borrar_camioneta(id):
        resultado = cochesBD.Camionetas.eliminar(id)
        Controller.respuesta_sql(resultado)


    @staticmethod
    def registro_camion(marca,color, modelo, velocidad, caballaje, plazas, eje,capacidadCarga):
        resultado = cochesBD.Camiones.insertar(marca,color, modelo, velocidad, caballaje, plazas, eje,capacidadCarga)
        Controller.respuesta_sql(resultado)
        
    @staticmethod
    def consultar_camiones():
        camiones = cochesBD.Camiones.consultar()
        return camiones

    @staticmethod
    def cambiar_camion(marca, color, modelo, velocidad, caballaje, plazas,eje,capacidadCarga, id):
        resultado = cochesBD.Camiones.actualizar(marca, color, modelo, velocidad, caballaje, plazas,eje,capacidadCarga, id)
        Controller.respuesta_sql(resultado)

    @staticmethod
    def borrar_camion(id):
        resultado = cochesBD.Camiones.eliminar(id)
        Controller.respuesta_sql(resultado)

        #ola

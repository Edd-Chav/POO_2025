from tkinter import messagebox
from model import operaciones

class Funciones:
    @staticmethod
    def operaciones(n1,n2,signo):
        if signo=="+":
            ope=n1+n2
            tipo="Suma"
        elif signo=="-":
            ope=n1-n2
            tipo="Resta"
        elif signo=="x":
            ope=n1*n2
            tipo="Multiplicacion"
        elif signo=="/":
            ope=n1/n2
            tipo="Division"
        resultado=messagebox.askquestion(message=f"{n1}{signo}{n2} = {ope}\n\n¿Deseas guardar en la base de datos?",icon="question")
        if resultado=="yes":
            operaciones.Operaciones.insertar(n1,n2,signo,ope)
        
    @staticmethod
    def insertar(numero1,numero2,signo):
        resultado=Funciones.operaciones(numero1,numero2,signo)
        respuesta= operaciones.Operaciones.insertar(numero1,numero2,signo, resultado)
        Funciones.respuesta_sql(respuesta)
    
    @staticmethod
    def consultar():
        registros=operaciones.Operaciones.consultar()
        return registros
    
    @staticmethod
    def actualizar(numero1,numero2,signo,resultado,id):
        respuesta=operaciones.Operaciones.actualizar(numero1,numero2,signo,resultado,id)
        Funciones.respuesta_sql(respuesta)
    
    @staticmethod
    def eliminar(id):
        respuesta=operaciones.Operaciones.eliminar(id)
        Funciones.respuesta_sql(respuesta)
    
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(message=f" Acción Realizada con Éxito ",icon="info")
        else:
            messagebox.showinfo(message="\n\t...No fue posible realizar la acción correctamente, vuelva a intentar...",icon="info")
    
    @staticmethod
    def buscar(id):
        operacion=operaciones.Operaciones.buscar(id)
        if operacion:
            return operacion
        else:
            messagebox.showinfo(message="No se encontró el id")
            
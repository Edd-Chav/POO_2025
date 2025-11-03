from cochesBD import *

class Autos:
    def _init_(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas

    def insertar(self):
        try:
            cursor.execute(
                "insert into coches values(null,%s,%s,%s,%s,%s,%s)",
                (self._marca,self._color,self._modelo,self._velocidad,self._caballaje,self._plazas)
            )
            conexion.commit()
            return True
        except:
            return False
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from coches")
            return cursor.fetchall()
        except:
            return []
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas):
        try:
            cursor.execute("" \
            "update coches set marca=%s, color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s where id=%s"),
            (marca,color,modelo,velocidad,caballaje,plazas)
            conexion.commit()
            return True
        except:
            return False

class Camionetas:
    
    @staticmethod
    def insertar(self,marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        try:
           cursor.execute(
               "insert into camionetas values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
               (marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
           )
           conexion.commit()
           return True
        except:
            return False    
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from camionetas")
            return cursor.fetchall()
        except:
            return []
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas):
        try:
            cursor.execute("" \
            "update camionetas set marca=%s, color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s where id=%s"),
            (marca,color,modelo,velocidad,caballaje,plazas)
            conexion.commit()
            return True
        except:
            return False

class Camiones:
    
    @staticmethod
    def insertar(self,marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
        try:
           cursor.execute(
               "insert into camiones values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
           )
           conexion.commit()
           return True
        except:
            return False   
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from camiones")
            return cursor.fetchall()
        except:
            return []
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas):
        try:
            cursor.execute("" \
            "update camiones set marca=%s, color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s where id=%s"),
            (marca,color,modelo,velocidad,caballaje,plazas)
            conexion.commit()
            return True
        except:
            return False
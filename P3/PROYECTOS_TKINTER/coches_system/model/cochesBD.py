from conexion_bd import conexion, cursor
import mysql.connector


class Autos:

    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas
    
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas):
        if cursor is None or conexion is None:
            print("No hay conexión a la base de datos (insertar autos)")
            return False
        try:
            cursor.execute(
                "insert into autos values (null, %s,%s,%s,%s,%s,%s)",
                (marca, color, modelo, velocidad, caballaje, plazas)
            )
            conexion.commit()
            return True
        except mysql.connector.Error as e:
            print("Error insertar autos:", e)
            return False

    @staticmethod    
    def consultar():
        if cursor is None:
            print("No hay conexión a la base de datos (consultar autos)")
            return []
        try:
            cursor.execute("select * from autos")
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print("Error consultar autos:", e)
            return []
        
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, id):
        if cursor is None or conexion is None:
            print("No hay conexión a la base de datos (actualizar autos)")
            return False
        try:
            sql = "UPDATE autos SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s WHERE Id_coche=%s"
            
            datos = (marca, color, modelo, velocidad, caballaje, plazas, id)
            
            cursor.execute(sql, datos)
            conexion.commit()
            
            return True
            
        except mysql.connector.Error as error:
            print(f"Error al actualizar: {error}")
            return False
        
    @staticmethod
    def eliminar(id):
        if cursor is None or conexion is None:
            print("No hay conexión a la base de datos (eliminar autos)")
            return False
        try:
            # Usamos Id_coche
            sql = "DELETE FROM autos WHERE Id_coche=%s"
            
            cursor.execute(sql, (id,))
            conexion.commit()
            
            return True
            
        except mysql.connector.Error as error:
            print(f"Error al eliminar: {error}")
            return False

class Camionetas:
    @staticmethod
    def insertar(marca,color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        if cursor is None or conexion is None:
            print("No hay conexión a la base de datos (insertar camionetas)")
            return False
        try:
            cursor.execute(
                "insert into camionetas values(null, %s,%s,%s,%s,%s,%s,%s,%s)", 
                (marca,color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
            )
            conexion.commit()
            return True
        except mysql.connector.Error as e:
            print("Error insertar camionetas:", e)
            return False
        
    @staticmethod    
    def consultar():
        if cursor is None:
            print("No hay conexión a la base de datos (consultar camionetas)")
            return []
        try:
            cursor.execute("select * from camionetas")
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print("Error consultar camionetas:", e)
            return []
    
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas,traccion, cerrada, id):
        if cursor is None or conexion is None:
            print("No hay conexión a la base de datos (actualizar camionetas)")
            return False
        try:
            cursor.execute(
                "update camionetas set marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s,traccion=%s, cerrada=%s where id_camionetas=%s",
                (marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada, id)
            )
            conexion.commit()
            return True
        except mysql.connector.Error as e:
            print("Error actualizar camionetas:", e)
            return False
    
    @staticmethod
    def eliminar(id):
        if cursor is None or conexion is None:
            print("No hay conexión a la base de datos (eliminar camionetas)")
            return False
        try:
            cursor.execute(
                "delete from camionetas where id_camionetas=%s",(id,)
            )
            conexion.commit()
            return True
        except mysql.connector.Error as e:
            print("Error eliminar camionetas:", e)
            return False

class Camiones:
    @staticmethod
    def insertar(marca,color, modelo, velocidad, caballaje, plazas, eje,capacidadCarga):
        if cursor is None or conexion is None:
            print("No hay conexión a la base de datos (insertar camiones)")
            return False
        try:
            cursor.execute(
                "insert into camiones values(null, %s,%s,%s,%s,%s,%s,%s,%s)", 
                (marca,color, modelo, velocidad, caballaje, plazas,eje, capacidadCarga)
            )
            conexion.commit()
            return True
        except mysql.connector.Error as e:
            print("Error insertar camiones:", e)
            return False
    
    @staticmethod    
    def consultar():
        if cursor is None:
            print("No hay conexión a la base de datos (consultar camiones)")
            return []     
        try:
            cursor.execute("select * from camiones")
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print("Error consultar camiones:", e)
            return []
        
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas,eje,capacidadCarga, id):
        if cursor is None or conexion is None:
            print("No hay conexión a la base de datos (actualizar camiones)")
            return False
        try:
            cursor.execute(
                "update camiones set marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s,eje=%s, capacidadCarga=%s where id_camion=%s",
                (marca, color, modelo, velocidad, caballaje, plazas,eje,capacidadCarga, id)
            )
            conexion.commit()
            return True
        except mysql.connector.Error as e:
            print("Error actualizar camiones:", e)
            return False
    
    @staticmethod
    def eliminar(id):
        if cursor is None or conexion is None:
            print("No hay conexión a la base de datos (eliminar camiones)")
            return False
        try:
            cursor.execute(
                "delete from camiones where id_camion=%s",(id,)
            )
            conexion.commit()
            return True
        except mysql.connector.Error as e:
            print("Error eliminar camiones:", e)
            return False
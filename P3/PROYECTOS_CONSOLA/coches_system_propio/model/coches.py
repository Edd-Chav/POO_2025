import conexionBD


class Autos:
    # Fallback en memoria si no hay BD
    _data = []
    _next_id = 1
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas):
        # Si hay conexión a BD, usarla
        if conexionBD.cursor is not None:
            try:
                sql = "INSERT INTO coches VALUES(null,%s,%s,%s,%s,%s,%s)"
                conexionBD.cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas))
                conexionBD.conexion.commit()
                return True
            except Exception as e:
                print(f"Error BD: {e}")
                return False
        # Fallback en memoria
        try:
            _id = Autos._next_id
            Autos._next_id += 1
            Autos._data.append((_id, marca, color, modelo, velocidad, caballaje, plazas))
            return True
        except Exception as e:
            print(f"Error memoria: {e}")
            return False

    @staticmethod
    def consultar():
        if conexionBD.cursor is not None:
            try:
                conexionBD.cursor.execute("SELECT * FROM coches")
                return conexionBD.cursor.fetchall()
            except:
                return []
        # Fallback en memoria
        return list(Autos._data)

    @staticmethod
    def actualizar(id_coche, marca, color, modelo, velocidad, caballaje, plazas):
        if conexionBD.cursor is not None:
            try:
                sql = "UPDATE coches SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s WHERE id_coche=%s"
                conexionBD.cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas, id_coche))
                conexionBD.conexion.commit()
                return True
            except Exception as e:
                print(f"Error BD actualizar: {e}")
                return False
        # Fallback memoria
        try:
            id_c = int(id_coche)
            for i, item in enumerate(Autos._data):
                if int(item[0]) == id_c:
                    Autos._data[i] = (id_c, marca, color, modelo, velocidad, caballaje, plazas)
                    return True
            return False
        except:
            return False

    @staticmethod
    def eliminar(id_coche):
        if conexionBD.cursor is not None:
            try:
                conexionBD.cursor.execute("DELETE FROM coches WHERE id_coche=%s", (id_coche,))
                conexionBD.conexion.commit()
                return True
            except Exception as e:
                print(f"Error BD eliminar: {e}")
                return False
        # Fallback memoria
        try:
            id_c = int(id_coche)
            for i, item in enumerate(Autos._data):
                if int(item[0]) == id_c:
                    del Autos._data[i]
                    return True
            return False
        except:
            return False

class Camionetas:
    _data = []
    _next_id = 1

    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        if conexionBD.cursor is not None:
            try:
                sql = "INSERT INTO camionetas VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s)"
                conexionBD.cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada))
                conexionBD.conexion.commit()
                return True
            except Exception as e:
                print(e)
                return False
        try:
            _id = Camionetas._next_id
            Camionetas._next_id += 1
            Camionetas._data.append((_id, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada))
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def consultar():
        if conexionBD.cursor is not None:
            try:
                conexionBD.cursor.execute("SELECT * FROM camionetas")
                return conexionBD.cursor.fetchall()
            except:
                return []
        return list(Camionetas._data)
    @staticmethod
    def actualizar(id_camioneta, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        if conexionBD.cursor is not None:
            try:
                sql = "update camionetas set marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, traccion=%s, cerrada=%s where id_camioneta=%s"
                conexionBD.cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id_camioneta))
                conexionBD.conexion.commit()
                return True
            except Exception as e:
                print(e)
                return False
        try:
            id_c = int(id_camioneta)
            for i, item in enumerate(Camionetas._data):
                if int(item[0]) == id_c:
                    Camionetas._data[i] = (id_c, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
                    return True
            return False
        except:
            return False

    @staticmethod
    def eliminar(id_camioneta):
        if conexionBD.cursor is not None:
            try:
                conexionBD.cursor.execute("DELETE FROM camionetas WHERE id_camioneta=%s", (id_camioneta,))
                conexionBD.conexion.commit()
                return True
            except Exception as e:
                print(e)
                return False
        try:
            id_c = int(id_camioneta)
            for i, item in enumerate(Camionetas._data):
                if int(item[0]) == id_c:
                    del Camionetas._data[i]
                    return True
            return False
        except:
            return False
    
    # ... Puedes completar actualizar y eliminar siguiendo el ejemplo de Autos ...

class Camiones:
    _data = []
    _next_id = 1

    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, carga):
        if conexionBD.cursor is not None:
            try:
                sql = "INSERT INTO camiones VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s)"
                conexionBD.cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas, eje, carga))
                conexionBD.conexion.commit()
                return True
            except:
                return False
        try:
            _id = Camiones._next_id
            Camiones._next_id += 1
            Camiones._data.append((_id, marca, color, modelo, velocidad, caballaje, plazas, eje, carga))
            return True
        except:
            return False
            
    @staticmethod
    def consultar():
        if conexionBD.cursor is not None:
            try:
                conexionBD.cursor.execute("SELECT * FROM camiones")
                return conexionBD.cursor.fetchall()
            except:
                return []
        return list(Camiones._data)
        
    @staticmethod
    def actualizar(id_camion, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        if conexionBD.cursor is not None:
            try:
                sql = "update camiones set marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, eje=%s, capacidadCarga=%s where id_camion=%s"
                conexionBD.cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga, id_camion))
                conexionBD.conexion.commit()
                return True
            except Exception as e:
                print(e)
                return False
        try:
            id_c = int(id_camion)
            for i, item in enumerate(Camiones._data):
                if int(item[0]) == id_c:
                    Camiones._data[i] = (id_c, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga)
                    return True
            return False
        except:
            return False

    @staticmethod
    def eliminar(id_camion):
        if conexionBD.cursor is not None:
            try:
                conexionBD.cursor.execute("DELETE FROM camiones WHERE id_camion=%s", (id_camion,))
                conexionBD.conexion.commit()
                return True
            except Exception as e:
                print(e)
                return False
        try:
            id_c = int(id_camion)
            for i, item in enumerate(Camiones._data):
                if int(item[0]) == id_c:
                    del Camiones._data[i]
                    return True
            return False
        except:
            return False
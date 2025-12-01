import mysql.connector

# Valores por defecto para evitar ImportError si la conexión falla
conexion = None
cursor = None
connected = False

try:
    conexion = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_concesionario'
    )
    cursor = conexion.cursor(buffered=True)
    connected = True
except Exception as e:
    # No detener la aplicación: dejar cursor/conexion en None
    print("Ocurrio un error con la BD verifique ...")
    print(e)
    conexion = None
    cursor = None
    connected = False
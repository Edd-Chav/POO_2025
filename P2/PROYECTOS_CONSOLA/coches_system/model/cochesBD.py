import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_coches2'
    )
    cursor = conexion.cursor(buffered=True)
except mysql.connector.Error as err:
    print(f"Error al conectar con la base de datos: {err}")
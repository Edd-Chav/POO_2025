import mysql.connector

# Export these names so other modules can import them even if connection fails
conexion = None
cursor = None

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="bd_coches",
    )
    cursor = conexion.cursor(buffered=True)
except mysql.connector.Error as e:
    print("Ocurrió un error con la base de datos:", e)
except Exception as e:
    print("Error inesperado al conectar a la base de datos:", e)


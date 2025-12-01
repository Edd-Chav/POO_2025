import mysql.connector

try:
    conexion=mysql.connector.connect(
    port="3306",    
    host="127.0.0.1",
    user="root",
    password="",
    database="bd_coches"
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("Ocurrio un error con la base de datos... Verifique")


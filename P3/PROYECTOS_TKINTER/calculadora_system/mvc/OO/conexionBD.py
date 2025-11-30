import mysql.connector

try:
    conexion=mysql.connector.connect(
        port=3306,
        host="127.0.0.1",
        user="root",
        password="admin",
        database="bd_calculadora_basica"
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("Ocurrio un error con la BD ... Verifique")
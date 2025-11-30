import mysql.connector
from tkinter import messagebox
try:
    #Conectar con la BD en MySQL
    conexion=mysql.connector.connect(
        port=3306,
        host='localhost',
        user='root',
        password='admin',
        database='bd_notas'
    )
    #Crear un objeto de tipo cursor que se pueda reutilizar nuevamente
    cursor=conexion.cursor(buffered=True)
except:
     messagebox.showinfo(message=f"Ocurrio un error con el Sistema por favor verifique ...")    

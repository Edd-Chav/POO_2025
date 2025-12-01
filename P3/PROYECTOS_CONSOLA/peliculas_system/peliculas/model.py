import mysql.connector
from mysql.connector import Error
from tkinter import messagebox


class Database:
    def __init__(self, host, user, password, database):
        try:
            self.conn = mysql.connector.connect(
                port=3306,
                host="localhost",
                user="root",
                password="admin",
                database="db_peliculas"
            )
            self.cursor = self.conn.cursor()
            print("Conexión a BD exitosa.")
        except Error as e:
            messagebox.showerror("Error", f"No se pudo conectar a la BD: {e}")

    def fetch(self):
        self.cursor.execute("SELECT * FROM peliculas")
        return self.cursor.fetchall()

    def insert(self, titulo, director, anio):
        self.cursor.execute("INSERT INTO peliculas (titulo, director, anio) VALUES (%s, %s, %s)",
                            (titulo, director, anio))
        self.conn.commit()

    def update(self, id_peli, titulo, director, anio):
        self.cursor.execute("UPDATE peliculas SET titulo=%s, director=%s, anio=%s WHERE id=%s",
                            (titulo, director, anio, id_peli))
        self.conn.commit()

    def delete(self, id_peli):
        self.cursor.execute("DELETE FROM peliculas WHERE id=%s", (id_peli,))
        self.conn.commit()
"""Establece conexión con MySQL si está disponible.
Si falla, expone `conexion=None`, `cursor=None` y `DB_AVAILABLE=False`.
El resto del código detecta la ausencia de BD y usa un fallback en memoria.
"""
DB_AVAILABLE = False
conexion = None
cursor = None
try:
    import mysql.connector
    conexion = mysql.connector.connect(
        port=3306,
        host="127.0.0.1",
        user="root",
        password="admin",
        database="bd_calculadora_basica"
    )
    cursor = conexion.cursor(buffered=True)
    DB_AVAILABLE = True
except Exception:
    # No connection available — la aplicación seguirá funcionando
    DB_AVAILABLE = False
    conexion = None
    cursor = None
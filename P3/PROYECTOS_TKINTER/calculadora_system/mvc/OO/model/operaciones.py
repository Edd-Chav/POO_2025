from conexionBD import DB_AVAILABLE, conexion, cursor
from datetime import datetime

class Operaciones:
  """Encapsula operaciones sobre la BD.
  Si `DB_AVAILABLE` es False, usa una lista en memoria como fallback.
  """
  # fallback en memoria
  _mem = []  # elementos: (id, fecha, numero1, numero2, signo, resultado)
  _next_id = 1

  @staticmethod
  def insertar(numero1, numero2, signo, resultado):
    if DB_AVAILABLE and cursor is not None:
      try:
        cursor.execute(
          "insert into operaciones values(null,NOW(),%s,%s,%s,%s)",
          (numero1, numero2, signo, resultado)
        )
        conexion.commit()
        return True
      except Exception:
        return False
    else:
      fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      id_ = Operaciones._next_id
      Operaciones._next_id += 1
      Operaciones._mem.append((id_, fecha, numero1, numero2, signo, resultado))
      return True

  @staticmethod
  def consultar():
    if DB_AVAILABLE and cursor is not None:
      try:
        cursor.execute("select * from operaciones")
        return cursor.fetchall()
      except Exception:
        return []
    else:
      return list(Operaciones._mem)

  @staticmethod
  def actualizar(numero1, numero2, signo, resultado, id):
    if DB_AVAILABLE and cursor is not None:
      try:
        cursor.execute(
          "update operaciones set fecha= NOW(), numero1=%s, numero2=%s, signo=%s, resultado=%s where id=%s",
          (numero1, numero2, signo, resultado, id)
        )
        conexion.commit()
        return True
      except Exception:
        return False
    else:
      for idx, rec in enumerate(Operaciones._mem):
        if rec[0] == id:
          fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          Operaciones._mem[idx] = (id, fecha, numero1, numero2, signo, resultado)
          return True
      return False

  @staticmethod
  def eliminar(id):
    if DB_AVAILABLE and cursor is not None:
      try:
        cursor.execute(
          "delete from operaciones where id=%s",
          (id,)
        )
        conexion.commit()
        return True
      except Exception:
        return False
    else:
      for idx, rec in enumerate(Operaciones._mem):
        if rec[0] == id:
          Operaciones._mem.pop(idx)
          return True
      return False

  @staticmethod
  def consultar_id(id):
    if DB_AVAILABLE and cursor is not None:
      try:
        cursor.execute(
          "select * from operaciones where id=%s",
          (id,)
        )
        # no commit necesario para select
        return cursor.fetchone()
      except Exception:
        return None
    else:
      for rec in Operaciones._mem:
        if rec[0] == id:
          return rec
      return None
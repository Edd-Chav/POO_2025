from conexionBD import conexion, cursor
import hashlib
import datetime


class BaseRepository:
    """Base repository providing CRUD-like interface. Concrete repos implement methods."""
    def create(self, *args, **kwargs):
        raise NotImplementedError

    def list(self, *args, **kwargs):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError


class UserRepository(BaseRepository):
    def _hash(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def create(self, nombre, apellidos, email, password):
        try:
            hashed = self._hash(password)
            fecha = datetime.datetime.now()
            cursor.execute(
                "insert into usuarios values(null,%s,%s,%s,%s,%s)",
                (nombre, apellidos, email, hashed, fecha)
            )
            conexion.commit()
            return True
        except Exception:
            return False

    def authenticate(self, email, password):
        try:
            hashed = self._hash(password)
            cursor.execute(
                "select * from usuarios where email=%s and password=%s",
                (email, hashed)
            )
            usuario = cursor.fetchone()
            return usuario
        except Exception:
            return None


class NoteRepository(BaseRepository):
    def create(self, usuario_id, titulo, descripcion):
        try:
            cursor.execute(
                "insert into notas values(null,%s,%s,%s,NOW())",
                (usuario_id, titulo, descripcion)
            )
            conexion.commit()
            return True
        except Exception:
            return False

    def list(self, usuario_id):
        try:
            cursor.execute(
                "select * from notas where usuario_id=%s",
                (usuario_id,)
            )
            return cursor.fetchall()
        except Exception:
            return []

    def update(self, id, titulo, descripcion):
        try:
            cursor.execute(
                "update notas set titulo=%s,descripcion=%s where id=%s",
                (titulo, descripcion, id)
            )
            conexion.commit()
            return True
        except Exception:
            return False

    def delete(self, id):
        try:
            cursor.execute(
                "delete from notas where id=%s",
                (id,)
            )
            conexion.commit()
            return True
        except Exception:
            return False

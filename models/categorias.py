from config import conexion
from sqlalchemy import Column,types

class Categorias(conexion.model):
    __tablename__ = 'categorias'
    id=Column(type_=types.Integer, primary_key=True,autoincrement=True)
    nombre=Column(type_=types.String (length=45))

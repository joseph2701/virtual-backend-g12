from config import conexion
from sqlalchemy import Column,types

class Usuario(conexion.model):
    __tablename__ = 'usuarios'
    id=Column(type_=types.Integer, primary_key=True,autoincrement=True)
    nombre=Column(type_=types.String (length=45))
    apelido=Column(type_=types.String (length=45))
    correo=Column(type_=types.String (length=45),nullable=False,unique=True)
    password=Column(type_=types.Text(),nullable=False)



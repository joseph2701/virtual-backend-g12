from datetime import datetime
from config import conexion
from sqlalchemy import Column,types,orm
from sqlalchemy.sql.schema import ForeignKey

class Movimiento(conexion.model):
    __tablename__ = 'movimientos'

    id=Column(type_=types.Integer, primary_key=True,autoincrement=True)
    monto=Column(type_=types.Float,nullable=False)
    tipo=Column(type_=types.Enum ('INGRESO','EGRESO'),nullable=False)
    descripcion=Column(type_=types.String (length=45))
    moneda=Column(type_=types.Enum ('SOLES','DOLARES','EUROS'),nullable=False)
    fecha_creacion=Column(type_=types.datetime(),default=datetime.now())
    id_usuario= Column(ForeignKey(column='usuarios.id'),type_=types.Integer,nullable=False)
    id_categoria= Column(ForeignKey(column='categorias.id'),type_=types.Integer,nullable=False)

    usuario=orm.relationship('Usuario',backref='usuario_movimientos')
    categoria=orm.relationship('Categoria',backref='categoria_movimientos')

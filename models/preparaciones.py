from config import conexion
from sqlalchemy import Column,types,orm
from sqlalchemy.sql.schema import ForeignKey

class Preparacion(conexion.Model):
    
    id = Column(type_=types.Integer,primary_key=True,autoincrement=True)
    descripcion = Column(type_=types.String(length=45))
    orden = Column(type_=types.Integer,nullable=False)
    #el foreignKey solo permite validar la relacion entre modelos
    receta_id = Column(ForeignKey(column='recetas.id'),type_=types.Integer)
    
    #el relationship permite navegar entre modelos
    #backref crea un atribut virtual, para acceder a otra subtabla
    receta=orm.relationship('Receta',backref='preparaciones')

    #crea la tabla preparaciones    
    __tablename__ = 'preparaciones'

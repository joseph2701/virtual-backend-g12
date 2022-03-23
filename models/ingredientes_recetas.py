from config import conexion
from sqlalchemy import Column,types,orm
from sqlalchemy.sql.schema import ForeignKey

class IngredientesRecetas(conexion.Model):
    id = Column(type_=types.Integer,primary_key=True,autoincrement=True)
    unidad_medida = Column(type_=types.String(length=45),nullable=False)
    ingrediente_id = Column(ForeignKey(column='ingredientes.id'),type_=types.Integer)
    receta_id = Column(ForeignKey(column='recetas.id'),type_=types.Integer)


    #el relationship permite navegar entre modelos
    #backref crea un atribut virtual, para acceder a otra subtabla
    receta=orm.relationship('Receta',backref='receta_ingredientes')
    ingrediente=orm.relationship('Ingrediente',backref='ingrediente_recetas')

    #crea la tabla ingrediente_receta
    __tablename__ = 'ingredientes_recetas'
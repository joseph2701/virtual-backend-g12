from models.categorias import Categoria
from config import conexion
from sqlalchemy import or_
#leer en la db si no existe las categorias:'OCIO','COMIDA','EDUCACION','VIAJES'

def categoriaSeed():
    #Si existe las categorias no se ignresas #si no si se ignresa
    conexion.session.query(Categoria).filter(
        or_(Categoria.nombre.like('%OCIO%'),Categoria.nombre.like('%COMIDA%'),
        )).first()
    pass

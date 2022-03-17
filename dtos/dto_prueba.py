from config import validador
from marshmallow import fields,validate

#validador de request
class ValidadorPrueba(validador.Schema):
    nombre=fields.Str(calidate=validate.Length(max=10))
    apellido=fields.Str()
    edad=fields.Int()
    soltero=fields.Bool()

    #class Meta:
        #es una clase que apsara parametros a la amedata padre de la cual estamos heredando
    #    fields=['nombre','apellido']

#validador d response
class ValidadorUsuarioPrueba(validador.Schema):
    nombre=fields.Str()
    apellido=fields.Str()        
    edad=fields.Int()
    soltero=fields.Bool()
from django.db import models

# Create your models here.
class Etiqueta(models.Model):
    #    https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
    #   https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options
    id=models.AutoField(primary_key=True,unique=True,null=False)
    nombre=models.CharField(max_length=20,unique=True,null=False)
    #Columnas de auditoria
    #son columnas que ayudan al seguimiento de cracion de registros
    #fecha en la que se creo el registro
    createdAt =models.DateTimeField(auto_now_add=True,db_column='created_at')
    #fecha en la que se modifico el registro
    updateAt=models.DateTimeField(auto_now=True,db_column='updated_at')


class Metea:
    #cambia el nombre de la tabla en la db ()
    db_table='etiquetas'
    # osea ASC del nombre, solo para GET mediante ORM
    ordering=['-nombre']
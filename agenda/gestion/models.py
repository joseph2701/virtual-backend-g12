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
    class Meta:
        #cambia el nombre de la tabla en la db ()
        db_table='etiquetas'
        # osea ASC del nombre, solo para GET mediante ORM
        ordering=['-nombre']


class Tareas(models.Model):
    #    https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
    #   https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options
    class CategoriasOpciones(models.TextChoices):
        #el primero es el nombre que se guarda en la db, y el segundo nombre
        #son los valores que se muestran usando templates para
        #jinga o DRF django RestFramework
        TODO='TODO','TO_DO'
        IN_PROGRESS='IP','IN_PROGRESS'
        DONE='DONE','DONE'
        CANCELLED='CANCELLED','CANCELLED'

    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=45,unique=True,null=False)
    categoria=models.CharField(max_length=45,choices=CategoriasOpciones.choices,default=CategoriasOpciones.TODO)

    #OTRA FORMA USANDO TUPLAS
    # categorias=models.CharField(max_length=45,choices=[
    #   ('TODO','TO_DO'),
    #   ('IP','IN_PROGRESS'),
    #   ('DONE','DONE'),
    #   ('CANCELLED','CANCELLED')
    # ],default='TODO')

    fechaCaducidad=models.DateTimeField(db_column='fecha_caducidad')
    importancia=models.IntegerField(null=False)
    descripcion=models.TextField(null=True)
    #Columnas de auditoria
    #son columnas que ayudan al seguimiento de cracion de registros
    #fecha en la que se creo el registro
    createdAt =models.DateTimeField(auto_now_add=True,db_column='created_at')
    #fecha en la que se modifico el registro
    updateAt=models.DateTimeField(auto_now=True,db_column='updated_at')
    
    #solo se usa esta forma, cuando la tabla es de muchos a muchos y solo us foreign keys
    etiquetas=models.ManyToManyField(to=Etiqueta,related_name='tareas')
    foto=models.ImageField(
        #sirve para inidicar el url, si no existe lo crea
        upload_to='multimedia',
        null=True
    )
    class Meta:
        #cambia el nombre de la tabla en la db ()
        db_table='tareas'
        # osea ASC del nombre, solo para GET mediante ORM
        #ordering=['-nombre']

#si la tabla tiene campos aparte
#   class TareasEtiquetas(models.Model):
#   EtiquetaFK=models.ForeignKey(To=Etiqueta)
#   TareaFK=models.ForeignKey(To=Tareas)
#   las demas columnas


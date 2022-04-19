from django.db import models
from cloudinary import models as modelsCloudinary

class Plato(models.Model):    
    # class CategoriasOpciones(models.TextChoices): 
    #     TODO='TODO','TO_DO'
    #     IN_PROGRESS='IP','IN_PROGRESS'
    #     DONE='DONE','DONE'
    #     CANCELLED='CANCELLED','CANCELLED'

    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=45,unique=True,null=False)
     #foto=models.ImageField(upload_to='multimedia',null=True)
    foto=modelsCloudinary.CloudinaryField( folder='plato')
    disponible=models.BooleanField(default=True,null=False)
    precio=models.FloatField(null=False)
    
    class Meta:
        db_table='platos'

class Stock(models.Model):
    id=models.AutoField(primary_key=True)
    fecha=models.DateField(null=False)         
    cantidad=models.IntegerField(null=False)
    precio_diario=models.FloatField(null=False)
    #related_name > servira para ingresar desde el mdoelo del cual se esta creando la relacion
    #desde platos podremos ingresar a todo sus stocks
    #ondelete> que accion toara cuando se desee elminar el padre
        #CASCADE: eliminara el registro del plato y todo los stocjs que tengan ese registro tbn
        #PROTECT: impedira que se realice la eliminacion del Plato si tiene stocks
        #SET_NULL: eliminara el plato y sus stocks colocara en su fk el valor de null
        #DO_NOTHING: eliminara el plato y no cambiara nada de los stocks(seguiran con el mismo valor ya eliminado)
        #RESTRICT: no permite la eliminacion y anza un error de restriccion
    platoId=models.ForeignKey(to=Plato,related_name="stocks",on_delete=models.CASCADE,db_column='plato_id')
    class Meta:
        db_table='stocks'
        #unique-together: crea un indice de dos o mas columnas
        unique_together=[['fecha','platoId']]

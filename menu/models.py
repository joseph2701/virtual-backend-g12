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
from rest_framework import  serializers
from .models import Tareas,Etiqueta
class PruebaSerializer(serializers.Serializer):
    nombre=serializers.CharField(max_length=40,trim_whitespace=True)
    apellido=serializers.CharField()
    correo=serializers.EmailField()
    dni=serializers.RegexField(max_length=8,min_length=8,regex="[0-9]")
    #dni=serializers.IntegerField(min_value=10000000,max_value=99999999)

class TareasSerializer(serializers.ModelSerializer):
    #esto setetea la configuracion para el serializador
    foto=serializers.CharField(max_length=100)
    class Meta:
        model=Tareas 
        fields='__all__'
        extra_kwargs={
            'etiquetas':{
                'write_only':True
            }
        }
        #o se usa fields, o se usa exclude
        # indica que columnas no quiero utilizar
        #exclude=['importancia']
       # depth=1
        #la profundidad max es 10

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tareas
        fields='__all__'
        depth=1

class EtiquetaSerializer(serializers.ModelSerializer):
    #se usa para acceder al related name llamado en el otro lado
    #readonly es para indicarle solo para GET

    tareas=TareaSerializer(many=True,read_only=True)
    #otra forma:
    #no_es_tareas=TareaSerializer(many=True,read_only=True,Source=True)
    
    class Meta:
        model=Etiqueta
        fields='__all__'
        #aqui se puede colocar los campos os cuales n se van a utilizar 
        #en una de las vistas
        extra_kwargs={
            'nombre':{'write_only':True},
            'id':{'read_only':True},
        }
        #asigna los campos que serean solo lectura
        read_only_fields=['createAt']
        # write_only_fields=['createAt']   NO EXISTEEEE

class TareaPersonalizableSerializer(serializers.ModelSerializer):
    class Meta:
        model=TareasSerializerfields='__all__'
        extra_kwargs={
            'nombre':{'read_only':True}
        }

class ArchivoSerializer(serializers.Serializer):
    #max leng indica longitud maxima del nombre
    #use_url si es True, retornara el link completo de la ubc del archivo
    archivo=serializers.ImageField(max_length=100,use_url=True)
    class Meta:
        model=TareasSerializerfields='__all__'
        extra_kwargs={
            'nombre':{'read_only':True}
        }


class EliminarArchivoSerializer(serializers.Serializer):
    archivo=serializers.CharField(max_length=100)
    # class Meta:
    #     model = TareasSerializerfields='__all__'        
    #     def delete(self, instance, *arg, **kwargs):
    #         profile = instance.profiles
    #         profile.delete()
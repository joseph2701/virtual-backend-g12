from rest_framework import  serializers
from .models import Tareas,Etiqueta
class PruebaSerializer(serializers.Serializer):
    nombre=serializers.CharField(max_length=40,trim_whitespace=True)
    apellido=serializers.CharField()
    correo=serializers.EmailField()
    dni=serializers.RegexField(max_length=8,min_length=8,regex="[0-9]")
    #dni=serializers.IntegerField(min_value=10000000,max_value=99999999)

class TareaSerializer(serializers.ModelSerializer)    :

    class Meta:
        model=Tareas 
        fields='__all__'
        #o se usa fields, o se usa exclude
        # indica que columnas no quiero utilizar
        #exclude=['importancia']

class EtiquetaSerializer(serializers.ModelSerializer)    :

    class Meta:
        model=Etiqueta
        fields='__all__'
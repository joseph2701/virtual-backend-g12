from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView,ListCreateAPIView
from .serializers import PruebaSerializer,TareasSerializer,EtiquetaSerializer,TareaSerializer 
from .models import Tareas ,Etiqueta
from rest_framework import status
#from datetime import datetime
from django.utils import timezone

@api_view(http_method_names=['GET','POST'])
def inicio(request:Request):
    #request sera toda la informacion enviada por el cliente
    print(request.method)
    print(request)
    #comportamiento GET
    if request.method=='GET':
        return Response(data={
        'message':'Bienvenido a mi API de agenda'
        })
        #comportamiento POST
    elif request.method=='POST':
        return Response(data={
        'message':'Hiciste un post'
        })

class PruebaApiView(ListAPIView):
    #serializar por nosotros igual quqe un DTO
    serializer_class = PruebaSerializer
    queryset=[
        {
        'nombre':'Joseph',
        'apellido':'Mendoza',
        'correo':'mendoza785@hotmail.com',
        'dni':'44156456',
        'estado_civil':'soltero'
        },
        {
        'nombre':'Maria',
        'apellido':'Ramirez',
        'correo':'mramirez@gmail.com',
        'dni':'01234566',
        'estado_civil':'casada'
        }            
    ]


    def get(self,request:Request):
        informacion=self.queryset
        #uso serialierclass para filtrar la info necesaria
        informacion_serializada=self.serializer_class(data=informacion, many=True)
        informacion_serializada.is_valid(raise_exception=True)
        return Response(data={'message':'hola','content':informacion_serializada.data})

class TareasApiView(ListCreateAPIView):
    #select * from Tareas
    queryset=Tareas.objects.all()  
    serializer_class=TareasSerializer

    def post(self,request):
        serializador=self.serializer_class(data=request.data)
        if serializador.is_valid():
            #luego de ejecutar is_valid, se pueden usar::: retornan diccionarios
            #serializador.initial_data es data inicial sin validacion
            #serializador.validated_data es data ya validada
            #print(type( serializador.validated_Data.get('fechaCaducidad')))
            print( serializador.validated_data.get('fechaCaducidad'))
            fechaCaducidad=serializador.validated_data.get('fechaCaducidad')            
            importancia=serializador.validated_data.get('importancia')     
            #if datetime.now(timezone.utc)>fechaCaducidad:
            #otra forma
            if importancia<0 or importancia>10:
                return Response(
                    data={
                        'message':'importancia no esta entre 0 - 10'
                    },status=status.HTTP_400_BAD_REQUEST
                )
            
            if timezone.now()>fechaCaducidad:
                return Response(
                    data={
                        'message':'Fecha no puede ser menor que la fecha actual'
                    },status=status.HTTP_400_BAD_REQUEST
                )
            else:
                return Response(data='Registrado con exito',status=status.HTTP_201_CREATED)
        else:
            #muestra los errores
            #   serializador.errors
            return Response(
                data={
                    'mensaje':'La data no es valida',
                    'content':serializador.errors},
                status=status.HTTP_400_BAD_REQUEST
            )




class EtiquetasApiView(ListCreateAPIView):
    #select * from Tareas
    queryset=Etiqueta.objects.all()  
    serializer_class=EtiquetaSerializer

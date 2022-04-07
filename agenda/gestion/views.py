from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView,ListCreateAPIView
from .serializers import PruebaSerializer,TareaSerializer,EtiquetaSerializer 
from .models import Tareas ,Etiqueta

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
    serializer_class=TareaSerializer

class EtiquetasApiView(ListCreateAPIView):
    #select * from Tareas
    queryset=Etiqueta.objects.all()  
    serializer_class=EtiquetaSerializer

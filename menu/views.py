from .models import Plato,Stock
from rest_framework.generics import ListCreateAPIView,CreateAPIView
from .serializers import (  PlatoSerializer,
                            StockSerializer,
                            PedidoSerializer,
                            AgregarDetallePedidoSerializer
                        )
from rest_framework.permissions import (AllowAny,  # sirve para que el controlador sea publico (no se necesite una token)
                                        # Los controladores soliciten una token de acceso
                                        IsAuthenticated,
                                        # Solamente para los metodos GET no sera necesaria la token pero para los demas metodos (POST, PUT, DELETE, PATCH) si sera requerido
                                        IsAuthenticatedOrReadOnly,
                                        # Verifica que en la token de acceso buscara al usuario y vera si es superuser (is_superuser)
                                        IsAdminUser,

                                        )
from rest_framework.response import Response
from rest_framework.request import Request
from cloudinary import CloudinaryImage
from .permissions import SoloAdminPuedeEscribir,SoloMozoPuedeEscribir
from fact_electr.models import Pedido,DetallePedido
from rest_framework import status
from django.utils import timezone
class PlatoApiView(ListCreateAPIView):
    serializer_class = PlatoSerializer
    queryset = Plato.objects.all()
    # sirve para indicar que tipos de permisos necesita el cliente para poder realizar la peticion
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request):
        data = self.serializer_class(instance=self.get_queryset(), many=True)
        # hacer una iteracion para modificar la foto de cada plato y devolver el link de la foto
        print(data.data[1].get('foto'))
        # del contenido de la foto solamente extraer el nombre del archivo o si esta en una carpeta extraer la carpeta y el archivo
        link = CloudinaryImage(
            'plato/u3aj7qh0dtmy73yanv5j.jpg').image(secure=True)

        print(link)
        return Response(data=data.data)

class StockApiView(ListCreateAPIView):
    serializer_class=StockSerializer
    queryset=Stock.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly,SoloAdminPuedeEscribir]

class PedidoApiView(ListCreateAPIView):
    queryset=Stock.objects.all()
    serializer_class=PedidoSerializer
    permission_classes=[IsAuthenticatedOrReadOnly,SoloMozoPuedeEscribir]
    def post(self,request: Request):
        print(request.user)
        request.data['usuarioId']=request.user.id
        data=self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response(data=data.data,status=status.HTTP_201_CREATED)

class AgregarDetallePedidoApiView(CreateAPIView):
    queryset=DetallePedido.objects.all()
    serializer_class=AgregarDetallePedidoSerializer
    def post(self,request: Request):
        #valido la data        
        data=self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        # {
            # "cantidad":2,
            # "plato":1,
            # "pedido_id":2
        # }
        #verifico que tenga cantidad de productos en stock
        #select top 1 * from stocks where fecha='...' and plato_id
        stock=Stock.objects.filter(
            fecha=timezone.now(),
            platoId=data.validated_data.get('platoId')
        ).first()
        print(stock)
        #agrego el detalle data=self.serializer_class(data=request.data)
        if stock is None:                
            return Response(data={'message':'No hay stck para este producto'},status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'message':'Detalle creado exitosamente'},status=status.HTTP_201_CREATED)
        # data.save()
        # return Response(data=data.data,status=status.HTTP_201_CREATED)
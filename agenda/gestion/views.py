from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView

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
    serializer_class = None
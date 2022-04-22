import requests
from django.db import connection
from .models import Comprobante,Pedido
from os import environ

def generar_comprobante(tipo_de_comprobante: int,tipo_documento:str,numero_documento:str,pedido_id:int):
    """Sirve para generar un comprobante electronico ya sea Factura, Boleta, Nota de Credito de un pedidos."""
    pedido=Pedido.objects.filter(id=pedido_id).first()
    if pedido is None:
        raise Exception('Pedido no existe')

    if pedido.total>700 and tipo_documento is None:
        raise Exception('El pedido mayor a 700, requiere un cliente')

    operacion='generar_comprobante'
    tipo=''
    sunat_transaction=1
    if tipo_de_comprobante==1:
        #esta serie se deberia de guardar en la bd en una tabla de series para que cuando
        #el contador desee cambiar de serie se modifique enea tabla de series
        serie='FFF1' #Serie.objects.filter(tipo='FACTURA').first()
        tipo='FACTURA'
    elif tipo_de_comprobante==2:
        serie='BBB1'
        tipo='BOLETA'
    elif tipo_de_comprobante==3 or tipo_de_comprobante==4:
        serie='0001'
        tipo='NOTA'   

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM vista_prueba')

    #select * from comprobantes where tipo='boleta | 'factura' order by numero desc
    ultimoComprobante=Comprobante.objects.values_list('numero','serie').filter(tipo=tipo).order_by('-numero').first()


    if ultimoComprobante is None:
        numero=12
    else:
        numero=int(ultimoComprobante[0]+1)
    
    if tipo_documento is None:
        cliente_tipo_de_documento='-'
        cliente_numero_de_documento=None
    else:
        cliente_tipo_de_documento=tipo_documento
        cliente_numero_de_documento=numero_documento
        cliente_denominacion=''
        if tipo_documento=='RUC':
            respuesta_apiperu=requests.get("https://apiperu.dev/api/ruc/"+numero_documento,
                        headers={'Authorization':'Bearer'+environ.get('APIPERU_TOKEN')})
            if respuesta_apiperu.json().get('success')==False:
                raise Exception('Datos del cliente no validos')
            else:
                cliente_denominacion=respuesta_apiperu.json.json().get('data').get('nombre_o_razon_social')
        elif tipo_documento=='DNI':
            respuesta_apiperu=requests.get("https://apiperu.dev/api/dni/"+numero_documento,
                        headers={'Authorization':'Bearer'+environ.get('APIPERU_TOKEN')})
            if respuesta_apiperu.json().get('success')==False:
                raise Exception('Datos del cliente no validos')
            else:
                cliente_denominacion=respuesta_apiperu.json.json().get('data').get('noombre_completo') 
        


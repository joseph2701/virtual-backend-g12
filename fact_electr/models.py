from django.db import models
from autorizacion.models import Usuario
from menu.models import Stock

class Pedido(models.Model):    
    id=models.AutoField(primary_key=True)    
    fecha=models.DateTimeField()
    total=models.FloatField(null=False)
    numeroDocumentoCliente=models.CharField(max_length=12)
    tipoDocumentoCliente=models.CharField(choices=(['RUC','RUC'],['DNI','DNI']),max_length=5)
    mesa=models.IntegerField(null=False)
    propina=models.IntegerField()

    # comprobante=models.OneToOneField(
    #     to=Usuario,related_name='pedidos',on_delete=models.CASCADE, db_column='usuario_id' 
    # )

    usuarioId=models.ForeignKey(to=Usuario,related_name="pedidos",on_delete=models.CASCADE,db_column='usuario_id')

    class Meta:
        db_table='pedidos'
   
class detalle_pedidos(models.Model):    
    id=models.AutoField(primary_key=True,null=False)    
    cantidad=models.IntegerField()    
    stockId=models.ForeignKey(to=Stock,related_name="detalle_pedidos",on_delete=models.CASCADE,db_column='stock_id')
    pedidoId=models.ForeignKey(to=Pedido,related_name="detalle_pedidos",on_delete=models.CASCADE,db_column='pedido_id')

    class Meta:
        db_table='detalle_pedidos'
   
class Comprobante(models.Model):
    id=models.AutoField(primary_key=True)    
    serie=models.CharField(max_length=5,null=False)
    numero=models.CharField(max_length=5,null=False)
    pdf=models.TextField()
    cdr=models.TextField()
    xml=models.TextField()
    tipo=models.CharField(max_length=10,choices=(['BOLETA','BOLETA'],['FACTURA','FACTURA']),null=False)
    pedido=models.OneToOneField(
        to=Pedido,related_name='comprobante',on_delete=models.CASCADE,db_column='pedido_id'
    )
    class Meta:
        db_table='comprobantes'
        unique_together=[['serie','numero']]

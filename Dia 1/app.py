from flask import Flask,request
from datetime import datetime
from flask_cors import CORS
#__name__ sirve para msotrar el archivo raiz
# 127.0.0.1:5000
app = Flask(__name__)
#inicializaremos  nuestro servidor Flask
CORS(app=app,origins=['http://127.0.0.1:5500','https://www.mifrontend.com','https://miapp.vercel.app'],
methods='*',allow_headers=['Content-Type'])
clientes=[
    {    
        "country": "Peru",
        "description": "description Joseph",
        "name": "Joseph",
        "organos": True,
        "photo": "photo Joseph",
        "id":1        
    }
] 

def buscar_cliente(id):
    resultado=None

    #for cliente in clientes:
        #   if cliente.get('id')==id:
        #       return cliente.get('id')
        #       break
    
    for posicion in range(0,len(clientes)):
        cliente=clientes[posicion]
        if cliente.get('id')==id:
            return(cliente,posicion)            
    
@app.route('/') 
def info_app():
    #formato a fecha strftime()
    hora_del_servidor=datetime.now()

    return{
        'status':True,
        'Hour':hora_del_servidor.strftime("%d-%m-%Y %H:%M:%S")
    }


@app.route('/clientes',methods=['POST','GET'])
def obtener_clientes():
    #request.method : muestra el tipo de metodo de consulta de aprte delf ront
    print(request.method)
    print(request.get_json())
    if request.method =='POST':
        data=request.get_json()   
        data['id']=len(clientes)+1
        clientes.append(data)
        return{
            #'message':'{} agregado exitosamente'.format(data.get('name', default=None)),
            'message':'agregado exitosamente',
            'client':data        
        }
    else:
        return{
            'message':'lista de clientes',
            'client':clientes
        }


@app.route('/cliente/<int:id>',methods=['GET','PUT','DELETE'])
def gestion_cliente(id):
    print (id)
    if request.method=='GET':
       [cliente,posicion]=buscar_cliente(id)
       if cliente:
            return cliente
       else:
            return{
                'message':'el cliente a buscar, no se encontro'
            },404
    elif request.method=='PUT':
        resultado=buscar_cliente(id)
        if resultado:
            #hacemos la destructuracion de la tupla otenida
            [cliente,posicion]=resultado
            #modificar el cliente a buscar, no se encontro
            #extraemos info del body a una  variable
            data=request.get_json()
            #se arega una llave 'id' al diccionario en la posicion 0 de la tupla encontrada
            #cliente=resultado[0]>cliente
            #resultado=resultado[1]>posicion
            #modificar ese cliente con el nuevo valor
            data['id']=id
            clientes[posicion]=data
            return clientes[posicion]
        else:
            return {
                'message':'el cliente a buscar, no se encontro'
            },404
    elif request.method=='DELETE':
        resultado=buscar_cliente(id)
        if resultado:            
            [cliente,posicion]=resultado
            data=request.get_json()                        
            cliente_eliminado=clientes.pop(posicion)
            return {
                'message':'cliente eliminado exitosamente',
                'cliente':cliente_eliminado
            }
        else:
            return {
                'message':'el cliente a eliminar, no se encontro'
            },404
      
#modo debugging : es modo prueba, cada vez que guardemos
#el servidor se reiniciara automaticamente
app.run(debug=True)
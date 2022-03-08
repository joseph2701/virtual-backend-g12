from flask import Flask,request
from datetime import datetime
#__name__ sirve para msotrar el archivo raiz
# 127.0.0.1:5000
app = Flask(__name__)
#inicializaremos  nuestro servidor Flask

clientes=[] 

@app.route('/') 
def info_app():
    #formato a fecha strftime()
    hora_del_servidor=datetime.now()

    return{
        'status':True,
        'Hour':hora_del_servidor.strftime("%d-%m-%Y %H:%M:%S")
    }

@app.route('/clientes',methods=['POST'])
def estado():
    #request.method : muestra el tipo de metodo de consulta de aprte delf ront
    print(request.method)
    data=request.get_json()
    clientes.append(data)
    return{
        'message':'{} agregado exitosamente'.format(data.get('name', default=None)),
        'client':data        
    }




#modo debugging : es modo prueba, cada vez que guardemos
#el servidor se reiniciara automaticamente
app.run(debug=True)
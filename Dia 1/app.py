from flask import Flask
from datetime import datetime
#__name__ sirve para msotrar el archivo raiz
# 127.0.0.1:5000
app = Flask(__name__)
#inicializaremos  nuestro servidor Flask
@app.route('/') 
def info_app():
    #formato a fecha strftime()
    hora_del_servidor=datetime.now()

    return{
        'status':True,
        'Hour':hora_del_servidor.strftime("%d-%m-%Y %H:%M:%S")
    }

@app.route('/clientes')
def estado():
    return{
        'mensaje':'cliente agregado exitosamente'
    }




#modo debugging : es modo prueba, cada vez que guardemos
#el servidor se reiniciara automaticamente
app.run(debug=True)
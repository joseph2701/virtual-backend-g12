from flask import Flask
from datetime import datetime
#__name__ sirve para msotrar el archivo raiz
# 127.0.0.1:5000
app = Flask(__name__)
#inicializaremos  nuestro servidor Flask
@app.route('/')
#modificare el comportamiento del metodo route
def inicial():
    #siempre en los controladores hay que enviar respuesta
    print('Me llamaron!')
    return 'Bienvenido a mi API 😎'

@app.route('/api/info')
def info_app():
    #formato a fecha strftime()
    return{
        'fecha':datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

#modo debugging : es modo prueba, cada vez que guardemos
#el servidor se reiniciara automaticamente
app.run(debug=True)
#lo que se ejecute luego del run, nunca llegara a ejecutarse
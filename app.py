from flask import Flask
from datetime import datetime
from flask_restful import Api
from controllers.ingredientes import IngredientesController
from config import conexion

app=Flask(__name__)
#creamos la instancia de flask_restul.Api
api=Api(app=app)

# Ahora asignaremos la cadena de conexion a nuestra base de datos
#                                       tipo://usuario:password@dominio:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:jmendoza2701@127.0.0.1:3306/recetario'


# para jalar la configuracion de mi flask y extraer su conexion a la base de datos
conexion.init_app(app)

# con el siguiente comando indicaremos la creacion de todas las tablas en la bd
# emitira un error si es que no hay ninguna tabla a crear 
# emitira un error si no le hemos instalado el conector correctamente
# tenemos que declarar en el parametro app nuestra aplicacion de flask
conexion.create_all(app=app)

@app.route('/status',methods=['GET'])

def status():
    return{
        'status': True,
        'date' : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

@app.route('/')
def inicio():
    return 'Bienvenido a mi API de recetas'

#definimos las rutas a ser suadas por un controlador especifico
api.add_resource(IngredientesController,'/Ingredientes','/Ingrediente')

#comprueba que solo se corra una instancia
#en un proyecto
if __name__ == '__main__':
    app.run(debug=True)


print ('hola')
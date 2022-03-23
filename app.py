from flask import Flask
from datetime import datetime
from flask_restful import Api
from controllers.ingredientes import (  IngredientesController, 
                                        PruebaController, 
                                        IngredienteController )

from controllers.recetas import (RecetasController,BuscarRecetaController,RecetaController)
from controllers.preparaciones import PreparacionesController
from controllers.ingredientes_recetas import IngredientesRecetasRequestDTO
from controllers.ingredientes_recetas import IngredientesRecetasControllers
from config import conexion, validador
from dotenv import load_dotenv
from os import environ

load_dotenv()
print(environ.get('NOMBRE'))


app=Flask(__name__)
#creamos la instancia de flask_restul.Api
api=Api(app=app)

# Ahora asignaremos la cadena de conexion a nuestra base de datos
#                                       tipo://usuario:password@dominio:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] =environ.get('DATABASE_URL')
# si true -> sqlalchemy rastrea modificaicones de bjetos(modelos) y emite señales ante cmbios
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# para jalar la configuracion de mi flask y extraer su conexion a la base de datos
conexion.init_app(app)
#jala la config del proyecto flask y agrega la validacion al proyecto
validador.init_app(app)
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
api.add_resource(PruebaController, '/pruebas')
api.add_resource(IngredienteController, '/ingrediente/<int:id>')
api.add_resource(RecetasController, '/recetas', '/receta')
api.add_resource(RecetaController, '/receta/<int:id>')
api.add_resource(BuscarRecetaController, '/buscar_receta')
api.add_resource(PreparacionesController, '/preparacion')
api.add_resource(IngredientesRecetasControllers, '/ingrediente_receta')

#comprueba que solo se corra una instancia
#en un proyecto
if __name__ == '__main__':
    app.run(debug=True)
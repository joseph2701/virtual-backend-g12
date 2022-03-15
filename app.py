from ast import In
from flask import Flask
from datetime import datetime
from flask_restful import Api
from controllers.ingredientes import IngredientesController

app=Flask(__name__)
#creamos la instancia de flask_restul.Api
api=Api(app=app)

@app.route('/status',methods=['GET'])

def status():
    return{
        'status': True,
        'date' : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

#definimos las rutas a ser suadas por un controlador especifico
api.add_resource(IngredientesController,'/Ingredientes','/Ingrediente')


#comprueba que solo se corra una instancia
#en un proyecto
if __name__ == '__main__':
    app.run(debug=True)


print ('hola')
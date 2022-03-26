from flask import Flask,render_template
from flask_restful import Api
from controllers.usuarios import RegistroController,LoginController
from config import validador,conexion
from os import environ
from dotenv import load_dotenv

load_dotenv() 

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

api=Api(app=app)
validador.init_app(app)
conexion.init_app(app)
# conexion.drop_all(app=app)
conexion.create_all(app=app)
#
@app.route('/')
def inicio():
    pass
api.add_resource(RegistroController,'/registro')
api.add_resource(LoginController,'/login')
 
if(__name__ == '__main__'):
    app.run(debug=True,port=8080)

from flask import Flask,render_template
from flask_restful import Api
from controllers.usuarios import RegistroController,LoginController
from config import validador,conexion
from os import environ
from dotenv import load_dotenv
from flask_cors import CORS
from flask_jwt import JWT,jwt_required,current_identity
from seguridad import autenticador,identificador
from datetime import timedelta
from dtos.registro_dto import UsuarioResponseDTO

load_dotenv() 

app=Flask(__name__)
CORS(app=app)


app.config['SECRET_KEY']='secreto'
app.config['SQLALCHEMY_DATABASE_URI'] =environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#PARA CAMBIAR EL END POINT
app.config['JWT_AUTH_URL_RULE']='/login-jwt'
#PARA AMIAR EL USERNAME
app.config['JWT_AUTH_USERNAME_KEY']='correo'
#PARA CAMBIAR EL PASSWORD
app.config['JWT_AUTH_PASSWORD_KEY']='pass'
#PÀRA CAMBIAR EL TIEMPO DE EXP DEL TOKEN
app.config['JWT_EXPIRATION_DELTA']=timedelta(hours=1,minutes=5)
#para identificar la autorizacion prefijo
app.config['JWT_AUTH_HEADER_PREFIX']='Bearer'
jsonwebtoken=JWT(app=app,authentication_handler=autenticador,identity_handler=identificador)

api=Api(app=app)
validador.init_app(app)
conexion.init_app(app)
# conexion.drop_all(app=app)
conexion.create_all(app=app)
#
@app.route('/')


def inicio():
    pass

@app.route('/user')
#indicamos que apra este controlador se debera proveer una JWT valida
@jwt_required()
def perfil_usuario():
    print(current_identity)
    #serializa el usuasrio
    usuario=UsuarioResponseDTO().dump(current_identity)
    return{
        'message':'El usuario es: %s' % current_identity,
        'content':usuario
    }

api.add_resource(RegistroController,'/registro')
api.add_resource(LoginController,'/login')


if(__name__ == '__main__'):
    app.run(debug=True,port=8080)

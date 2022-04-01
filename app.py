from flask import Flask,render_template,request
from flask_restful import Api
from controllers.usuarios import (ResetPasswordController, RegistroController, LoginController)
from config import validador,conexion
from os import environ
from dotenv import load_dotenv
from flask_cors import CORS
from flask_jwt import JWT,jwt_required,current_identity
from seguridad import autenticador,identificador
from datetime import timedelta
from dtos.registro_dto import UsuarioResponseDTO
from seed import categoriaSeed
from controllers.movimientos import MovimientoController
from cryptography.fernet import Fernet
from datetime import datetime
load_dotenv() 
import json
from models.usuarios import Usuario

app=Flask(__name__)
CORS(app=app)

app.config['SECRET_KEY']=environ.get('JWT_SECRET_KEY')
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
@app.before_first_request
def seed():
    #ahora ahcemos el seed de las tablas respectivas
    categoriaSeed()


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

@app.route('/validar-token',methods=['POST'])
def validar_token():
    #tarea agregar DTO para recibir token en el body
    #la token debe ser strign
    body=request.get_json()
    token=body.get('token')
    fernet=Fernet(environ.get('FERNET_SECRET_KEY'))

    #el decrypt decifra la token encriptada
    try:

        data=fernet.decrypt(bytes(token,'utf-8')).decode('utf-8')
        print(data)
        diccionario=json.loads(data)
        fecha_caducidad=datetime.strptime(diccionario.get('fecha_caducidad'),'%Y-%m-%d %H:%M:%S.%f')
        hora_actual=datetime.now()
        #print(fecha_caducidad)
        if hora_actual <= fecha_caducidad:
            print('todavia hay tiempo')
            #with_entities:: selecciona que columnas queremos del modelo (tabla)
            usuarioEncontrado= conexion.session.query(Usuario).with_entities(Usuario.correo).filter_by(id=diccionario.get('id_usuario')).first()
            if usuarioEncontrado:
                return{
                    'message':'Correcto',
                    'content':{
                        'correo':usuarioEncontrado.correo
                    }
                        
                }
            else:                
                return{
                    'message':'Usuario no existe'
                },400
        else:
            print('Ya no hay tiempo')
            return{
                'message':'la token caduco',                
            },400
    except Exception as e:
        return{
            'message':'Token incorrecta'
        },400

api.add_resource(RegistroController,'/registro')
api.add_resource(LoginController,'/login')
api.add_resource(MovimientoController,'/movimiento','/movimientos')
api.add_resource(ResetPasswordController,'/reset-password')


if(__name__ == '__main__'):
    app.run(debug=True,port=8080)

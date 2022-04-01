from flask_restful import Resource,request
from dtos.registro_dto import (RegistroDTO,UsuarioResponseDTO,LoginDTO)
from dtos.usuario_dto import ResetPasswordRequestDTO
from models.usuarios import Usuario
from config import conexion,sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email,To,Content,Mail
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os import environ 
import os
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
import json

class RegistroController(Resource):
    def post(self):
        body=request.get_json()
        try:
            data=RegistroDTO().load(body)
            nuevoUsuario=Usuario(**data)
            nuevoUsuario.encriptar_pwd()
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()
            respuesta=UsuarioResponseDTO().dump(nuevoUsuario)
            return{
                'message':'Usuario registrado exitosamente',
                'content':respuesta
            },201
        except Exception as e:
            conexion.session.rollback()
            return{
                'message':'Error al registrar al usuario',
                'content': e.args
            },400

class LoginController(Resource):
    def post(self):
        body=request.get_json()

        #hacer un DTO que solo reciba un correo y un password, el correo debe de ser emailk
        try:
            data=LoginDTO().load(body)
            return{
                'message':'Bienvenido'
            }
        except Exception as e:
            return{
                'message':'Credenciales incorrectas',
                'content': e.args
            }

class ResetPasswordController(Resource):
    def post(self):
        body=request.get_json()
        mensaje=MIMEMultipart()
        email_emisor=environ.get('EMAIL_EMISOR')
        email_password=environ.get('EMAIL_PASSWORD')
        try:
            data=ResetPasswordRequestDTO().load(body)
            usuarioEncontrado=conexion.session.query(Usuario).filter_by(correo=data.get('correo')).first()
            if usuarioEncontrado is not None:                
                mensaje['Subject']='Reiniciar contraseña Monedero APP'

                #generar propia key de Fernet
                #Fernet.generate.key()
                fernet=Fernet(environ.get('FERNET_SECRET_KEY'))

                mensaje_secreto={
                    #aqui damos el tiempo valido de la key
                    'fecha_caducidad':str(datetime.now()+timedelta(hours=1)),
                    'id_usuario':usuarioEncontrado.id
                }
                mensaje_secreto_str=json.dumps(mensaje_secreto)
                mensaje_encriptado=fernet.encrypt(bytes(mensaje_secreto_str,'utf-8'))

                #texto='Hola, este es un mensaje de prueba'   
                #si queremos un generador de correos con diseño: http://beefree.io/
                html= open('email_templates/joshua_template.html').read().format(usuarioEncontrado.nombre,environ.get('URL_FRONT')+'/reset-password?token='+mensaje_encriptado.decode('utf-8'))
                #mensaje.attach(MIMEText(texto,'plain'))
                mensaje.attach(MIMEText(html,'html'))
                ##inicio ell envio del correo
                # outlook ->  outlook.office365.com |587
                ##gmail -> smtp.gmail.om |587
                ##icloud -> smtp.mail.me.com |587
                ##yahoo -> smtp.mail.yahoo.com |587
                ##hotmail -> smtp.live.com  |587
                
                emisorSMTP=SMTP('smtp-mail.outlook.com',587)
                emisorSMTP.starttls()
                ##se ahce el login de mi servidor del correo
                emisorSMTP.login(email_emisor,email_password)
                emisorSMTP.sendmail(
                    from_addr=email_emisor,
                    to_addrs=usuarioEncontrado.correo,
                    msg=mensaje.as_string()                      
                )
                emisorSMTP.quit()
                print('Mensaje enciado exitosamente')
            return{
                'message':'Correo enviado exitosamente'
            }
        except Exception as e:
            return{
                'message':'Error al enviar el correo',
                'content':e.args
            }
        #------------------------------------------------
        # body = request.get_json()
        # try:            
        #     data=ResetPasswordRequestDTO().load(body)
        #     usuarioEncontrado=conexion.session.query(Usuario).filter_by(correo=data.get('correo')).first()
        #     if usuarioEncontrado is not None:
        #         print('llegue antes de correo')
        #         print(usuarioEncontrado.correo)
        #         ##utilizar correos verificados en sendgrid 
        #         ##usar un correo no verificado nunca llegara
        #         from_email=Email('asistentesistemas@zonacel.pe')                
        #         to_email=To(usuarioEncontrado.correo)
        #         subject='Reinicia tu contraseña del Monedero App'
        #         content=Content('text/plain','Hola, has solicitado el reinicio de tu password, haz clic en el siguiente link apra cambiar, sino has sido tu ignora este mensaje')                
        #         mail=Mail(from_email,to_email,subject,content)
        #         envia_correo=sendgrid.client.mail.send.post(request_body=mail.get())
        #         #estado de respuesta de sendgrid
        #         print(envia_correo.status_code)
        #         ##cuerpo de rpta de sendgrid
        #         print(envia_correo.body) 
        #         ##caebeceras de rpta de sendgrid
        #         print(envia_correo.headers)                         
        #     return{
        #         'message':'Correo enviado exitosamente'
        #     }
        # except Exception as e:
        #     return{
        #         'message':'Error al resetar el password',
        #         'content':e.args
        #     }
    # #------------------------------------------------    
class UsuarioResponseDTO:

     def get(self):        
        usuarios: list[Usuario] = conexion.session.query(Usuario).filter_by(id_usuario=current_identity.id).all()        
        resultado=UsuarioResponseDTO(many=True).dump(movimientos)
        return{
            'message':'Los usuarios son',
            'content': resultado
        }
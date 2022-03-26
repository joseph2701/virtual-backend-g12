from config import conexion
from sqlalchemy import Column,types
from bcrypt import hashpw,gensalt
class Usuario(conexion.Model):
    __tablename__ = 'usuarios'
    id=Column(type_=types.Integer, primary_key=True,autoincrement=True)
    nombre=Column(type_=types.String(length=45))
    apellido=Column(type_=types.String(length=45))
    correo=Column(type_=types.String(length=45),nullable=False,unique=True)
    password=Column(type_=types.Text(),nullable=False)


    def encriptar_pwd(self):
        pass
        #password a bytes
        password_bytes=bytes(self.password,'utf-8')
        #usar metodo gensaly -> generar hash random combinado con password 
        # formando un nuevo hash generator
        salt=gensalt(rounds=10)
        # combinamos
        hash_password=hashpw(password_bytes, salt)
        #lo convierto a string para guardarlo en la debug
        hash_pwd_string=hash_password.decode('utf-8')
        #sobreescribo el valor del password en la instancia por el generado
        self.password=hash_pwd_string
        

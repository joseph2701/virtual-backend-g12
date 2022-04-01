from config import conexion
from models.usuarios import Usuario
from bcrypt import checkpw

class UsuarioJWT:
    def __init__(self,id,username):
        self.id=id
        self.username=username


#encargada de validar si las credenciales son correctas
def autenticador(username,password):
    if username and password:
        #bsucara en la db
        usuarioEncontrado=conexion.session.query(Usuario).filter_by(correo=username).first()
        if usuarioEncontrado:
            print('Se encontro el usuario')
            validacion=checkpw(bytes(password,'utf-8'),
            bytes(usuarioEncontrado.password,'utf-8'))
            
            if validacion is True:
                print('si es el password')
                return usuarioEncontrado

            else:
                return None
        else :
            return{
                'message':'error'
            }
    else:
        return None

def identificador(payload):
    usuarioEncontrado:Usuario | None = conexion.session.query(Usuario).filter_by(id=payload['identity']).first()
    if usuarioEncontrado:
        print('Usuario encontrado')
        return usuarioEncontrado
    else:
        return None
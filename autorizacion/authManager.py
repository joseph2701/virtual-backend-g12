from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """Clase que sirve para manejar el comportamiento del auth_user"""
    def create_user(self, correo,nombre,rol,password):
        """Creacion de un usuario sni el comando createsuperuser"""
        if not correo:
            raise ValueError("El user debe tener correo obligatorio")
        #normalizar el correo
        correo=self.normalize_email(correo)
        #manda a llamar al modelo usuario e iniciara su construccion
        nuevoUsuario=self.model(correo=correo,nombre=nombre,rol=rol)
        #el metodo set_password genera un ash de la pass bcrypt y SHA256
        nuevoUsuario.set_password(password)
        #sirve para direccionar la conexion a la db
        nuevoUsuario.save(using=self._db)
        return nuevoUsuario

    def create_superuser(self, correo,nombre,rol,password):
        """Creacion de un sa por consola"""
        usuario=self.create_user(correo,nombre,rol,password)
        #asigna que usuarios seran sa
        usuario.is_superuser=True
        usuario.is_taff=True
        usuario.save(using=self._db)   
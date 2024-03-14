from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

def generate_image_dirname(self, filename):
    url = 'fotosPerfil/{}/{}'.format(self.id,filename)
    return url
def generate_shield_dirname(self, filename):
    url = 'escudos/{}/{}'.format(self.nombre,filename)
    return url

class User(AbstractUser):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    idBd = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(max_length=100, unique=True)
    fotoPerfil = models.ImageField(upload_to= generate_image_dirname, null=True, blank=True, default='fotosPerfil/default.jpg')
    descripcion = models.TextField(max_length=3000, null=True, blank=True)
    contrasenia = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre','contrasenia']

class Equipo(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    idBd = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    modelImage = models.ImageField(upload_to= generate_shield_dirname, null=True, blank=True, default='fotosPerfil/default.jpg')
# Create your models here.

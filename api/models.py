from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

def generate_image_dirname(self, filename):
    url = 'fotosPerfil/{}/{}'.format(self.id,filename)
    return url
def generate_shield_dirname(self, filename):
    url = 'escudos/{}/{}'.format(self.id,filename)
    return url

class User(AbstractUser):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    idBd = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(max_length=100, unique=True)
    fotoPerfil = models.ImageField(upload_to= generate_image_dirname, null=True, blank=True, default='fotosPerfil/default.jpg')
    descripcion = models.TextField(max_length=3000, null=True, blank=True)
    contrasenia = models.CharField(max_length=255)
    equipoFavorito = models.ForeignKey('Equipo', on_delete=models.SET_NULL, null=True, blank=True)
    username = None

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre','contrasenia']

class Equipo(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    idBd = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    fotoEscudo = models.ImageField(upload_to= generate_shield_dirname, null=True, blank=True)

class Partido(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    idBd = models.AutoField(primary_key=True)
    estadio = models.CharField(max_length=255)
    status = models.IntegerField()
    jornada = models.IntegerField()
    fecha = models.DateTimeField(null=True, blank=True)
    equipoLocal = models.ForeignKey('Equipo', on_delete=models.CASCADE, null=False, blank=False, related_name='equipoLocal')
    equipoVisitante = models.ForeignKey('Equipo', on_delete=models.CASCADE, null=False, blank=False, related_name='equipoVisitante')
    golesLocal = models.IntegerField()
    golesVisitante = models.IntegerField()

class Valoracion(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    idBd = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('User', on_delete=models.CASCADE, null=False, blank=False)
    partido = models.ForeignKey('Partido', on_delete=models.CASCADE, null=False, blank=False)
    valoracion = models.IntegerField()
    hora = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ['usuario','valoracion','partido']

class Visualizacion(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    idBd = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('User', on_delete=models.CASCADE, null=False, blank=False)
    partido = models.ForeignKey('Partido', on_delete=models.CASCADE, null=False, blank=False)
    hora = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ['usuario', 'partido']

class Resena(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    idBd = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('User', on_delete=models.CASCADE, null=False, blank=False)
    partido = models.ForeignKey('Partido', on_delete=models.CASCADE, null=False, blank=False)
    comentario = models.TextField()
    hora = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ['usuario', 'comentario', 'partido']

class Seguido(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    idBd = models.AutoField(primary_key=True)
    seguidor = models.ForeignKey('User', on_delete=models.CASCADE, null=False, blank=False, related_name='seguidor')
    seguido = models.ForeignKey('User', on_delete=models.CASCADE, null=False, blank=False, related_name='seguido')
    hora = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ['seguidor', 'seguido']
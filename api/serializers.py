from rest_framework import serializers
from collections import OrderedDict
from .models import User, Equipo, Partido, Valoracion, Visualizacion, Resena, Seguido

class UserSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
    class Meta:
        model = User
        fields = ['id', 'idBd','nombre', 'correo', 'contrasenia', 'fotoPerfil', 'descripcion', 'equipoFavorito' ]
        extra_kwargs = {'contrasenia': {'write_only': True}}
    

    
    def create(self, validated_data):
        password = validated_data.pop('contrasenia')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id', 'idBd','nombre', 'fotoEscudo']

class PartidoSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
    class Meta:
        model = Partido
        fields = ['id', 'idBd','estadio', 'status', 'jornada', 'fecha', 'equipoLocal', 'equipoVisitante', 'golesLocal', 'golesVisitante']
    
class ValoracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valoracion
        fields = ['id', 'idBd','usuario', 'partido', 'valoracion', 'hora']

class VisualizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visualizacion
        fields = ['id', 'idBd', 'usuario', 'partido', 'hora']

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = ['id', 'idBd', 'usuario', 'partido', 'comentario', 'hora']

class SeguidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguido
        fields = ['id', 'idBd', 'seguidor', 'seguido', 'hora']
from rest_framework import serializers
from .models import User, Equipo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'idBd','nombre', 'correo', 'contrasenia', 'fotoPerfil', 'descripcion']
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
        fields = ['id', 'idBd','nombre', 'modelImage']
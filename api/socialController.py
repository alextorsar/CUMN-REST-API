from rest_framework.views import APIView
from .serializers import VisualizacionSerializer, ValoracionSerializer, ResenaSerializer, SeguidoSerializer
from .models import Visualizacion, Valoracion, Resena, Seguido
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt

def getVisualizaciones(userId):
    visualizaciones = Visualizacion.objects.filter(usuario=userId).all()
    serializer = VisualizacionSerializer(visualizaciones, many=True)
    return serializer.data

def getValoraciones(userId):
    valoraciones = Valoracion.objects.filter(usuario=userId).all()
    serializer = ValoracionSerializer(valoraciones, many=True)
    return serializer.data

def getResenas(userId):
    resenas = Resena.objects.filter(usuario=userId).all()
    serializer = ResenaSerializer(resenas, many=True)
    return serializer.data

def getSeguidos(userId):
    seguidos = Seguido.objects.filter(seguidor=userId).all()
    serializer = SeguidoSerializer(seguidos, many=True)
    return serializer.data

def getUltimasAccionesSociales(userId):
    visualizaciones = getVisualizaciones(userId)
    valoraciones = getValoraciones(userId)
    resenas = getResenas(userId)
    acciones = visualizaciones + valoraciones + resenas
    return acciones 
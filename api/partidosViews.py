from rest_framework.views import APIView
from .serializers import EquipoSerializer, UserSerializer, PartidoSerializer
from .models import Equipo, User, Partido
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt

class PartidoView(APIView):
    """
    def post(self, request):
            serializer = PartidoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)"""
    
    def get(self, request):
        equipos = Partido.objects.all()
        serializer = PartidoSerializer(equipos, many=True)
        return Response(serializer.data)
    
class PartidoIdView(APIView):
    def get(self, request, id):
        equipo = Partido.objects.get(idBd=id)
        serializer = PartidoSerializer(equipo)
        return Response(serializer.data)
    
class PartidosEquipoView(APIView):
    def get(self, request, id):
        partidos = Partido.objects.filter(equipoVisitante=id) | Partido.objects.filter(equipoLocal=id)
        serializer = PartidoSerializer(partidos, many=True)
        return Response(serializer.data)

class PartidosJornadaView(APIView):
    def get(self, request, jornada):
        partidos = Partido.objects.filter(jornada=jornada)
        serializer = PartidoSerializer(partidos, many=True)
        return Response(serializer.data)
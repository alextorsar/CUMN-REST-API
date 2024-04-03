from rest_framework.views import APIView
from ..serializers import PartidoSerializer
from ..models import Partido
from rest_framework.response import Response
from ..controllers.partidoController import getAllPartido, getPartidoById, getPartidosEquipo, getPartidosJornada

class PartidoView(APIView):
    def get(self, request):
        partidos = getAllPartido()
        return Response(partidos)
    
class PartidoIdView(APIView):
    def get(self, request, id):
        partido = getPartidoById(id)
        if partido is not None:
            return Response(partido)
        else:
            return Response({'mensaje': 'Partido no encontrado'}, status=404)
    
class PartidosEquipoView(APIView):
    def get(self, request, id):
        partidos = getPartidosEquipo(id)
        return Response(partidos)

class PartidosJornadaView(APIView):
    def get(self, request, jornada):
        partidos = getPartidosJornada(jornada)
        return Response(partidos)
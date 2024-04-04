from rest_framework.views import APIView
from ..serializers import PartidoSerializer
from ..models import Partido
from rest_framework.response import Response
from ..controllers.partidoController import getAllPartido, getPartidoById, getPartidosEquipo, getPartidosJornada, getPartidosStatus, setPartidoStatusTo2, setPartidoStatusTo1

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
    
class PartidosStatusView(APIView):
    def get(self, request, status):
        partidos = getPartidosStatus(status)
        return Response(partidos)
    
    def post(self, request):
        if ('status' in request.data):
            if int(request.data['status']) == 2:
                if ('hora' in request.data):
                    partido = setPartidoStatusTo2(request.data['id'], request.data['hora'])
                    return Response(partido)
                else:
                    return Response({'mensaje': 'Falta la hora del partido'}, status=400)
            elif int(request.data['status']) == 1:
                if ('golesLocal' in request.data) and ('golesVisitante' in request.data):
                    partido = setPartidoStatusTo1(request.data['id'], request.data['golesLocal'], request.data['golesVisitante'])
                    return Response(partido)
                else:
                    return Response({'mensaje': 'Faltan los goles del partido'}, status=400)
            else:
                return Response({'mensaje': 'Status no válido'}, status=400)
        else:
            return Response({'mensaje': 'Falta el status del partido'}, status=400)
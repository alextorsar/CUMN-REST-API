from ..serializers import PartidoSerializer
from ..models import Partido

def getAllPartido():
    partidos = Partido.objects.all()
    serializer = PartidoSerializer(partidos, many=True)
    return serializer.data

def getPartidoById(id):
    partido = Partido.objects.filter(idBd=id).first()
    serializer = PartidoSerializer(partido)
    return serializer.data

def getPartidosEquipo(equipoId):
    partidos = Partido.objects.filter(equipoVisitante=equipoId) | Partido.objects.filter(equipoLocal=equipoId)
    serializer = PartidoSerializer(partidos, many=True)
    return serializer.data

def getPartidosJornada(jornada):
    partidos = Partido.objects.filter(jornada=jornada)
    serializer = PartidoSerializer(partidos, many=True)
    return serializer.data
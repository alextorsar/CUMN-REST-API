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

def getPartidosStatus(status):
    partidos = Partido.objects.filter(status=status)
    serializer = PartidoSerializer(partidos, many=True)
    return serializer.data

def setPartidoStatusTo2(id, hora):
    partido = Partido.objects.filter(idBd=id).first()
    partido.status = 2
    partido.fecha = hora
    partido.save()
    serializer = PartidoSerializer(partido)
    return serializer.data

def setPartidoStatusTo1(id, golesLocal, golesVisitante):
    partido = Partido.objects.filter(idBd=id).first()
    partido.status = 1
    partido.golesLocal = golesLocal
    partido.golesVisitante = golesVisitante
    partido.save()
    serializer = PartidoSerializer(partido)
    return serializer.data
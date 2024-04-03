from ..serializers import EquipoSerializer
from ..models import Equipo
from .partidoController import getPartidoById

def getAllEquipo():
    equipos = Equipo.objects.all()
    serializer = EquipoSerializer(equipos, many=True)
    return serializer.data

def getEquipoById(id):
    equipo = Equipo.objects.filter(idBd=id).first()
    if equipo is not None:
        serializer = EquipoSerializer(equipo)
        return serializer.data
    else:
        return None

def getEquiposPartido(partidoId):
    partido = getPartidoById(partidoId)
    equipoLocal = getEquipoById(partido['equipoLocal'])
    equipoVisitante = getEquipoById(partido['equipoVisitante'])
    return equipoLocal, equipoVisitante

def getEquipoByName(nombre):
    equipo = Equipo.objects.filter(nombre=nombre).first()
    if equipo is not None:
        serializer = EquipoSerializer(equipo)
        return serializer.data
    else:
        return None
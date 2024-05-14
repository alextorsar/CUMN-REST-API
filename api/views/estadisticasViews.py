from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from ..controllers.socialController import getVisualizaciones
from ..controllers.equipoController import getEquiposPartido
from ..models import Partido
import jwt

def getPartidosVisualizados(userId):
    return len(getVisualizaciones(userId))

def getSegundosVisualizados(userId):
    return len(getVisualizaciones(userId)) * 5400

def getEquipoMasVisto(userId):
    visualizaciones = getVisualizaciones(userId)
    equipos = {}
    equipoMasVisto = -1
    maximasVisualizacinones = 0
    for visualizacion in visualizaciones:
        equipoLocal, equipoVisitante = getEquiposPartido(visualizacion['partido'])
        equipoLocalId = equipoLocal['idBd']
        equipoVisitanteId = equipoVisitante['idBd']
        if equipoLocalId in equipos:
            equipos[equipoLocalId] += 1
        else:
            equipos[equipoLocalId] = 1
        if equipos[equipoLocalId] > maximasVisualizacinones:
            equipoMasVisto = equipoLocal['idBd']
            maximasVisualizacinones = equipos[equipoLocalId]
        if equipoVisitanteId in equipos:
            equipos[equipoVisitanteId] += 1
        else:
            equipos[equipoVisitanteId] = 1
        if equipos[equipoVisitanteId] > maximasVisualizacinones:    
            equipoMasVisto = equipoVisitante['idBd']
            maximasVisualizacinones = equipos[equipoVisitanteId]
    return equipoMasVisto, maximasVisualizacinones

class EstadisticasView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        equipoMasVisto, vecesVisto = getEquipoMasVisto(payload['idBd'])
        response = Response({
            'numeroPartidos': getPartidosVisualizados(payload['idBd']),
            'numeroSegundos': getSegundosVisualizados(payload['idBd']),
            'equipoMasVisto': equipoMasVisto,
            'vecesVisto': vecesVisto,
        })
        return response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from ..controllers.socialController import getSeguidos, getUltimasAccionesSociales
from ..controllers.partidoController import getPartidoById
from ..controllers.equipoController import getEquipoById
import jwt

def getHoraDeAccion(accion):
    return accion['hora']

class UltimasAccionesSociales(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        userId = payload['idBd']
        seguidos = getSeguidos(userId)
        acciones = []
        for seguido in seguidos:
            acciones += getUltimasAccionesSociales(seguido['seguido'])
        acciones.sort(key=getHoraDeAccion, reverse=True)
        for accion in acciones:
            partido = getPartidoById(accion['partido'])
            equipoLocal = getEquipoById(partido['equipoLocal'])
            equipoVisitante = getEquipoById(partido['equipoVisitante'])
            accion['nombrePartido'] = "{}-{}".format(equipoLocal['nombre'], equipoVisitante['nombre'])
        return Response(acciones)


from rest_framework.views import APIView
from ..serializers import UserSerializer
from ..models import User
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from ..controllers.equipoController import getAllEquipo, getEquipoById, getEquiposPartido, getEquipoByName
import jwt

class EquipoView(APIView):   
    def get(self, request):
        equipos = getAllEquipo()
        return Response(equipos)
    
class EquipoIdView(APIView):
    def get(self, request, id):
        equipo = getEquipoById(id)
        if equipo is not None:
            return Response(equipo)
        else:
            return Response({'mensaje': 'Equipo no encontrado'}, status=404)

class EquipoNombreView(APIView):
    def get(self, request, nombre):
        equipo = getEquipoByName(nombre)
        if equipo is not None:
            return Response(equipo)
        else:
            return Response({'mensaje': 'Equipo no encontrado'}, status=404)

class PostEquipoFavoritoView(APIView):
    def post(self, request, favorito):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        user = User.objects.filter(idBd=payload['idBd']).update(equipoFavorito=favorito)
        user = User.objects.filter(idBd=payload['idBd']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    
class DeleteEquipoFavoritoView(APIView):
    def delete(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        user = User.objects.filter(idBd=payload['idBd']).update(equipoFavorito=None)
        user = User.objects.filter(idBd=payload['idBd']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
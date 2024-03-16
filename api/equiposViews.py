from rest_framework.views import APIView
from .serializers import EquipoSerializer, UserSerializer
from .models import Equipo, User
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt

class EquipoView(APIView):

    #Este método es para crear un nuevo equipo, está comentado porque es necesario crear más equipos
    """def post(self, request):
        serializer = EquipoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)"""
    
    def get(self, request):
        equipos = Equipo.objects.all()
        serializer = EquipoSerializer(equipos, many=True)
        return Response(serializer.data)
class EquipoIdView(APIView):
    def get(self, request, id):
        equipo = Equipo.objects.get(idBd=id)
        serializer = EquipoSerializer(equipo)
        return Response(serializer.data)

class EquipoNombreView(APIView):
    def get(self, request, nombre):
        equipo = Equipo.objects.get(nombre=nombre)
        serializer = EquipoSerializer(equipo)
        return Response(serializer.data)

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
    
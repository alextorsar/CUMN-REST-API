from rest_framework.views import APIView
from .serializers import ResenaSerializer
from .models import Resena
from .socialController import getResenas
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt

class ResenaView(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        data = request.data.copy()
        data['usuario'] = payload['idBd']
        serializer = ResenaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        resenas = getResenas(payload['idBd'])
        return Response(resenas)
    
    def delete(self, request, resena_id):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        resenia = Resena.objects.filter(idBd=resena_id).first()
        if resenia != None and resenia.usuario.idBd == payload['idBd']:
            resenia.delete()
            return Response({'message': 'Reseña eliminada correctamente'})
        else:
            return Response({'message': 'No se pudo elimar la reseña'}, status=400) 

class ResenaPartidoView(APIView):
    def get(self, request, partido_id):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        resenias = Resena.objects.filter(partido=partido_id).all()
        serializer = ResenaSerializer(resenias, many=True)
        return Response(serializer.data)
from rest_framework.views import APIView
from .serializers import SeguidoSerializer
from .models import Seguido
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt

class SeguidosView(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        data = request.data.copy()
        data['seguidor'] = payload['idBd']
        serializer = SeguidoSerializer(data=data)
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
        seguidos = Seguido.objects.filter(seguidor=payload['idBd'])
        serializer = SeguidoSerializer(seguidos, many=True)
        return Response(serializer.data)
    def delete(self, request, seguido_id):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        seguido = Seguido.objects.filter(idBd=seguido_id, seguidor=payload['idBd']).first()
        if seguido != None and seguido.seguidor.idBd == payload['idBd']:
            seguido.delete()
            return Response({'mensaje': 'Se ha dejado de seguir correctamente'}, status=204)
        else:
            return Response({'mensaje': 'No se ha podido dejar de seguir'}, status=401)
class SeguidoresView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        seguidores = Seguido.objects.filter(seguido=payload['idBd'])
        serializer = SeguidoSerializer(seguidores, many=True)
        return Response(serializer.data)
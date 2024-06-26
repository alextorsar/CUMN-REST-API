from rest_framework.views import APIView
from ..serializers import ValoracionSerializer
from ..models import Valoracion
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from ..controllers.socialController import getValoraciones
import jwt

class ValoracionView(APIView):
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
        serializer = ValoracionSerializer(data=data)
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
        valoraciones = getValoraciones(payload['idBd'])
        return Response(valoraciones)
    


class ValoracionPartidoView(APIView):
    def get(self, request, partido_id):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        valoraciones = Valoracion.objects.filter(partido=partido_id).all()
        serializer = ValoracionSerializer(valoraciones, many=True)
        return Response(serializer.data)
    
    def delete(self, request, partido_id):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        valoracion = Valoracion.objects.filter(partido=partido_id,usuario=payload['idBd']).first()
        if valoracion != None and valoracion.usuario.idBd == payload['idBd']:
            valoracion.delete()
            return Response({'mensaje': 'Valoracion eliminada correctamente'})
        else:
            return Response({'mensaje': 'No se pudo elimar la valoracion'}, status=400)
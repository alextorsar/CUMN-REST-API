from rest_framework.views import APIView
from ..serializers import VisualizacionSerializer
from ..models import Visualizacion
from ..controllers.socialController import getVisualizaciones
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt

class VisualizacionView(APIView):
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
        serializer = VisualizacionSerializer(data=data)
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
        visualizaciones = getVisualizaciones(payload['idBd'])
        return Response(visualizaciones)
    
    

class VisualizacionPartidoView(APIView):
    def get(self, request, partido_id):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        visualizaciones = Visualizacion.objects.filter(partido=partido_id).all()
        serializer = VisualizacionSerializer(visualizaciones, many=True)
        return Response(serializer.data)
    
    def delete(self, request, partido_id):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        visualizacion = Visualizacion.objects.filter(partido=partido_id, usuario=payload['idBd']).first()
        if visualizacion != None and visualizacion.usuario.idBd == payload['idBd']:
            visualizacion.delete()
            return Response({'mensaje': 'Visualizacion eliminada correctamente'})
        else:
            return Response({'mensaje': 'No se pudo elimar la visualizacion'}, status=400)
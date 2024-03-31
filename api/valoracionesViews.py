from rest_framework.views import APIView
from .serializers import ValoracionSerializer
from .models import Valoracion
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
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
        valoraciones = Valoracion.objects.filter(usuario=payload['idBd']).all()
        serializer = ValoracionSerializer(valoraciones, many=True)
        return Response(serializer.data)
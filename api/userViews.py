from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
import jwt, datetime


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        data = request.data
        correo = data.get('correo')
        contrasenia = data.get('contrasenia')
        user = User.objects.filter(correo=correo).first()
        if user is None:
            raise AuthenticationFailed('Usuario no encontrado')
        if not user.check_password(contrasenia):
            raise AuthenticationFailed('Contrasenia incorrecta')
        payload = {
            'idBd': user.idBd,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload,'ahhshfgfrsvsfsvb5657890gst45362gdf',algorithm='HS256')
        response = Response({'mensaje': 'Login correcto'})
        response.set_cookie(key='jwt', value=token, httponly=True)
        return response
    
class LogoutView(APIView):
    def post(self, request):
        response = Response({'mensaje': 'Logout correcto'})
        response.delete_cookie('jwt')
        return response
    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No autenticado')
        try:
            payload = jwt.decode(token, 'ahhshfgfrsvsfsvb5657890gst45362gdf', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesion expirada')
        user = User.objects.filter(idBd=payload['idBd']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
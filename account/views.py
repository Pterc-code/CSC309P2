from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.tokens import RefreshToken

from .models import Account
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['avatar', 'phone_number', 'email', 'password']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class RegisterView(APIView):
    def post(self, request):
        serializers = AccountSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.save()
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None).strip()

        if email is None:
            raise AuthenticationFailed('Email Invalid')

        account = Account.objects.filter(email=email).first()

        if account is None:
            raise AuthenticationFailed('Account is not found.')

        if password != account.password.strip():
            raise AuthenticationFailed('Incorrect password.')
        else:
            refresh = RefreshToken.for_user(account)
            response_data = {
                'status': 'success',
                'message': 'Logged in successfully',
                'data': {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                         }
                             }

            return Response(response_data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            'username': user.email,
            'password': user.password,
            'avatar': user.avatar,
            'phone_number': user.phone_number
        }
        return Response(data)
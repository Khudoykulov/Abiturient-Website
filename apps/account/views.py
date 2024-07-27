
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from .tasks import send_mail_func
from .models import User, UserToken
from rest_framework import generics, views, status, permissions, viewsets
from .tasks import crm_send_email

from apps.account.serializers import (
    # UserSerializer,
    UserRegistrationSerializer,
    CustomTokenObtainPairSerializer,
    SendEmailSerializer,
    ChangePasswordSerializer,
    UserVerifySerializer
)


class UserRegisterAPIView(generics.CreateAPIView):  #user registratsiya emailga kod yuboradi
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        email = request.data.get('email')
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = get_object_or_404(User, email=email)
        token = UserToken.objects.create(user=user)
        send_mail_func.apply_async(('Abiturient_Website', f'Your verification code is   'f'({str(token.token)}),'
                                                      f' thank you {str(user.username)}', [user.email]), )
        data = {
            'success': True,
            'message': 'Worker successfully registered.',
        }
        return Response(data, status=status.HTTP_201_CREATED)


class UserVerifyView(generics.GenericAPIView):
    serializer_class = UserVerifySerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        context = {
            'email': self.kwargs.get('email'),
            'request': request
        }
        serializer = self.serializer_class(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'success': True,
            'message': 'User successfully registered.',
        }
        return Response(data, status=status.HTTP_201_CREATED)


class LoginAPIView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class SendEmailAPIView(generics.GenericAPIView):
    serializer_class = SendEmailSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data.get('email')
        user = get_object_or_404(User, email=email)
        token = UserToken.objects.create(user=user)
        print(user.email)
        crm_send_email.apply_async(('Activation Token Code', user.username, [user.email]),)
        data = {
            'success': True,
            'detail': 'Yuborildi'
        }
        return Response(data, status=200)


class ChangePasswordAPIView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'success': True,
            'datail': 'Your password has been changed',
        }
        return Response(data=data, status=status.HTTP_200_OK)

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import generics, views, status, permissions, viewsets
from django.shortcuts import get_object_or_404
from apps.account.models import User, UserToken
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from datetime import datetime, timezone

class UserRegistrationSerializer(serializers.ModelSerializer):    #user registratsiya emailga kod yuboradi

    class Meta:
        model = User
        fields = ['email', 'username']


class UserVerifySerializer(serializers.Serializer):
    password1 = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, validators=[validate_password])
    token = serializers.IntegerField(write_only=True)

    class Meta:
        fields = ('token', 'password1', 'password2')

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        token = attrs.get('token')
        email = self.context.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if password1 == password2:
                if UserToken.objects.filter(user=user,).exists():
                    token_last = UserToken.objects.filter(user=user).last()
                    if token_last.token == token:
                        user.is_active = True
                        user.is_user_active = True
                        password = attrs.get('password1')
                        user.set_password(password)
                        user.verify_date = datetime.now()
                        UserToken.objects.get(token=token_last.token).is_used = True
                        user.save()
                    raise ValidationError('Token send')
                raise ValidationError('Token already exists')
            raise ValidationError('Passwords do not match')
        raise ValidationError('Email already registered')

    def create(self, validated_data):
        email = self.context.get('email')
        password = validated_data.pop('password1')
        user = get_object_or_404(User, email=email)
        user.set_password(password)
        user.save()
        print('dcsdc')
        print(user.password)
        print('cssscc')
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user,):
        token = super().get_token(user)
        token['email'] = user.email
        token['password'] = user.password
        token['created_date'] = user.created_date.strftime('%d/%m/%Y')
        return token


class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('Email does not exist')
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, validators=[validate_password])
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, validators=[validate_password])

    def validate(self, attrs):
        old_password = attrs.get('old_password')
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if self.context['request'].user.check_password(old_password):
            if old_password == password:
                raise ValidationError('Current password does not match!!!!!!!!')
            if password == password2:
                return attrs
            raise ValidationError('Passwords do not match!!!!!')
        raise ValidationError('old password is incorrect!!!!!!!!!!!!')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user

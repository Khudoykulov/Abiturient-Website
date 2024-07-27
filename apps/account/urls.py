from django.urls import path, include

from .views import (
    UserRegisterAPIView,
    LoginAPIView,
    SendEmailAPIView,
    ChangePasswordAPIView,
    UserVerifyView
)
app_name = 'account'


urlpatterns = [
    path('user/register/', UserRegisterAPIView.as_view(), name='register'),
    path('user/login/', LoginAPIView.as_view(), name='login'),
    path('user/send/', SendEmailAPIView.as_view(), name='send'),
    path('user/change-password/', ChangePasswordAPIView.as_view(), name='change-password'),
    path('user/verify_and_update_password/<str:email>/', UserVerifyView.as_view(), name='user-verify'),

]


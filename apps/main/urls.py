from django.urls import path
from .views import BalanceView
app_name = 'main'

urlpatterns = [
    path('balance', BalanceView.as_view())
]


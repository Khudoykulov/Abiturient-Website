from django.urls import path, include
from .views import BalanceView, MainTestAPIView
from rest_framework.routers import DefaultRouter
app_name = 'main'

router = DefaultRouter()
router.register('main_test', MainTestAPIView)

urlpatterns = [
    path('balance/', BalanceView.as_view()),
    # path('main_test/', MainTestAPIView.as_view()),
    path('', include(router.urls)),
]
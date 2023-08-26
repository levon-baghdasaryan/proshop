from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from ..views import auth_views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', auth_views.register, name='register'),
]

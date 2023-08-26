from django.urls import path

from ..views import product_views

app_name = 'products'
urlpatterns = [
    path('', product_views.index, name='index'),
    path('<str:id>/', product_views.show, name='show'),
]

from django.urls import path

from ..views import user_views

app_name = 'users'
urlpatterns = [
    path('', user_views.index, name='index'),
    path('profile/', user_views.profile, name='profile'),
    path('update/', user_views.update, name='update'),
]

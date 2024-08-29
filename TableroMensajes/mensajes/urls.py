from django.urls import path
from . import views

urlpatterns = [
    path('', views.mensajes_filtrados, {'filtro': 'ninguno'}, name='mensajes_filtrados'),
    path('<str:filtro>/', views.mensajes_filtrados, name='mensajes_filtrados'),
]
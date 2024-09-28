from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrar_consulta/', views.registrar_consulta, name='registrar_consulta'),  # Añade esta línea

]

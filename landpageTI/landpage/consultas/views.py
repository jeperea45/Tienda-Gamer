from django.shortcuts import render
from django.http import HttpResponse
from .models import Consulta
# Create your views here.

def home(request):
    return render(request, 'consulta.html')



def registrar_consulta(request):
    if request.method == 'POST':
        Nombre = request.POST['Nombre']
        Apellido = request.POST['Apellido']
        Tipo_De_Documento = request.POST['Tipo_De_Documento']
        Numero_De_Documento = request.POST['Numero_De_Documento']
        Celular= request.POST['Celular']
        Correo= request.POST['Correo']
        Servicio= request.POST['Servicio']

        consulta = Consulta(
            Nombre=Nombre,
            Apellido=Apellido,
            Tipo_De_Documento=Tipo_De_Documento,
            Numero_De_Documento=Numero_De_Documento,
            Celular=Celular,
            Correo=Correo,
            Servicio=Servicio,
        )
        consulta.save()
        return HttpResponse("Consulta registrada exitosamente.")
    return render(request, 'consulta.html')
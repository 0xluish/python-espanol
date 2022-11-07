from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar1
import datetime

# Create your views here.
def familiar1(request):
    
    familiar1 = Familiar1(nombre = 'Luis', apellido = 'Hernandez')
    # ,ID = 12345,fechaNacimiento = (1997,7,18),email = 'luishsolis@pm.me',presion = 'Estudiante')

    inicio = f'El primer familiar es {familiar1.nombre} {familiar1.apellido}'

    return HttpResponse(inicio)

    #return render(request,'',{'nombre': familiar1.nombre,'apellido': familiar1.apellido})
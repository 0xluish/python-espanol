from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar1, Familiar2, Familiar3
import datetime

# Create your views here.
def familiar1(request):
    
    familiar1 = Familiar1(nombre = 'Luis', apellido = 'Hernandez',ID = 12345,fechaNacimiento = (1997,7,18),email = 'luis@dominio.com',profesion = 'Crypto Vago')

    inicio = f'El primer familiar es {familiar1.nombre} {familiar1.apellido}.\nTiene un ID número {familiar1.ID}. Nació el {familiar1.fechaNacimiento}. Su profesión actual está marcada como "{familiar1.profesion}" y se puede contactar a través del correo: {familiar1.email}.'

    return HttpResponse(inicio)

def familiar2(request):
    
    familiar2 = Familiar2(nombre = 'Lionel', apellido = 'Messi',ID = 67890,fechaNacimiento = (1987,6,24),email = 'messi@psg.com',profesion = 'Futbolista')

    inicio2 = f'El primer familiar es {familiar2.nombre} {familiar2.apellido}.\nTiene un ID número {familiar2.ID}. Nació el {familiar2.fechaNacimiento}. Su profesión actual está marcada como "{familiar2.profesion}" y se puede contactar a través del correo: {familiar2.email}.'

    return HttpResponse(inicio2)

def familiar3(request):
    
    familiar3 = Familiar3(nombre = 'Cristiano', apellido = 'Ronaldo',ID = 777,fechaNacimiento = (1985,2,5),email = 'elbicho@cr7.com',profesion = 'Gritar SIIIIIUUUU')

    inicio3 = f'El primer familiar es {familiar3.nombre} {familiar3.apellido}.\nTiene un ID número {familiar3.ID}. Nació el {familiar3.fechaNacimiento}. Su profesión actual está marcada como "{familiar3.profesion}" y se puede contactar a través del correo: {familiar3.email}.'

    return HttpResponse(inicio3)
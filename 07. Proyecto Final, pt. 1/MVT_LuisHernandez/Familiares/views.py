from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar1, Familiar2, Familiar3
import datetime

# Create your views here.
def Familiar1(request):
    return render(request, 'Familiar1.html',{'nombre': 'Luis', 'apellido': 'Hernandez','ID': 12345,'fechaNacimiento': (1997,7,18),'email': 'luis@dominio.com','profesion': 'Crypto Vago', 'apodo': '0xluish'})

def Familiar2(request):
    return render(request, 'Familiar2.html',{'nombre': 'Lionel', 'apellido': 'Messi','ID': 67890,'fechaNacimiento': (1987,6,24),'email': 'messi@psg.com','profesion': 'Futbolista', 'apodo': 'La Pulga'})

def Familiar3(request):
    return render(request, 'Familiar3.html',{'nombre': 'Cristiano', 'apellido': 'Ronaldo','ID': 777,'fechaNacimiento': (1985,2,5),'email': 'elbicho@cr7.com','profesion': 'Gritar SIIIIIUUUU', 'apodo': 'Serresiete'})

# def familiares(request):
    
#     familiar1 = Familiar1(nombre = 'Luis', apellido = 'Hernandez',ID = 12345,fechaNacimiento = (1997,7,18),email = 'luis@dominio.com',profesion = 'Crypto Vago', apodo = 'Oxluish')

#     familiar2 = Familiar2(nombre = 'Lionel', apellido = 'Messi',ID = 67890,fechaNacimiento = (1987,6,24),email = 'messi@psg.com',profesion = 'Futbolista', apodo = 'La Pulga')

#     familiar3 = Familiar3(nombre = 'Cristiano', apellido = 'Ronaldo',ID = 777,fechaNacimiento = (1985,2,5),email = 'elbicho@cr7.com',profesion = 'Gritar SIIIIIUUUU', apodo = 'Serresiete')

#     inicio = f'La primera persona de la lista es {familiar1.nombre} {familiar1.apellido}, de sobre nombre "{familiar1.apodo}". Tiene un ID número {familiar1.ID}. Nació el {familiar1.fechaNacimiento}. Su profesión actual está marcada como "{familiar1.profesion}" y se puede contactar a través del correo: {familiar1.email}.'

#     inicio2 = f'La siguiente persona en la lista es {familiar2.nombre} {familiar2.apellido}, de sobre nombre "{familiar2.apodo}". Tiene un ID número {familiar2.ID}. Nació el {familiar2.fechaNacimiento}. Su profesión actual está marcada como "{familiar2.profesion}" y se puede contactar a través del correo: {familiar2.email}.'

#     inicio3 = f'La última persona de la lista es {familiar3.nombre} {familiar3.apellido}, de sobre nombre "{familiar3.apodo}". Tiene un ID número {familiar3.ID}. Nació el {familiar3.fechaNacimiento}. Su profesión actual está marcada como "{familiar3.profesion}" y se puede contactar a través del correo: {familiar3.email}.'

#     salida = (f'{inicio}{inicio2}{inicio3}')

#     return HttpResponse(salida)

# def familiar1(request):
    
#     familiar1 = Familiar1(nombre = 'Luis', apellido = 'Hernandez',ID = 12345,fechaNacimiento = (1997,7,18),email = 'luis@dominio.com',profesion = 'Crypto Vago', apodo = '0xluish')

#     inicio = f'La primera persona de la lista es {familiar1.nombre} {familiar1.apellido}, de sobre nombre "{familiar1.apodo}". Tiene un ID número {familiar1.ID}. Nació el {familiar1.fechaNacimiento}. Su profesión actual está marcada como "{familiar1.profesion}" y se puede contactar a través del correo: {familiar1.email}.'

#     return HttpResponse(inicio)

# def familiar2(request):
    
#     familiar2 = Familiar2(nombre = 'Lionel', apellido = 'Messi',ID = 67890,fechaNacimiento = (1987,6,24),email = 'messi@psg.com',profesion = 'Futbolista',apodo = 'La Pulga')

#     inicio2 = f'La siguiente persona en la lista es {familiar2.nombre} {familiar2.apellido}, de sobre nombre "{familiar2.apodo}". Tiene un ID número {familiar2.ID}. Nació el {familiar2.fechaNacimiento}. Su profesión actual está marcada como "{familiar2.profesion}" y se puede contactar a través del correo: {familiar2.email}.'

#     return HttpResponse(inicio2)

# def familiar3(request):
    
#     familiar3 = Familiar3(nombre = 'Cristiano', apellido = 'Ronaldo',ID = 777,fechaNacimiento = (1985,2,5),email = 'elbicho@cr7.com',profesion = 'Gritar SIIIIIUUUU', apodo = 'Serresiete')

#     inicio3 = f'La última persona de la lista es {familiar3.nombre} {familiar3.apellido}, de sobre nombre "{familiar3.apodo}". Tiene un ID número {familiar3.ID}. Nació el {familiar3.fechaNacimiento}. Su profesión actual está marcada como "{familiar3.profesion}" y se puede contactar a través del correo: {familiar3.email}.'

#     return HttpResponse(inicio3)
from django.shortcuts import render
from django.core import serializers as ssr
from django.http import HttpResponse
from platos.models import Platos
from django.shortcuts import redirect
# Create your views here.

def platos_list(request):
    data_context = Platos.objects.all()
    return render(request, 'platos_list.html', context ={'data': data_context})

def platos_peruanos(request):
    data_context = Platos.objects.filter(procedencia = 'Peru', precio__gt = 40)
    return render(request, 'platos_peruanos.html', context ={'data': data_context})
def platos_delete(request):
    p = Platos.objects.filter(precio__lt = 15)
    p.delete()
    return redirect('platos_list')
def platos_ssr(request):
    lista_platos= ssr.serialize('json', Platos.objects.filter(precio__gte=50), fields=['nombre', 'procedencia', 'precio'])
    return HttpResponse(lista_platos, content_type="application/json")
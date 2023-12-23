from django.shortcuts import render
from django.db.models import F
from meseros.models import Meseros
from django.shortcuts import redirect
# Create your views here.
def meseros_list(request):
    data_context = Meseros.objects.all()
    return render(request,  'meseros_list.html', context ={'data': data_context})
def meseros_peruanos(request):
    data_context = Meseros.objects.filter(nacionalidad='Peruana', edad__lt=30)
    return render(request,  'meseros_peruanos.html', context ={'data': data_context})
def meseros_update(request):
    Meseros.objects.update(edad=F('edad')+5)
    return redirect('meseros_list')
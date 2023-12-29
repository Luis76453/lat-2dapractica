from django.shortcuts import render
from django.core import serializers as ssr
from django.http import HttpResponse
from django.db.models import F
from meseros.models import Meseros
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from meseros.forms import MeserosForm
from django.urls import reverse_lazy
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from meseros.serializers import MeserosSerializer

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
def meseros_ssr(request):
    lista_meseros= ssr.serialize('json', Meseros.objects.filter(edad__gt=25), fields=['nombre', 'nacionalidad', 'edad'])
    return HttpResponse(lista_meseros, content_type="application/json")
class MeserosCreate(CreateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros_create.html'
    success_url = reverse_lazy('meseros_list')

class MeserosPeruList(ListView):
    model = Meseros
    template_name = 'meseros_proc_pe.html'

    def get_queryset(self):
        return Meseros.objects.filter(nacionalidad='Peruana')

class MeserosUpdateVC(UpdateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros_update_vc.html'
    success_url = reverse_lazy('meseros_list')

class MeserosDelete(DeleteView):
    model = Meseros
    template_name = "meseros_confirm_delete.html"
    success_url = reverse_lazy('meseros_list')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def meseros_create_api(request):

    if request.method == 'POST':
        print("Data OWNER: {}".format(request.data))
        serializers = MeserosSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT','GET','DELETE'])
@permission_classes([IsAuthenticated])
def meseros_details_view(request, pk):
    mesero = Meseros.objects.filter(id=pk).first()

    if mesero:
        if request.method == 'GET':
            serializers = MeserosSerializer(mesero)
            return Response(serializers.data)

        elif request.method == 'DELETE':
            print("Ingresó a Eliminar")
            mesero.delete()
            return Response("El mesero se ha eliminado ", status=status.HTTP_200_OK)


        elif request.method == "PUT":
            serializers = MeserosSerializer(mesero, data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


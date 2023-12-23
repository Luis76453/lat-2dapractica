from django.urls import path
from . import views
urlpatterns = [
    path('platos_list/', views.platos_list, name='platos_list'),
    path('platos_peruanos/', views.platos_peruanos, name= 'platos_peruanos'),
    path('platos_delete/', views.platos_delete, name= 'platos_delete')
    ]
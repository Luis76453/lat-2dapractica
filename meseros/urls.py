from django.urls import path
from . import views
urlpatterns = [
    path('meseros_list/', views.meseros_list, name='meseros_list'),
    path('meseros_peruanos/', views.meseros_peruanos, name='meseros_peruanos'),
    path('meseros_update/', views.meseros_update, name='meseros_update')
    ]
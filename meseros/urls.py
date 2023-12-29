from django.urls import path
from . import views
urlpatterns = [
    path('meseros_list/', views.meseros_list, name='meseros_list'),
    path('meseros_peruanos/', views.meseros_peruanos, name='meseros_peruanos'),
    path('meseros_update/', views.meseros_update, name='meseros_update'),

    path('meseros_ssr/', views.meseros_ssr, name='meseros_ssr'),

    path('meseros_create/', views.MeserosCreate.as_view(), name='meseros_create'),
    path('meseros_proc_pe/', views.MeserosPeruList.as_view(), name='meseros_proc_pe'),
    path('meseros_update_vc/<int:pk>', views.MeserosUpdateVC.as_view(), name='meseros_update_vc'),
    path('meseros_confirm_delete/<int:pk>', views.MeserosDelete.as_view(), name='meseros_delete'),

    path('meseros_create_api/', views.meseros_create_api, name="meseros_create_api"),
    path('meseros_detail_api/<int:pk>', views.meseros_details_view, name="meseros_detail_api")

    ]
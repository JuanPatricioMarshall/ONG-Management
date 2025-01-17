from django.urls import path

from . import views

urlpatterns = [
    path('cuentas/', views.CuentasLista.as_view(), name='ver_cuentas'),
    path('contactos/', views.ContactosPorNivel.as_view(), name='contactos'),
    path('cuentas/<int:pk>/', views.CuentasDetalles.as_view(), name='cuentas_detalles'),
    path('delete/<int:pk>', views.ContactoEliminar.as_view(), name='eliminar_contacto'),
    path('create/', views.ContactoCrear.as_view(), name='crear_contacto'),
    path('edit/<int:pk>', views.ContactoEditar.as_view(), name='editar_contacto'),
    path('dashboard/', views.DashBoard.as_view(),name='ver_dashboard'),
]
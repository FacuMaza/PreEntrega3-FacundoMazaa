from django.contrib import admin
from django.urls import path, include
from PreEntrega3.views import saludos, dia_hoy, probando_template, agregar_curso



urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludos/", saludos),
    path("dia_hoy/", dia_hoy),
    path("probando_template/", probando_template),
    path("agregar/", agregar_curso),
    path("aplicacion/", include("pre_entrega.urls"))

]

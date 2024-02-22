from django.urls import path
from pre_entrega import views



urlpatterns = [
    path("", views.inicio, name= "Inicio" ),
    path("cursos/", views.cursos,name= "Cursos"),
    path("profesores/", views.profesores,name= "Profesores"),
    path("alumnos/", views.alumnos,name= "Alumnos"),
    path("formulario/", views.formulario, name="Formulario"),
    path("formulario2/", views.formulario2, name="Formulario2"),
    path("buscar/", views.buscar, name="Buscar")
]
from django.shortcuts import render
from django.http import HttpResponse
from pre_entrega.models import Curso
from pre_entrega.forms import CursoFormulario, Buscar


def inicio (request):
    return render(request, "index.html")

def cursos (request):

    cursos= Curso.objects.all()

    return render(request, "cursos.html", {"cursos" : cursos})

def profesores (request):
    return render(request, "profesores.html")

def alumnos (request):
    return render(request, "alumnos.html")

def formulario(request):

    if request.method == "POST":

        curso = Curso(nombre=request.POST["curso"],camada=request.POST["camada"])

        curso.save()

        return render(request, "index.html")

    return render(request, "formulario.html")


def formulario2(request):
     if request.method == "POST":
         
         miFormulario = CursoFormulario(request.POST)

         if miFormulario.is_valid():
             
             informacion = miFormulario.cleaned_data

             curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])

             curso.save()

             return render(request, "index.html")
         else:
            miFormulario = CursoFormulario()

            return render(request, "cursoFormulario.html", {"formulario": miFormulario})


def buscar(request):

    if request.method == "POST":
        miFormulario = Buscar(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            curso = Curso.objects.filter(nombre__icontains=info["nombre"])
            render(request, "buscar.html", {"cursos": curso})
    else:
        miFormulario = Buscar()

    return render(request, "buscar.html", {"formulario": miFormulario})





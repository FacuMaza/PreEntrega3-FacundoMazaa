from django.http import HttpResponse
from datetime import datetime as dt

from django.template import Template, Context, loader
from pre_entrega.models import Curso

def probando_template(request):

    # mi_html = open("./plantillas/template1.html")
    # plantilla=Template(mi_html.read())
    # mi_html.close()
    # mi_contexcto =  Context(
    #     {"nombre": "Facundo",
    #      "notas" : [10,7,6,2]
    
    # })
    # documento = plantilla.render(mi_contexcto)

    diccionario = {
        "nombre": "Facundo",
         "notas" : [10,7,6,2]
    }
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render()

    return HttpResponse (documento)

def agregar_curso(request):
    
    return HttpResponse("Curso Guardado")




def saludos(request):
    return HttpResponse("Hola")

def dia_hoy(request):
    var = "Hoy es:<br>"
    var += str(dt.now())
    return HttpResponse(var)

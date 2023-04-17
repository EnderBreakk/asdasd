from django.http import HttpResponse
import datetime 
from django.template import Template, Context, loader
def saludo(request):
    return HttpResponse("Hola Josefo")
def segunda_vista(request):
    return HttpResponse("<br>segunda vista")

def tiempo(request):
    dia= datetime.datetime.now()
    texto= f"Hoy es: <br> {dia}"
    
    return HttpResponse(texto)

def nom(self, nombre):
    texto=f"bienvenido al sistema {nombre} <br> ¿En que podemos ayudarte?"
    return HttpResponse(texto)

def pT(self):
    nomb="jose"
    ap="grillo"
    diccionario={"nombre":nomb, "apellido":ap}
    # mihtml=open("C:/Users/Josefo/Desktop/CURSO CODERHOUSE/Django/proyecto_1/proyecto_1/plantillas/template1.html")
    # plantilla= Template(mihtml.read())
    # mihtml.close()
    # miContext=Context(diccionario)
    plantilla=loader.get_template("template1.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def pTiempo(request):
    dia= datetime.datetime.now()
    diccionario={"dia":dia}
    # mihtml=open("C:/Users/Josefo/Desktop/CURSO CODERHOUSE/Django/proyecto_1/proyecto_1/plantillas/template1.html")
    # plantilla= Template(mihtml.read())
    # mihtml.close()
    # miContext=Context(diccionario)
    plantilla=loader.get_template("template2.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)
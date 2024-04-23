from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hola(request):
    return HttpResponse("""
<h1> Hola Mundo!!!</h1>
<p> Esta es mi primera aplicacion con Django 
    mostrando HTML """)
from django.shortcuts import render

# Create your views here.

def mostrar_mascota(request):
    return render(request, 'mascotasApp/mostrar_mascota.html')

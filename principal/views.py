from django.shortcuts import render
from .models import dibujos

def pag_principal(request):
    return render(request, 'principal/pagina_principal.html')

def quien_soy(request):
    return render(request, 'principal/quien_soy.html')

def portafolio(request):

    mostrar_dibujos = dibujos.objects.all()

    return render(request, 'principal/portafolio.html', {"mostrar_dibujos":mostrar_dibujos})

def dibujo_id(request, id):

    dibujo = dibujos.objects.get(id = id)

    return render(request, 'principal/dibujo_id.html', {"dibujo":dibujo})
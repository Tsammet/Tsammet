from unittest import result
from django.shortcuts import redirect, render
from .models import dibujos
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import EmailMultiAlternatives, send_mail
from django.conf import settings
from django.template.loader import get_template


def pag_principal(request):
    return render(request, 'principal/pagina_principal.html')

def quien_soy(request):
    return render(request, 'principal/quien_soy.html')

def portafolio(request):

    mostrar_dibujos = dibujos.objects.all().order_by('-id')

    paginator = Paginator(mostrar_dibujos, 5)
    page =  request.GET.get('page')
    mostrar_dibujos = paginator.get_page(page)

    if request.method == "POST":
        busqueda = request.POST["buscar"]

   
        if busqueda:
            mostrar_dibujos = dibujos.objects.filter(
                Q(Nombre__icontains = busqueda) |
                Q(Anime__icontains = busqueda) |
                Q(contenido__icontains = busqueda)

            ).distinct()

    return render(request, 'principal/portafolio.html', {"mostrar_dibujos":mostrar_dibujos, 'busqueda_dibujo':mostrar_dibujos})

def dibujo_id(request, id):

    dibujo = dibujos.objects.get(id = id)
    dibujo_html = dibujos.objects.filter(id = id)

    return render(request, 'principal/dibujo_id.html', {"dibujo":dibujo, "dib": dibujo_html})

def contactanos(request):

    if request.method == "POST":
        rq_nombres = request.POST['nombres']
        rq_email = request.POST['email']
        rq_titulo = request.POST['titulo']
        rq_contenido = request.POST['contenido']

        # ENVIO DE MENSAJES A MI CORREO

        contenido_email_titulo=request.POST['email'] + " " + request.POST['titulo'] +  " " + request.POST['contenido']
 
        email_from= settings.EMAIL_HOST_USER

        send_mail(rq_nombres, contenido_email_titulo, email_from, ["tsammetsito@gmail.com"])

        # ENVIO DE MENSAJES A MI CORREO

      
        nombres = rq_nombres
        email = rq_email
        titulo = rq_titulo
        contenido = rq_contenido

        template = get_template('principal/envio_email_contactanos.html')

        content = template.render({'nombres':nombres ,"email":email, "titulo":titulo, "contenido":contenido})

        msg = EmailMultiAlternatives(
                'Empresa: TSAMMET',
                'estimado',
                
                settings.EMAIL_HOST_USER,
                [email]
            )

        msg.attach_alternative(content, 'text/html')
        msg.send()


    return render(request, 'principal/contactanos.html')


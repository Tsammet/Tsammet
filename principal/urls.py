from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('principal/', views.pag_principal, name='pag_principal'),
    path('quien_soy/', views.quien_soy, name='quien_soy'),
    path('portafolio/', views.portafolio, name='portafolio'),
    path('dibujo/<id>', views.dibujo_id, name='dibujo_id'),
    path('contactanos/', views.contactanos, name='contactanos'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


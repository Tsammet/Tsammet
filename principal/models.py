from distutils.command.upload import upload
from django.db import models

# Create your models here.



class dibujos(models.Model):

    Nombre = models.CharField(max_length=20)
    Anime = models.CharField(max_length=50)
    link_video = models.CharField(max_length=100, blank=True)
    contenido = models.CharField(max_length=50)
    dibujo = models.ImageField(upload_to ="dibujos")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Nombre



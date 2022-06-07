from django.contrib import admin
from .models import dibujos

# Register your models here.

class dibujosAdmin(admin.ModelAdmin):
    readonly_fields=("created", 'updated')

admin.site.register(dibujos, dibujosAdmin)
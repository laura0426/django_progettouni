from django.contrib import admin
from .models import Ricette, Preferiti, Categoria
# Register your models here.
admin.site.register(Ricette)
admin.site.register(Preferiti)
admin.site.register(Categoria)

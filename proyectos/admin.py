from django.contrib import admin
from .models import Proyecto, Autor, FotoAutor
# proyectos/admin.py
from .forms import ProyectoForm

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    # Opcional: search_fields para el Admin de Autor
    search_fields = ('nombre',)

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    form = ProyectoForm

admin.site.register(FotoAutor)

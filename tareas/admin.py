from django.contrib import admin
from .models import Tarea, Categoria, Prioridad

admin.site.register(Tarea)
admin.site.register(Categoria)
admin.site.register(Prioridad)
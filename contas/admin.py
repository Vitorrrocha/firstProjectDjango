from django.contrib import admin
from .models import Categoria
from .models import Trasacao

admin.site.register(Categoria)
admin.site.register(Trasacao)
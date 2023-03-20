from django.contrib import admin

from .models import Categoria

admin.site.register(Categoria)

def __str__(self):
        return self.descricao
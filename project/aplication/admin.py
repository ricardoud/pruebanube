from django.contrib import admin

from .models import clientes, contenedores, lavadora, prendas, secadora

# Register your models here.
admin.site.register(clientes)
admin.site.register(prendas)
admin.site.register(contenedores)
admin.site.register(lavadora)
admin.site.register(secadora)

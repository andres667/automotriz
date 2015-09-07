from django.contrib import admin
from automotriz.apps.ventas.models import Ventas, Vendedor, Automovil, Cliente

admin.site.register(Ventas)
admin.site.register(Vendedor)
admin.site.register(Automovil) 
admin.site.register(Cliente)
 
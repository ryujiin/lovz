from django.contrib import admin
from models import *

class EnlaceCliente(admin.ModelAdmin):
	list_display= ('nombre','direccion','ruc')


admin.site.register(Cliente , EnlaceCliente)
admin.site.register(Cuenta_Cliente)
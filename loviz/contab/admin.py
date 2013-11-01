from django.contrib import admin
from models import *

class EnlaceCliente(admin.ModelAdmin):
	list_display= ('nombre','direccion','ruc')

class CuentaCliente(admin.ModelAdmin):
	list_display=('cliente','deuda','abono','total','fecha')

class Materiales_lista(admin.ModelAdmin):
	list_display=('nombre','precio',)	

admin.site.register(Cliente , EnlaceCliente)
admin.site.register(Cuenta_Cliente, CuentaCliente)
admin.site.register(Modelos_calzado)
admin.site.register(Material,Materiales_lista)
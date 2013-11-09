from django.contrib import admin
from models import Material,Firme,StockMaterial,StockFirme,Compras_Material
from forms import * 
import datetime

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'precio','unidad_compra')
    
    def save_model(self, request, obj, form, change):
    	nombre = form.cleaned_data['nombre']
    	obj.save()
    	id_material=Material.objects.get(nombre=nombre)
    	now=datetime.datetime.now()
    	stock=StockMaterial(nombre=id_material, cantidad=0,total_unidades=0, timestamp=now, total_soles=0,registro="Agregado")
    	stock.save()

class StockMateAdmin(admin.ModelAdmin):
	list_display=('nombre','timestamp','total_soles','cantidad','total_unidades','registro')
	list_filter=('nombre','timestamp')

	def get_ordering(self, request):
		return ['-timestamp',]

class ComprasAdmin(admin.ModelAdmin):
	list_display=('compra_materiales','fecha','cantidad')

	def save_model(self, request, obj, form, change):
		nombre = form.cleaned_data['compra_materiales']
		cantidad1= form.cleaned_data['cantidad']
		material=Material.objects.get(nombre=nombre)
		materia_stock = StockMaterial.objects.filter(nombre=material).order_by('-timestamp')[0]
		total=cantidad1+materia_stock.cantidad
		now=datetime.datetime.now()
		stock=StockMaterial(nombre=material, cantidad=cantidad1,total_unidades=total, timestamp=now, total_soles=0,registro="Compra")
		obj.save()
		stock.save()
		
admin.site.register(Material, MaterialAdmin)
admin.site.register(StockMaterial,StockMateAdmin)
admin.site.register(Compras_Material,ComprasAdmin)
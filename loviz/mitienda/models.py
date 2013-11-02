from shop.models import Product
from django.db import models

# Create your models here.

class Calzado(Product):
	sku = models.CharField(max_length = 140)
	categorias = models.ForeignKey('Categoria',blank=True, null=True,on_delete=models.SET_NULL)
	estilo = models.ForeignKey('EstiloCalzado',blank=True, null=True,on_delete=models.SET_NULL)
	descripcion = models.TextField()
	descuento =models.IntegerField (default = 0)
	palabras_claves = models.ManyToManyField('PalabrasClaves', blank=True)
	cantidad =models.IntegerField(default=0)
	relacion_color = models.ManyToManyField('self')
	talla= models.ForeignKey('Varacion')

	class Meta:
		pass

class Varacion(models.Model):
	nombre = models.CharField(max_length=140)

	def __unicode__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length=140)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.nombre

class PalabrasClaves(models.Model):
	nombre = models.CharField(max_length=140)
	
	def __unicode__(self):
		return self.nombre

class EstiloCalzado(models.Model):
	nombre = models.CharField(max_length=140)
	descripcion = models.TextField()
	categoria =models.ForeignKey(Categoria,blank=True, null=True,on_delete=models.SET_NULL)

	def __unicode__(self):
		return self.nombre
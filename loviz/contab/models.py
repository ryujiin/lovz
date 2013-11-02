from django.db import models

# Create your models here.
class Cliente(models.Model):
	nombre = models.CharField(max_length = 100)
	direccion = models.CharField(max_length = 140)
	ruc = models.CharField(max_length = 11)

	def __str__(self):
		return self.nombre

class Cuenta_Cliente(models.Model):
	cliente = models.ForeignKey(Cliente)
	deuda = models.IntegerField(default = 0)
	abono = models.IntegerField(default = 0)
	total = models.IntegerField(default=0)
	fecha = models.DateTimeField(auto_now_add=True)

class Material(models.Model):
	UNIDADES_DE_MEDIDA = (
		('M','Metros'),
		('P','Pies'),
		('U','Unidad')
		)
	nombre = models.CharField(max_length = 140)
	cantidad = models.IntegerField(default = 0)
	unidad = models.CharField(max_length=1, choices=UNIDADES_DE_MEDIDA)
	precio = models.IntegerField(default = 0)
	total_soles = models.IntegerField(default=0)

	def __str__(self):
		return self.nombre

class Modelos_calzado(models.Model):
	nombre = models.CharField(max_length=140)
	materiales = models.ForeignKey(Material)
	costo = models.IntegerField(default=0)
	
	def __str__(self):
		return self.nombre

class Venta(models.Model):
	UNI_CANT_VENT=(
		('D','Docena'),
		('P','Par'),
		)
	cliente=models.ForeignKey(Cliente)
	modelo=models.ForeignKey(Modelos_calzado)
	cantidad=models.IntegerField(default=0)
	unidada_venta=models.CharField(max_length=1,choices=UNI_CANT_VENT)
	precio_unidad=models.IntegerField(default=0)
	fecha=models.DateField(auto_now_add=False)

	def __unicode__(self):
		return "%s - %s" % (self.cliente,self.modelo)

	def mis_precios_en_soles(self):
		return 'S/.%s' % self.precio_unidad

	def total_venta(self):
		totales_venta = self.cantidad * self.precio_unidad
		return 'S/.%s' % totales_venta 




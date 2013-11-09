from django.db import models
# Create your models here.

#lista de materiales para manejar Stock
class Material(models.Model):
	TIPO=(('tela','Tela'),('cinta','Cinta'),)
	UNID=(('metros','Metros'),('millar','millar'),('paquetes','Paquetes'))

	nombre = models.CharField(max_length = 140)
	unidad_compra = models.CharField(max_length=20,choices=UNID)
	tipo = models.CharField(max_length=20,choices=TIPO)
	precio = models.DecimalField(max_digits=5, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.nombre
	class Meta:
		unique_together = (("nombre",),)
	

#lista de Firmes Stock
class Firme(models.Model):
	COLOR=(('fucsia','Fucsia'),('azul','Azul'),('negro','Negro'),('lila','Lila'),('celeste','Celeste'),('beige','Beige'),)
	TALLA=(('28','28'),('30','30'),('32','32'),('34','34'),('36','36'),('38','38'),('40','40'),)

	color=models.CharField(max_length=20,choices=COLOR)
	talla= models.CharField(max_length=2,choices=TALLA)

	def __unicode__(self):
		return "%s - %s" % (self.color,self.talla)	

class StockMaterial(models.Model):
	nombre = models.ForeignKey(Material)
	cantidad = models.IntegerField(default=0)
	total_unidades = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True)
	total_soles = models.DecimalField(max_digits=6, decimal_places=2)
	registro = models.CharField(max_length=30)

	def __unicode__(self):
		return "%s - %s" % (self.nombre,self.cantidad) 

class StockFirme(models.Model):
	nombre = models.ForeignKey(Firme)
	cantidad = models.IntegerField(default=0)
	total_unidades = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True)
	total_soles = models.DecimalField(max_digits=6, decimal_places=2)
	registro = models.CharField(max_length=30)

class Compras_Material(models.Model):
	fecha=models.DateTimeField(auto_now_add=True)
	compra_materiales = models.ForeignKey(Material)
	cantidad= models.IntegerField(default=0)

class PedidoFirmes(models.Model):
	fecha=models.DateTimeField(auto_now_add=True)
	compra_materiales = models.ForeignKey(Firme)
	cantidad= models.IntegerField(default=0)

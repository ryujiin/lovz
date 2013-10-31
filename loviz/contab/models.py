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
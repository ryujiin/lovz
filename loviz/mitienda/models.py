from django.db import models

# Create your models here.s Producto(Product):
class Calzado(Product):
	padre= models.ForeignKey("self",blank=True,null=True)

	class Meta:
		pass

class TallasCalzado(models.Model):
	nombre=models.CharField(max_length=140)

class Categoria(models.Model):
	nombre=models.CharField(max_length=140)
	peso=models.IntegerField(default = 0)
	padre = models.ForeignKey("self",blank=True,null=True)
from shop.models import Product
from django.db import models

# Create your models here.
class Pantufla(Product):
	isbn=models.CharField(max_length=255)
	color =models.CharField(max_length = 255)

	class Meta:
		pass

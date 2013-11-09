from models import *

from django.test import TestCase

from django.contrib import admin
from forms import * 


class SimpleTest(TestCase):
    def salvar_objetos(self):
    	datos= StockMaterial.objects.get(nombre='plush')
	
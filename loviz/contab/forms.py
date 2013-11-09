from django import forms
from django.forms import ModelForm
from models import *
from django.contrib.admin import widgets

class MaterialForm(ModelForm):
	class Meta:
		model=Material
		exclude = ("tipo",)

class StockMaterialForm(ModelForm):
	class Meta:
		model=StockMaterial
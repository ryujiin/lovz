from django import forms
from django.forms import ModelForm
from models import *

class ProductoForm(ModelForm):

    class Meta:
        model = Calzado
        

from django.shortcuts import render_to_response,get_object_or_404, render
from django.template.context import RequestContext
from models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required,permission_required
from forms import MaterialForm

@login_required(login_url='/usuario/ingresar/')
def inicio_admin(request):
	t='admin/base_admin.html'
	return render(request,t,{"request":request,})

@login_required
def add_material(request):
	if request.POST:
		form_materiales = MaterialForm(request.POST)
		form_stockmateriales = StockMaterialForm(request.POST)
		if form_materiales.is_valid():
			nombre = form.cleaned_data['nombre']
			return HttpResponseRedirect("/")
	else:
		form_materiales = MaterialForm()
	return form_materiales
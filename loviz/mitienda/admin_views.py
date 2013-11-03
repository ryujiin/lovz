from django.shortcuts import render_to_response,get_object_or_404, render
from django.template.context import RequestContext
from models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required,permission_required
from forms import *


def admintienda(request):
    categorias = Categoria.objects.all()
    template = "admin/adminindex.html"
    return render(request, template,{"categorias" : categorias, "request":request})

def add_producto(request):
    if request.POST:
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            return HttpResponseRedirect("/")
    else:
        form = ProductoForm()
    template = "admin/forms/form_producto.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

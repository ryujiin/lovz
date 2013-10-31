# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from django.template.context import RequestContext

def home(request):
    mensaje = "Hola chicos"
    template = "index.html"
    return render_to_response(template,{"mensaje" : mensaje,"request":request,})

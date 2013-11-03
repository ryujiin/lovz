from django.shortcuts import render_to_response,get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf


def inicio(request):
	t= "base_tienda.html"
	return render(request, t,{"request":request,})

#Sistema de login en la pagina Usuarios
def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/usuario/perfil/')
	else:
		c={}
		c.update(csrf(request))
		return render_to_response('formus/login.html',c)

def auth_view(request):
	if request.method == "POST":
		username = request.POST['username']
		p = request.POST['password']

		user = auth.authenticate(username=username, password=p)
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/usuario/perfil/')
		else:
			return HttpResponseRedirect('/usuario/invalido/')
	else:
		return HttpResponseRedirect('/usuario/invalido/')

def perfil(request):
	t= 'perfil.html'
	return render_to_response(t,{'full_name':request.user.username})

def invalido(request):
	t='user_invalido.html'
	return render_to_response(t)

def logout(request):
	auth.logout(request)
	t='base_tienda.html'
	return render_to_response(t)
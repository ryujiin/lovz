from random import choice

frases = ['Freddy cabeza', 'arturo flaco', 'julian gordo']

def ejemplo(request):

    return {'frase': choice(frases)}

from django.core.urlresolvers import reverse

#procesadores de Administrador
def menu_admin(request):
    menu_admin1 = {'menu_admin': [
        {'name': 'Inicio', 'url': reverse('inicio contab')},
        {'name': 'Clientes', 'url': reverse('Clientes'),
        	'sub_menu':[
        		{'name_submenu':'Agregar cliente','url': reverse('Agregar cliente')
        	}]
        },
        {'name': 'Materiales', 'url': reverse('Materiales'),
            'sub_menu':[
                {'name_submenu':'Agregar Material','url': reverse('Agregar Material')
            }]
        },
    ]}
    for item in menu_admin1['menu_admin']:
        if request.path == item['url']:
            item['active'] = True
    return menu_admin1

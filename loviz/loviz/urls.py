from django.conf.urls import patterns, include, url
from shop import urls as shop_urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'contab.views.home', name='home'),
    url(r'^admin/tienda/$', 'mitienda.admin_views.admintienda', name='Administrador'),
    url(r'^admin/tienda/producto/add$', 'mitienda.admin_views.add_producto', name='Agregar Producto'),
    (r'^tienda/', include(shop_urls)),
    # url(r'^loviz/', include('loviz.foo.urls')),

    url(r'^usuario/ingresar/$', 'mitienda.views.login'),
    url(r'^usuario/auth/$', 'mitienda.views.auth_view'),
    url(r'^usuario/logout/$', 'mitienda.views.logout'),
    url(r'^usuario/perfil/$', 'mitienda.views.perfil'),
    url(r'^usuario/invalido/$', 'mitienda.views.invalido'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

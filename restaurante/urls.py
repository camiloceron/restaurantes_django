from django.conf.urls import patterns, include, url
from restaurante.views import InicioView


urlpatterns = patterns('',

    url(r'^$', InicioView.as_view(), name='inicio'),    
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^salir/$', 'restaurante.views.logOut'), 
    url(r'^login/$', 'restaurante.views.logIn'), 

    url(r'^clientes/$', 'restaurante.views.lista_clientes'),
    url(r'^clientes/add/$', 'restaurante.views.agregar_cliente'),
    url(r'^clientes/delete/(?P<id>\d+)$', 'restaurante.views.borrar_cliente'),
    url(r'^clientes/edit/(?P<id>\d+)$', 'restaurante.views.editar_cliente'),

    url(r'^platos/$', 'restaurante.views.lista_platos'),
    url(r'^platos/add/$', 'restaurante.views.agregar_plato'),
    url(r'^platos/delete/(?P<id>\d+)$', 'restaurante.views.borrar_plato'),
    url(r'^platos/edit/(?P<id>\d+)$', 'restaurante.views.editar_plato'),
    url(r'^platos/catalogo$', 'restaurante.views.catalogo'),
)

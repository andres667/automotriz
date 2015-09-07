from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('automotriz.apps.home.views',

		url(r'^$', 'index_view', name = 'vista_index'),
		url(r'^ventas/(?P<id_ven>.*)/$', 'single_vent_view', name = 'vista_single_ventas'),
		url(r'^vendedor/(?P<id_vend>.*)/$', 'single_vended_view', name = 'vista_single_vendedor'),
		url(r'^automovil/(?P<id_aut>.*)/$', 'single_autom_view', name = 'vista_single_automovil'),
		url(r'^cliente/(?P<id_cli>.*)/$', 'single_clien_view', name = 'vista_single_cliente'),
		url(r'^ventas/$', 'ventas_view', name = 'vista_ventas'),
		url(r'^vendedores/$', 'vendedor_view', name = 'vista_vendedor'),
		url(r'^automoviles/$', 'automovil_view', name = 'vista_automovil'),
		url(r'^clientes/$', 'cliente_view', name = 'vista_cliente'),
		url(r'^busqueda/$','busqueda_view', name = 'vista_busqueda'),





)
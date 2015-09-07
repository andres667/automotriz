from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('automotriz.apps.ventas.views',
		url(r'^add/ventas/$','add_ventas_view',name = 'vista_agregar_ventas'),
		url(r'^add/vendedor/$','add_vendedor_view',name = 'vista_agregar_vendedor'),
		url(r'^add/automovil/$','add_automovil_view',name = 'vista_agregar_automovil'),
		url(r'^add/cliente/$','add_cliente_view',name = 'vista_agregar_cliente'),
		url(r'^edit/ventas/(?P<id_ven>.*)/$', 'edit_vent_view', name = 'vista_editar_ventas'),
		url(r'^edit/vendedor/(?P<id_vend>.*)/$', 'edit_vended_view', name = 'vista_editar_vendedor'),
		url(r'^edit/automovil/(?P<id_aut>.*)/$', 'edit_autom_view', name = 'vista_editar_automovil'),
		url(r'^edit/cliente/(?P<id_cli>.*)/$', 'edit_clien_view', name = 'vista_editar_cliente'),
		url(r'^del/ventas/(?P<id_ven>.*)/$', 'del_vent_view', name = 'vista_eliminar_ventas'),
		url(r'^del/vendedor/(?P<id_vend>.*)/$', 'del_vended_view', name = 'vista_eliminar_vendedor'),
		url(r'^del/automovil/(?P<id_aut>.*)/$', 'del_autom_view', name = 'vista_eliminar_automovil'),
		url(r'^del/cliente/(?P<id_cli>.*)/$', 'del_clien_view', name = 'vista_eliminar_cliente'),



)
  
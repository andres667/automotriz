# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from automotriz.apps.ventas.forms import *
from automotriz.apps.ventas.models import *
from django.http import HttpResponseRedirect


def add_ventas_view(request):
	info = "Inicializando"
	if request.method == "POST":
		formulario = add_ventas_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/ventas/%s'%add.id)
	else:
		formulario = add_ventas_form()
	ctx =  {'form':formulario, 'informacion':info}
	return render_to_response('ventas/add_ventas.html', ctx,context_instance = RequestContext(request))
	
	
def add_vendedor_view(request):
	info = "Inicializando"
	if request.method == "POST":
		formulario = add_vendedor_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/vendedor/%s'%add.id)
	else:
		formulario = add_vendedor_form()
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('ventas/add_vendedor.html', ctx,context_instance = RequestContext(request))
	
def add_automovil_view(request):
	info = "Inicializando"
	if request.method == "POST":
		formulario = add_automovil_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect  ('/automovil/%s' %add.id)
	else:
		
		formulario = add_automovil_form()
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('ventas/add_automovil.html', ctx,context_instance = RequestContext(request))

def add_cliente_view(request):
	info = "Inicializando"
	if request.method == "POST":
		formulario = add_cliente_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/cliente/%s' %add.id)
	else:
		formulario = add_cliente_form()
	ctx =  {'form':formulario, 'informacion':info}
	return render_to_response('ventas/add_cliente.html', ctx,context_instance = RequestContext(request))


def edit_vent_view(request, id_ven):
	info = ""
	ven = Ventas.objects.get(pk = id_ven)
	if request.method == "POST":
		formulario = add_ventas_form(request.POST, request.FILES, instance = ven)
		if formulario.is_valid():
			edit_ven = formulario.save(commit = False)
			edit_ven.status = True
			edit_ven.save()
			info = "Guardado Satisfatoriamente"
			return HttpResponseRedirect('/ventas/%s'% edit_ven.id)
	else:
		formulario = add_ventas_form(instance = ven)
	ctx = {'form':formulario, 'informacion':info}	
	return render_to_response('ventas/edit_ventas.html', ctx,context_instance = RequestContext(request))
			
def edit_vended_view(request, id_vend):
	info = ""
	vend = Vendedor.objects.get(pk = id_vend)
	if request.method == "POST":
		formulario = add_vendedor_form(request.POST, request.FILES, instance = vend)
		if formulario.is_valid():
			edit_vend = formulario.save(commit = False)
			edit_vend.status = True
			edit_vend.save()
			info = "Guardado Satisfatoriamente"
			return HttpResponseRedirect('/vendedor/%s'% edit_vend.id)
	else:
		formulario = add_vendedor_form(instance = vend)
	ctx = {'form':formulario, 'informacion':info}	
	return render_to_response('ventas/edit_vendedor.html', ctx,context_instance = RequestContext(request))

def edit_autom_view(request, id_aut):
	info = ""
	aut = Automovil.objects.get(pk = id_aut)
	if request.method == "POST":
		formulario = add_automovil_form(request.POST, request.FILES, instance = aut)
		if formulario.is_valid():
			edit_aut = formulario.save(commit = False)
			edit_aut.status = True
			edit_aut.save()
			info = "Guardado Satisfatoriamente"
			return HttpResponseRedirect('/automovil/%s'% edit_aut.id)
	else:
		formulario = add_automovil_form(instance = aut)
	ctx = {'form':formulario, 'informacion':info}	
	return render_to_response('ventas/edit_automovil.html', ctx,context_instance = RequestContext(request))

def edit_clien_view(request, id_cli):
	info = ""
	cli = Cliente.objects.get(pk = id_cli)
	if request.method == "POST":
		formulario = add_cliente_form(request.POST, request.FILES, instance = cli)
		if formulario.is_valid():
			edit_cli = formulario.save(commit = False)
			edit_cli.status = True
			edit_cli.save()
			info = "Guardado Satisfatoriamente"
			return HttpResponseRedirect('/cliente/%s'% edit_cli.id)
	else:
		formulario = add_cliente_form(instance = cli)
	ctx = {'form':formulario, 'informacion':info}	
	return render_to_response('ventas/edit_cliente.html', ctx,context_instance = RequestContext(request))


def del_vent_view(request, id_ven):
	info = "Inicializando"
	try:
		ven = Ventas.objects.get(pk = id_ven)
		ven.delete()
		info = "Venta Eliminado Correctamente"
		return HttpResponseRedirect('/ventas/')
	except:
		info = "Venta no se puede Eliminar"	
		#return render_to_response('home/ventas.html', context_instance = RequestContext(request))
		return HttpResponseRedirect('/ventas/')

def del_vended_view(request, id_vend):
	info = "Inicializando"
	try:
		vend = Vendedor.objects.get(pk = id_vend)
		vend.delete()
		info = "vendedor Eliminado Correctamente"
		return HttpResponseRedirect('/vendedores/')
	except:
		info = "Vendedor no se puede Eliminar"	
		#return render_to_response('home/ventas.html', context_instance = RequestContext(request))
		return HttpResponseRedirect('/vendedores/')

def del_autom_view(request, id_aut):
	info = "Inicializando"
	try:
		aut = Automovil.objects.get(pk = id_aut)
		aut.delete()
		info = "automovil Eliminado Correctamente"
		return HttpResponseRedirect('/automoviles/')
	except:
		info = "automovil no se puede Eliminar"	
		#return render_to_response('home/ventas.html', context_instance = RequestContext(request))
		return HttpResponseRedirect('/automoviles/')

def del_clien_view(request, id_cli):
	info = "Inicializando"
	try:
		cli = Cliente.objects.get(pk = id_cli)
		cli.delete()
		info = "cliente Eliminado Correctamente"
		return HttpResponseRedirect('/clientes')
	except:
		info = "cliente no se puede Eliminar"	
		#return render_to_response('home/ventas.html', context_instance = RequestContext(request))
		return HttpResponseRedirect('/clientes/')



			
		



# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from automotriz.apps.ventas.forms import *
from automotriz.apps.home.forms import *
from automotriz.apps.ventas.models import *
from django.http import HttpResponseRedirect

def index_view(request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))


def single_vent_view(request, id_ven):
	ven = Ventas.objects.get(id = id_ven)
	ctx = {'ventas':ven}
	return render_to_response('home/single_ventas.html',ctx,context_instance = RequestContext(request))	

def single_vended_view(request, id_vend):
	vend = Vendedor.objects.get(id = id_vend)
	ctx = {'vendedor':vend}
	return render_to_response('home/single_vendedor.html',ctx,context_instance = RequestContext(request))	

def single_autom_view(request, id_aut):
	aut = Automovil.objects.get(id = id_aut)
	ctx = {'automovil':aut}
	return render_to_response('home/single_automovil.html',ctx,context_instance = RequestContext(request))	

def single_clien_view(request, id_cli):
	cli = Cliente.objects.get(id = id_cli)
	ctx = {'cliente':cli}
	return render_to_response('home/single_cliente.html',ctx,context_instance = RequestContext(request))	


def ventas_view(request):
	lista_ven = Ventas.objects.all()
	ctx = {'ventas':lista_ven}
	return render_to_response ('home/ventas.html', ctx, context_instance = RequestContext(request))	
	
def vendedor_view(request):
	lista_vend = Vendedor.objects.filter(status = True)
	ctx = {'vendedor':lista_vend}
	return render_to_response ('home/vendedor.html', ctx, context_instance = RequestContext(request))	
	
def automovil_view(request):
	lista_aut = Automovil.objects.filter(status = True)
	ctx = {'automovil':lista_aut}
	return render_to_response ('home/automovil.html', ctx, context_instance = RequestContext(request))

def cliente_view(request):
	lista_cli = Cliente.objects.all()
	ctx = {'cliente':lista_cli}
	return render_to_response ('home/cliente.html', ctx, context_instance = RequestContext(request))	

	

def busqueda_view(request): 
	if request.method == 'POST':
		formulario = busqueda_form(request.POST)
		if formulario.is_valid():
			b = formulario.cleaned_data['busqueda']
			ventas = Ventas.objects.filter(cliente__cedula = b)
			cliente = Automovil.objects.filter(cedula = b)
			autos = Automovil.objects.all()
			ctx = {'form': formulario, 'client':cliente,'venta': ventas, 'auto':autos}
			return render_to_response('home/busqueda.html',ctx, context_instance = RequestContext(request))
	else:
		formulario = busqueda_form()
	ctx = {'form': formulario}
	return render_to_response('home/busqueda.html',ctx , context_instance=RequestContext(request))
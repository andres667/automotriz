from automotriz.apps.ventas.models import Ventas,Vendedor,Automovil,Cliente
from django import forms 

class add_ventas_form(forms.ModelForm):
	class Meta:
		model = Ventas


class add_vendedor_form(forms.ModelForm):
	class Meta:
		model = Vendedor
		exclude	= {'status',}


class add_automovil_form(forms.ModelForm):
	class Meta:
		model = Automovil
		exclude= {'status',}

class add_cliente_form(forms.ModelForm):
	class Meta:
		model = Cliente		

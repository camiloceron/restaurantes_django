from django import forms
from restaurante.models import Cliente
from restaurante.models import Plato

class ClienteForm(forms.ModelForm):
	class Meta:		
		model = Cliente
		exclude = ["id"]

class PlatoForm(forms.ModelForm):
	class Meta:		
		model = Plato
		exclude = ["id"]
from ..models import Cidades
from django import forms

class CidadesForm(forms.ModelForm):
		class Meta:
				model = Cidades
				# fields = ['nome_cidade','uf']
				fields = '__all__'
from ..models import Cidades
from django import forms
from localflavor.br.br_states import STATE_CHOICES

class CidadesForm(forms.ModelForm):
		class Meta:
				model = Cidades
				# fields = '__all__'
				fields = ['nome_cidade','uf']
				

class RawCidadesForm(forms.Form):
		nome_cidade = forms.CharField(label='dsrrsdrsd',
																	widget=forms.TextInput(attrs={'class':'form-control',
																																'placeholder':'Digite o Nome da Cidade'
																																}))
		uf = forms.ChoiceField(label='',
													 widget=forms.Select, choices=STATE_CHOICES)
	

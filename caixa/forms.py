from .models import EntradaSaida
from django import forms


class EntradaSaidaForm(forms.ModelForm):
		class Meta:
				model = EntradaSaida
				fields = '__all__'

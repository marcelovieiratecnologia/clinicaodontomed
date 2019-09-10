from django import forms
from .models import Profissionais


class ProfissionaisForm(forms.ModelForm):
		class Meta:
				model = Profissionais
				fields = '__all__'
from django import forms
from ..models import Especialidades


class EspecialidadesForm(forms.ModelForm):
		class Meta:
				model = Especialidades
				fields = ['especialidade']
				# fields = '__all__'




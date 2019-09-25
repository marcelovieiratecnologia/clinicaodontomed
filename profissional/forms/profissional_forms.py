from django import forms
from ..models import Profissionais, Especialidades


class ProfissionaisForm(forms.ModelForm):
		especialidades = forms.ModelMultipleChoiceField(queryset=Especialidades.objects.all())
		
		class Meta:
				model = Profissionais
				#fields = '__all__'
				fields = ['nome_profissional','cpf_profissional','num_registro_classe','cidades','orgao_emissor','especialidades']
				

from django import forms

from .models import EntradaSaida

from profissional.models import Profissionais


class EntradaSaidaForm(forms.ModelForm):
		# profissionais = forms.ModelChoiceField(queryset=Profissionais.objects.all())
		class Meta:
				model = EntradaSaida
				#fields = '__all__'
				fields = ['dt_movimentacao','profissional','paciente','qt_parcelas','valor_entr_saida','tp_entrada',
									'tp_convenio','tp_pagamento','tp_credito','tp_porcentagem','observacao','motivo',
									'fkprofissional','fkespecialidades']
				

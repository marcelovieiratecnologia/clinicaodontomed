from django import forms

from .models import EntradaSaida

from profissional.models import Profissionais

TP_ENTRADA = [
		('ENTRADA', u'Entrada'),
		('SAIDA', u'Saida'),
]
TP_CONVENIO = [
		('INTERODONTO', u'InterOdonto'),
		('ODONTOPREV', u'OdontoPrev'),
		('BRADESCO', u'Bradesco'),
		('PARTICULAR', u'Particular'),
]
TP_PAGAMENTO = [
		('CREDITO', u'Credito'),
		('DEBITO', u'Debito'),
		('DINHEIRO', u'Dinheiro'),
]
TP_CREDITO = [
		('APRAZO', u'A Prazo'),
]
TP_PORCENTAGEM = [
		('0.00', u'0.00%'),
		('2.68', u'2.68%'),
		('7.07', u'7.07%'),
		('8.51', u'8.51%'),
]


class EntradaSaidaForm(forms.ModelForm):
		# profissionais = forms.ModelChoiceField(queryset=Profissionais.objects.all())
		class Meta:
				model = EntradaSaida
				#fields = '__all__'
				fields = ['dt_movimentacao','profissional','paciente','qt_parcelas','valor_entr_saida','tp_entrada',
									'tp_convenio','tp_pagamento','tp_credito','tp_porcentagem','observacao','motivo',
									'fkprofissional','fkespecialidades']
				
				# todo: outra maneira de montar meu widget
				# widgets = {
				# 		'dt_movimentacao': forms.DateInput(attrs={'class': 'date-input'}),
				#
				# }
	
	
# todo: NÃO ESTA RODA ESSE CODIGO : Fazer funcionar essa classe onde monto meus widgtes de cada campo
class RawEntradaSaidaForm(forms.Form):
		dt_movimentacao = forms.DateField()
		profissional = forms.CharField()
		paciente = forms.CharField()
		qt_parcelas = forms.DecimalField()
		valor_entr_saida = forms.DecimalField(initial=0.0)
		tp_entrada = forms.ChoiceField(widget=forms.RadioSelect, choices=TP_ENTRADA,)
		tp_convenio = forms.ChoiceField(widget=forms.Select, choices=TP_CONVENIO,)
		tp_pagamento = forms.ChoiceField(widget=forms.Select, choices=TP_PAGAMENTO)
		tp_credito = forms.ChoiceField(widget=forms.Select, choices=TP_CREDITO)
		tp_porcentagem = forms.ChoiceField(widget=forms.Select, choices=TP_PORCENTAGEM)
		observacao = forms.TextInput(attrs={"placeholder": "Escreva alguma observação"})
		motivo = forms.CharField()
		fkprofissional = forms.ModelChoiceField(queryset=Profissionais.objects.all())
		fkespecialidades = forms.CharField()
		


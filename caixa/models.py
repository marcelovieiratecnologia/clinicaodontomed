from django.db import models
from django.core.exceptions import ValidationError
from django.utils.html import format_html

# Create your models here.

'''
FIELDS
tp_entrada(Entrada,Saida); tp_convenio(InterOdonto, Convênio,Particular;Bradesco); tp_pagamento(Crédito,Débito,Dinheiro), tp_credito(APrazo); tp_porcentagem(valor1,valor2,valor3,valor4)
data_movimento;
profissional;
paciente;
qt_parcelas;
valor_ent_saida;
'''

class EntradaSaida(models.Model):
		TP_ENTRADA = (
				('ENTRADA',u'Entrada'),
				('SAIDA',u'Saida'),
		)
		TP_CONVENIO = (
				('INTERODONTO',u'InterOdonto'),
				('ODONTOPREV',u'OdontoPrev'),
				('BRADESCO',u'Bradesco'),
				('PARTICULAR',u'Particular'),
		)
		TP_PAGAMENTO = (
				('CREDITO',u'Credito'),
				('DEBITO', u'Debito'),
				('DINHEIRO', u'Dinheiro'),
		)
		TP_CREDITO = (
				('APRAZO',u'A Prazo'),
		)
		TP_PORCENTAGEM = (
				('2.68', u'2.68%'),
				('7.07', u'7.07%'),
				('8.51', u'8.51%'),
		)
		dt_movimentacao = models.DateField(blank=False, null=False)
		profissional=models.CharField(verbose_name='Profissional',max_length=150,blank=True)
		paciente=models.CharField(verbose_name='Paciente',max_length=150,blank=True)
		qt_parcelas=models.IntegerField(verbose_name='Quantidade de Parcelas',default=0)
		valor_entr_saida=models.DecimalField(verbose_name='Valor',max_digits=14,decimal_places=2,default=0)
		tp_entrada=models.CharField(verbose_name='Tipos de Entrada', max_length=10, choices=TP_ENTRADA)
		tp_convenio = models.CharField(verbose_name='Tipos de Convênios', max_length=30, choices=TP_CONVENIO, blank=True, null=True)
		tp_pagamento = models.CharField(verbose_name='Tipos de Pagamentos', max_length=30, choices=TP_PAGAMENTO, blank=True, null=True)
		tp_credito = models.CharField(verbose_name='Tipos de Créditos', max_length=20, choices=TP_CREDITO, blank=True, null=True)
		tp_porcentagem = models.CharField(verbose_name='Tipos de Porcentagens', max_length=10, choices=TP_PORCENTAGEM, blank=True, null=True)
		observacao = models.TextField(verbose_name='Observação',blank=True)
		motivo = models.CharField(verbose_name='Motivo da Entrada/Saída', max_length=150, blank=True)
		
		def calcula_desconto(self):
				if self.tp_porcentagem == None:
						return 0.0
				else:
						calculo = (float(self.valor_entr_saida) * float(self.tp_porcentagem)) / 100
						return round(calculo, 2)

		def calcula_totalLiquido(self):
				valor_total = float(self.valor_entr_saida) - self.calcula_desconto()
				return "{0:.2f}".format(valor_total)
		
		
		# Modificando o valor do campo usando html
		def desconto(self):
				return format_html(
						'<span style="color:green;">{}</span>',
						self.calcula_desconto(),
				)
		def total(self):
				return format_html(
						'<span style="color:red; font-weight: bold;">{}</span>',
						self.calcula_totalLiquido(),
				)
		def valor(self):
				return format_html(
						'<span style="color:red;">{}</span>',
						self.valor_entr_saida,
				)
		
		
		class Meta:
				verbose_name = 'Tipo de Entrada'#'Entrada/Saída'
				#verbose_name_plural = 'Entradas/Saídas'
				ordering = ['dt_movimentacao']
		
		def __str__(self):
				return 'Movimentação de: ' #.self.tp_entrada
		
		#Validações
		def clean(self):
				# Validações para os tipos de Movimentações de Entradas
				if self.tp_entrada == 'Entrada':
						#if self.tp_convenio:
						if self.tp_convenio == None:
								raise ValidationError({'tp_convenio','Sendo uma ENTRADA, o campo Tipo de Convênio tem que ser preenchido'})

						#if self.paciente:
						self.paciente = self.paciente.strip()
						if len(self.paciente.split(' ')) < 2:
								raise ValidationError({'paciente':'Nome e Sobrenome do Paciente são queridos'})

				
				# Validações para os tipos de Movimentações de Saídas
				if self.tp_entrada == 'SAIDA':
						if self.motivo == '':
								raise ValidationError({'motivo':'Sendo uma SAÍDA é necessário especificar algum motivo'})
								
			
				#Validações que servem para as duas Movimentações
				if self.qt_parcelas < 0:
						raise ValidationError({'qt_parcelas': 'Quantidade de parcelas não pode ser menor que 0'})
				
				if (self.valor_entr_saida == 0.00) :
						raise ValidationError({'valor_entr_saida':'O Valor tem que ser maior que 0'})
						
				
				super().clean()
				
				
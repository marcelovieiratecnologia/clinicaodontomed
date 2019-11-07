from django.db import models

from django.core.exceptions import ValidationError
from django.utils.html import format_html
#from joinfield.joinfield import JoinField
import datetime

# Create your models here.

'''
@@@ fazer algo assim para que eu trafegue no link com o UUID e não com o id , isso por segurança !
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, UUIDField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
import uuid

class User(AbstractUser):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
				('0.00',u'0.00%'),
				('2.68', u'2.68%'),
				('7.07', u'7.07%'),
				('8.51', u'8.51%'),
		)
		# id_entrada_saida = # Não preciso me preocupar com o campo ID o django cria sozinho e como primary key e auto incremento.
		#dt_movimentacao = models.DateField(blank=False, null=False) #auto_now_add=True) serve para auto preencher o campo com a a data e hora atual, mas esta dando pau
		dt_movimentacao = models.DateField(default=datetime.datetime.now, null=False, blank=False)
		profissional=models.CharField(verbose_name='Profissional',max_length=130,blank=True)
		paciente=models.CharField(verbose_name='Paciente',max_length=130,blank=True)
		qt_parcelas=models.IntegerField(verbose_name='Quantidade de Parcelas',default=0)
		valor_entr_saida=models.DecimalField(verbose_name='Valor',max_digits=14,decimal_places=2,default=0.00, blank=True)
		tp_entrada=models.CharField(verbose_name='Tipos de Entrada', max_length=10, choices=TP_ENTRADA)
		tp_convenio = models.CharField(verbose_name='Tipos de Convênios', max_length=30, choices=TP_CONVENIO, blank=True, null=True)
		tp_pagamento = models.CharField(verbose_name='Tipos de Pagamentos', max_length=30, choices=TP_PAGAMENTO, blank=True, null=True)
		tp_credito = models.CharField(verbose_name='Tipos de Créditos', max_length=20, choices=TP_CREDITO, blank=True, null=True)
		tp_porcentagem = models.CharField(verbose_name='Tipos de Porcentagens', max_length=10, choices=TP_PORCENTAGEM, default=0.00, blank=True, null=True)
		observacao = models.TextField(verbose_name='Observação',blank=True)
		motivo = models.CharField(verbose_name='Motivo da Entrada/Saída', max_length=150, blank=True)
		fkprofissional = models.ForeignKey('profissional.Profissionais',verbose_name='Profissional',related_name='qry_profissionais', on_delete=models.CASCADE)
		fkespecialidades = models.ForeignKey('profissional.Especialidades', verbose_name='Especialidades', related_name='qry_especialidades',null=True, blank=True, on_delete=models.CASCADE)

		class Meta:
				db_table = 'tb_om_entrada_saida' # definindo o nome da tabela, no caso não utilizei deixei o django fazer por mim
				verbose_name = 'Tipo de Entrada'#'Entrada/Saída'
				verbose_name_plural = 'Tipos de Entradas'
				ordering = ['dt_movimentacao']

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
						'<span style="color:#006400;">{}</span>',
						self.calcula_desconto(),
				)
		def total(self):
				return format_html(
						'<span style="color:#FF0000; font-weight: bold;">{}</span>',
						self.calcula_totalLiquido(),
				)
		def valor(self):
				return format_html(
						'<span style="color:#FF0000;">{}</span>',
						self.valor_entr_saida,
				)

	
		# Esse método estava salvando certo pelo /admin , mas pelo front estava dando problemas com o seguinte erro: "Cannot force an update in save() with no primary key."
		def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
				self.paciente = self.paciente.upper()
				super(EntradaSaida, self).save()
		
		#  Validações
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
				
		def __str__(self):
				data = self.dt_movimentacao.strftime('%d/%m/%Y') # formatando a data
				texto = self.tp_entrada + ' de R$ ' + str(self.valor_entr_saida) + ' , Data do Movimento de: ' + data
				return texto

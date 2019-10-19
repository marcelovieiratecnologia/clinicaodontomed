from django.db.models import Sum, Aggregate, Avg
from datetime import datetime, date

from ..models import EntradaSaida

data = datetime.now()

def listar_entrada_saida():
		data = datetime.now()
		return EntradaSaida.objects.filter(dt_movimentacao=data)
		
def listar_entrada_saida_data(data): # Listo sempre o mes corrente
		return EntradaSaida.objects.filter(dt_movimentacao=data)

def listar_entrada_saida_anomes(ano,mes):
		return EntradaSaida.objects.filter(dt_movimentacao__year=ano).filter(dt_movimentacao__month=mes)
		
def listar_entrada_saida_id(id):
		
		entrada_saida_id = EntradaSaida.objects.get(id=id)
		
		# especialidade = Entrada.objects.get
		# print('ssssssssssssssss', entrada_saida_id.fkespecialidades)
		return entrada_saida_id

def cadastrar_entrada_saida(entrada_saida):
		entrada_saida_bd = EntradaSaida.objects.create(dt_movimentacao=entrada_saida.dt_movimentacao,
																									 profissional=entrada_saida.profissional,
																									 paciente=entrada_saida.paciente,
																									 qt_parcelas=entrada_saida.qt_parcelas,
																									 valor_entr_saida=entrada_saida.valor_entr_saida,
																									 tp_entrada=entrada_saida.tp_entrada,
																									 tp_convenio=entrada_saida.tp_convenio,
																									 tp_pagamento=entrada_saida.tp_pagamento,
																									 tp_credito=entrada_saida.tp_credito,
																									 tp_porcentagem=entrada_saida.tp_porcentagem,
																									 observacao=entrada_saida.observacao, motivo=entrada_saida.motivo,
																									 fkprofissional=entrada_saida.fkprofissional,
																									 fkespecialidades=entrada_saida.fkespecialidades)
		entrada_saida_bd.save()

def editar_entrada_saida(entrada_saida_bd, entrada_saida_nova):
		entrada_saida_bd.dt_movimentacao = entrada_saida_nova.dt_movimentacao
		entrada_saida_bd.profissional = entrada_saida_nova.profissional
		entrada_saida_bd.paciente = entrada_saida_nova.paciente
		entrada_saida_bd.qt_parcelas = entrada_saida_nova.qt_parcelas
		entrada_saida_bd.valor_entr_saida = entrada_saida_nova.valor_entr_saida
		entrada_saida_bd.tp_entrada = entrada_saida_nova.tp_entrada
		entrada_saida_bd.tp_convenio = entrada_saida_nova.tp_convenio
		entrada_saida_bd.tp_pagamento = entrada_saida_nova.tp_pagamento
		entrada_saida_bd.tp_credito = entrada_saida_nova.tp_credito
		entrada_saida_bd.tp_porcentagem = entrada_saida_nova.tp_porcentagem
		entrada_saida_bd.observacao = entrada_saida_nova.observacao
		entrada_saida_bd.motivo = entrada_saida_nova.motivo
		entrada_saida_bd.fkprofissional = entrada_saida_nova.fkprofissional
		entrada_saida_bd.fkespecialidades = entrada_saida_nova.fkespecialidades
		entrada_saida_bd.save(force_update=True)
		
def remover_entrada_saida(entrada_saida_bd):
		entrada_saida_bd.delete()

# Estou usando um for na VIEW
# def calcula_total_final():
# 		total_final = EntradaSaida.objects.all().aggregate(Sum('valor_entr_saida')).get('valor_entr_saida__sum')
# 		# desconto_final = EntradaSaida.objects.all().aggregate(Sum('__desconto')).get('desconto__sum')
# 		return total_final

# Vai ser um tipo de total que vou deixar em cima do DataTable
def calcula_total_entrada():
		total_entrada_mes = EntradaSaida.objects.filter(tp_entrada='ENTRADA', dt_movimentacao__year=data.year, dt_movimentacao__month=data.month).aggregate(Sum('valor_entr_saida')).get('valor_entr_saida__sum')
		if total_entrada_mes == None:
				total_entrada_mes = 0.00
		# desconto_final = EntradaSaida.objects.all().aggregate(Sum('__desconto')).get('desconto__sum')
		return total_entrada_mes

# Vai ser um tipo de total que vou deixar em cima do DatTable
def calcula_total_saida():
		total_saida_mes = EntradaSaida.objects.filter(tp_entrada='SAIDA', dt_movimentacao__year=data.year, dt_movimentacao__month=data.month).aggregate(Sum('valor_entr_saida')).get('valor_entr_saida__sum')
		if total_saida_mes == None:
				total_saida_mes = 0.00
		# desconto_final = EntradaSaida.objects.all().aggregate(Sum('__desconto')).get('desconto__sum')
		return total_saida_mes

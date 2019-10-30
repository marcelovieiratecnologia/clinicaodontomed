from django.shortcuts import render, redirect, render_to_response
from .forms import EntradaSaidaForm
from .entidades.entrada_saida import Entrada_Saida
from .services import entrada_saida_service
from profissional.services import profissional_service
from profissional.services import especialidades_service
from datetime import date, datetime
import ast
from decimal import *

from .models import EntradaSaida
import json

def index(request):
		return render_to_response()

def listar_especialidades_profissional(request):
		id_fkprofissional = request.GET.get('id_fkprofissional') # vem do meu ajax
		especialidades_profissional = profissional_service.listar_especialidades_profissional(id_fkprofissional)
		context = {'especialidades_profissional': especialidades_profissional}
		return  render(request, 'caixa/includes/_especialidadesprofissional.html', context)

def listar_entrada_saida_anomes(request):
		
		anomes = request.GET.get('datepicker_month_filter')
		ano = anomes[-4:] # pego o ano da string '09/2019'
		mes = anomes[:-5] # pego o mes da string '09/2019'
		
		entradas_saidas = entrada_saida_service.listar_entrada_saida_anomes(ano, mes)
		
		total_bruto_final = 0.00
		total_desconto_final = 0.00
		total_liquido_final = 0.00
		
		for entrada_saida in entradas_saidas:
				total_bruto_final = float(total_bruto_final) + float(entrada_saida.valor_entr_saida)
				if entrada_saida.tp_porcentagem != None:
						total_desconto_final = total_desconto_final + (float(entrada_saida.valor_entr_saida) * float(entrada_saida.tp_porcentagem)) / 100
		
		total_liquido_final = + total_bruto_final - total_desconto_final
		total_mes_entrada = entrada_saida_service.calcula_total_entrada()
		total_mes_saida = entrada_saida_service.calcula_total_saida()
		return render(request, 'caixa/listar_entrada_saida.html', {"entradas_saidas": entradas_saidas,
																															 "total_bruto_final": round(total_bruto_final, 2),
																															 "total_desconto_final": round(total_desconto_final, 2),
																															 "total_liquido_final": round(total_liquido_final, 2),
																															 "total_mes_entrada": round(total_mes_entrada, 2),
																															 "total_mes_saida": round(total_mes_saida, 2),
																															 })

def listar_entrada_saida_data(request):
		
		dt = request.GET.get('datepicker_filter')
		data = datetime.strptime(dt, '%d/%m/%Y').date()
		
		entradas_saidas = entrada_saida_service.listar_entrada_saida_data(data)
		total_bruto_final = 0.00
		total_desconto_final = 0.00
		total_liquido_final = 0.00
		
		for entrada_saida in entradas_saidas:
				total_bruto_final = float(total_bruto_final) + float(entrada_saida.valor_entr_saida)
				total_desconto_final = total_desconto_final + (
										float(entrada_saida.valor_entr_saida) * float(entrada_saida.tp_porcentagem)) / 100
		
		total_liquido_final = + total_bruto_final - total_desconto_final
		total_mes_entrada = entrada_saida_service.calcula_total_entrada()
		total_mes_saida = entrada_saida_service.calcula_total_saida()
		return render(request, 'caixa/listar_entrada_saida.html', {"entradas_saidas": entradas_saidas,
																															 "total_bruto_final": round(total_bruto_final, 2),
																															 "total_desconto_final": round(total_desconto_final, 2),
																															 "total_liquido_final": round(total_liquido_final, 2),
																															 "total_mes_entrada": round(total_mes_entrada, 2),
																															 "total_mes_saida": round(total_mes_saida, 2),
																															 })

def listar_entrada_saida(request):
		
		entradas_saidas = entrada_saida_service.listar_entrada_saida()
		total_bruto_final = 0.00
		total_desconto_final = 0.00
		total_liquido_final = 0.00
		
		for entrada_saida in entradas_saidas:
				total_bruto_final = float(total_bruto_final) + float(entrada_saida.valor_entr_saida)
				if entrada_saida.tp_porcentagem != None:
					total_desconto_final = total_desconto_final + (float(entrada_saida.valor_entr_saida) * ast.literal_eval(entrada_saida.tp_porcentagem)) / 100

		total_liquido_final = + float(total_bruto_final) - total_desconto_final
		total_mes_entrada = entrada_saida_service.calcula_total_entrada()
		total_mes_saida = entrada_saida_service.calcula_total_saida()
		
		return render(request, 'caixa/listar_entrada_saida.html', {"entradas_saidas": entradas_saidas,
																															 "total_bruto_final": round(total_bruto_final,2),
																															 "total_desconto_final": round(total_desconto_final, 2),
																															 "total_liquido_final": round(total_liquido_final, 2),
																															 "total_mes_entrada": round(total_mes_entrada, 2),
																															 "total_mes_saida": round(total_mes_saida, 2),
																															 })

def cadastrar_entrada_saida(request):
	
		context = {}
		profissionais = profissional_service.listar_profissional()
		especialidades = especialidades_service.listar_especialidade()
		#especialidades = profissional_service.listar_especialidade_id(id)
		if request.method == "POST": # vejo se esta sendo um POST
				form_entrada_saida = EntradaSaidaForm(request.POST)
				if form_entrada_saida.is_valid(): # se for válido sigo 
						dt_movimentacao = form_entrada_saida.cleaned_data['dt_movimentacao']
						profissional = form_entrada_saida.cleaned_data['profissional']
						paciente = form_entrada_saida.cleaned_data['paciente']
						qt_parcelas = form_entrada_saida.cleaned_data['qt_parcelas']
						valor_entr_saida = form_entrada_saida.cleaned_data['valor_entr_saida']
						tp_entrada = form_entrada_saida.cleaned_data['tp_entrada']
						tp_convenio = form_entrada_saida.cleaned_data['tp_convenio']
						tp_pagamento = form_entrada_saida.cleaned_data['tp_pagamento']
						tp_credito = form_entrada_saida.cleaned_data['tp_credito']
						tp_porcentagem = form_entrada_saida.cleaned_data['tp_porcentagem']
						observacao = form_entrada_saida.cleaned_data['observacao']
						motivo = form_entrada_saida.cleaned_data['motivo']
						fkprofissional = form_entrada_saida.cleaned_data['fkprofissional']
						fkespecialidades = form_entrada_saida.cleaned_data['fkespecialidades']
						# Crio uma nova variavel que ai receber os dados , para que eu passe para o meu entidades/Entrada_Saida.py
						entrada_saida_nova = Entrada_Saida(dt_movimentacao=dt_movimentacao,profissional=profissional,paciente=paciente,qt_parcelas=qt_parcelas,valor_entr_saida=valor_entr_saida,
																							 tp_entrada=tp_entrada,tp_convenio=tp_convenio,tp_pagamento=tp_pagamento,tp_credito=tp_credito,tp_porcentagem=tp_porcentagem,
																							 observacao=observacao,motivo=motivo,fkprofissional=fkprofissional,fkespecialidades=fkespecialidades)
						# passando para o service os dados , e lá vou executar meu create
						entrada_saida_service.cadastrar_entrada_saida(entrada_saida_nova) # aqui que cadastra , executa o create no service
						return redirect('listar_entrada_saida') # dando certo chamo meu metodo 'listar_entrada_saida' que no caso ele se ecarrega de chamar meu html para que liste todas as entradas e saidas
		else:
				form_entrada_saida = EntradaSaidaForm()
		return render(request, 'caixa/form_entrada_saida.html', {'form_entrada_saida': form_entrada_saida})  #, 'profissionais': profissionais,'especialidades': especialidades})
																																																		
def editar_entrada_saida(request, id):
		
		entrada_saida_bd = entrada_saida_service.listar_entrada_saida_id(id) # trago os dados da tabela que tem relação com o ID que estou passando
		
		id_fkprofissional = entrada_saida_bd.fkprofissional_id
		especialidades_profissional = profissional_service.listar_especialidades_profissional(id_fkprofissional) # trago as especialidades do profissional
		
		especialidade = entrada_saida_bd.fkespecialidades # é a especialidade que foi gravado na tabela
		
		form_entrada_saida = EntradaSaidaForm(request.POST or None, instance=entrada_saida_bd)
		if form_entrada_saida.is_valid():
				# print(form_entrada_saida)
				dt_movimentacao = form_entrada_saida.cleaned_data['dt_movimentacao']
				profissional = form_entrada_saida.cleaned_data['profissional']
				paciente = form_entrada_saida.cleaned_data['paciente']
				qt_parcelas = form_entrada_saida.cleaned_data['qt_parcelas']
				valor_entr_saida = form_entrada_saida.cleaned_data['valor_entr_saida']
				tp_entrada = form_entrada_saida.cleaned_data['tp_entrada']
				tp_convenio = form_entrada_saida.cleaned_data['tp_convenio']
				tp_pagamento = form_entrada_saida.cleaned_data['tp_pagamento']
				tp_credito = form_entrada_saida.cleaned_data['tp_credito']
				tp_porcentagem = form_entrada_saida.cleaned_data['tp_porcentagem']
				observacao = form_entrada_saida.cleaned_data['observacao']
				motivo = form_entrada_saida.cleaned_data['motivo']
				fkprofissional = form_entrada_saida.cleaned_data['fkprofissional']
				fkespecialidades = form_entrada_saida.cleaned_data['fkespecialidades']
				entrada_saida_nova = Entrada_Saida(dt_movimentacao=dt_movimentacao,profissional=profissional,paciente=paciente,qt_parcelas=qt_parcelas,valor_entr_saida=valor_entr_saida,
																							 tp_entrada=tp_entrada,tp_convenio=tp_convenio,tp_pagamento=tp_pagamento,tp_credito=tp_credito,tp_porcentagem=tp_porcentagem,
																							 observacao=observacao,motivo=motivo,fkprofissional=fkprofissional,fkespecialidades=fkespecialidades)
				entrada_saida_service.editar_entrada_saida(entrada_saida_bd, entrada_saida_nova)
				return redirect('listar_entrada_saida')

		# print('ddddddddddddddddddddddddd', form_entrada_saida)
		return render(request, 'caixa/form_entrada_saida.html', {'form_entrada_saida': form_entrada_saida, # os dados que vem da tabela
																														 'especialidade': especialidade,
																														 'id_fkespecialidades': especialidades_profissional,
																														 })
		
def remover_entrada_saida(request, id):
		entrada_saida_bd = entrada_saida_service.listar_entrada_saida_id(id)
		if request.method == "POST":
				entrada_saida_service.remover_entrada_saida(entrada_saida_bd)
				return redirect('listar_entrada_saida')
		return render(request, 'caixa/confirma_exclusao.html', {'entrada_saida': entrada_saida_bd})


# VIEWs CHARTs
# def charts(request, *args, **kwargs):
# 		data = {
# 				"sales":100,
# 				"costumers": 10,
# 		}
# 		return render(request, 'charts/charts.html')


def charts(request):
		queryset = EntradaSaida.objects.all()
		names = [obj.tp_entrada for obj in queryset]
		
		prices = [int(obj.valor_entr_saida) for obj in queryset]
		date = [str(obj.dt_movimentacao) for obj in queryset]
		for dt in date:
				print(type(dt))
				data = datetime.strptime(dt, '%d/%m/%Y').date()
		
		print('ddddddddddddddddddddddd',type(date[:][0]))
		# print('fffffffffffffffffffffffff', data)
		context = {
        'names': json.dumps(names),
        'prices': json.dumps(prices),
				'date': json.dumps(date),
				'choice_colours': ['rgba(0, 209, 178, 0.55)'] * len(date),
				'choice_border_colours': ['rgba(0, 209, 178, 0.9)'] * len(date),
    }
		print(context)
		return render(request, 'charts/charts.html', context)
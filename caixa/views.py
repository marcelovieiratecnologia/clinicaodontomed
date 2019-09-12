from django.shortcuts import render, redirect, render_to_response
from .forms import EntradaSaidaForm
from .entidades.entrada_saida import Entrada_Saida
from .services import entrada_saida_service

# Create your views here.

def index(request):
		return render_to_response()


def listar_entrada_saida(request):
		# imprimir_variavel = 'Valor da variavel impressa no html que esta vindo da VIEW do APP Caixa'
		# dicinario_Imprimir_variavel = {'dicinario_Imprimir_variavel': "Passando o valor para o html através de uma variavel de Dicionário"}
		entradas_saidas = entrada_saida_service.listar_entrada_saida()
		return render(request, 'caixa/listar_entrada_saida.html', {"entradas_saidas": entradas_saidas})

def cadastrar_entrada_saida(request):

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
		return render(request, 'caixa/form_entrada_saida.html', {'form_entrada_saida': form_entrada_saida})
																																																		
def editar_entrada_saida(request, id):
		entrada_saida_bd = entrada_saida_service.listar_entrada_saida_id(id)
		form_entrada_saida = EntradaSaidaForm(request.POST or None, instance=entrada_saida_bd)
		if form_entrada_saida.is_valid():
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
		return render(request, 'caixa/form_entrada_saida.html', {'form_entrada_saida': form_entrada_saida})
		
		


def remover_entrada_saida(request, id):
		entrada_saida_bd = entrada_saida_service.listar_entrada_saida_id(id)
		if request.method == "POST":
				entrada_saida_service.remover_entrada_saida(entrada_saida_bd)
				return redirect('listar_entrada_saida')
		return render(request, 'caixa/confirma_exclusao.html', {'entrada_saida': entrada_saida_bd})


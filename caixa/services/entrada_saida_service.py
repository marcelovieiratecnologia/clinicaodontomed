from ..models import EntradaSaida

def cadastrar_entrada_saida(entrada_saida):
		entrada_saida_bd = EntradaSaida.objects.create(dt_movimentacao=entrada_saida.dt_movimentacao, profissional=entrada_saida.profissional, paciente=entrada_saida.paciente,
																qt_parcelas=entrada_saida.qt_parcelas, valor_entr_saida=entrada_saida.valor_entr_saida,tp_entrada=entrada_saida.tp_entrada,
																tp_convenio=entrada_saida.tp_convenio, tp_pagamento=entrada_saida.tp_pagamento, tp_credito=entrada_saida.tp_credito,
																tp_porcentagem=entrada_saida.tp_porcentagem,observacao=entrada_saida.observacao, motivo=entrada_saida.motivo,
																fkprofissional=entrada_saida.fkprofissional, fkespecialidades=entrada_saida.fkespecialidades)
		entrada_saida_bd.save()

def listar_entrada_saida():
		return EntradaSaida.objects.all()

def listar_entrada_saida_id(id):
		return EntradaSaida.objects.get(id=id)

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
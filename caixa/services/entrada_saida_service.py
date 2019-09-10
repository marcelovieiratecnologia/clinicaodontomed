from ..models import EntradaSaida

def cadastrar_entrada_saida(entrada_saida):
		EntradaSaida.objetcs.create(dt_movimentacao=entrada_saida.dt_movimentacao, profissional=entrada_saida.prodissional, paciente=entrada_saida.paciente, qt_parcelas=entrada_saida.qt_parcelas, valor_entr_saida=entrada_saida.valor_entr_saida,
																tp_entrada=entrada_saida.tp_entrada, tp_convenio=entrada_saida.tp_convenio, tp_pagamento=entrada_saida.tp_pagamento, tp_credito=entrada_saida.tp_credito, tp_porcentagem=entrada_saida.tp_porcentagem,
																observacao=entrada_saida.observacao, motivo=entrada_saida.motivo, fkprofissional=entrada_saida.fkprofissional, fkespecialidades=entrada_saida.fkespecialidades)
		

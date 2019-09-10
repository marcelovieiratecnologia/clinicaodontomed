

class Entrada_Saida():
		def __init__(self, dt_movimentacao,profissional,paciente,qt_parcelas,valor_entr_saida,tp_entrada,tp_convenio,tp_pagamento,tp_credito,tp_porcentagem,observacao,motivo,fkprofissional,fkespecialidades):
				self.__dt_movimentacao = dt_movimentacao
				self.__profissional = profissional
				self.__paciente = paciente
				self.__qt_parcelas = qt_parcelas
				self.__valor_entr_saida = valor_entr_saida
				self.__tp_entrada = tp_entrada
				self.__tp_convenio = tp_convenio
				self.__tp_pagamento = tp_pagamento
				self.__tp_credito = tp_credito
				self.__tp_porcentagem = tp_porcentagem
				self.__observacao = observacao
				self.__motivo = motivo
				self.__fkprofissional = fkprofissional
				self.__fkespecialidades = fkespecialidades
				
		@property
		def dt_movimentacao(self):
				return self.__dt_movimentacao
		
		@dt_movimentacao.setter
		def dt_movimentacao(self, dt_movimentacao):
				self.__dt_movimentacao = dt_movimentacao
		
		@property
		def profissional(self):
				return self.__profissional
		
		@profissional.setter
		def profissional(self, profissional):
				self.__profissional = profissional
		
		@property
		def paciente(self):
				return self.__paciente
		
		@paciente.setter
		def paciente(self, paciente):
				self.__paciente = paciente
		
		@property
		def qt_parcelas(self):
				return self.__qt_parcelas
		
		@qt_parcelas.setter
		def qt_parcelas(self, qt_parcelas):
				self.__qt_parcelas= qt_parcelas
		
		@property
		def valor_entr_saida(self):
				return self.__valor_entr_saida
		
		@valor_entr_saida.setter
		def valor_entr_saida(self, valor_entr_saida):
				self.__valor_entr_saida = valor_entr_saida
		
		@property
		def tp_entrada(self):
				return self.__tp_entrada
		
		@tp_entrada.setter
		def tp_entrada(self, tp_entrada):
				self.__tp_entrada = tp_entrada
		
		@property
		def tp_convenio(self):
				return self.__tp_convenio
		
		@tp_convenio.setter
		def tp_convenio(self, tp_convenio):
				self.__tp_convenio = tp_convenio
		
		@property
		def tp_pagamento(self):
				return self.__tp_pagamento
		
		@tp_pagamento.setter
		def tp_pagamento(self, tp_pagamento):
				self.__tp_pagamento = tp_pagamento
		
		@property
		def tp_credito(self):
				return self.__tp_credito
		
		@tp_credito.setter
		def tp_credito(self, tp_credito):
				self.__tp_credito = tp_credito
		
		@property
		def tp_porcentagem(self):
				return self.__tp_porcentagem
		
		@tp_porcentagem.setter
		def tp_porcentagem(self, tp_porcentagem):
				self.__tp_porcentagem = tp_porcentagem
		
		@property
		def observacao(self):
				return self.__observacao
		
		@observacao.setter
		def observacao(self, observacao):
				self.__observacao = observacao
		
		@property
		def motivo(self):
				return self.__motivo
		
		@motivo.setter
		def motivo(self, motivo):
				self.__motivo = motivo
		
		@property
		def fkprofissional(self):
				return self.__fkprofissional
		
		@fkprofissional.setter
		def fkprofissional(self, fkprofissional):
				self.__fkprofissional = fkprofissional
		
		@property
		def fkespecialidades(self):
				return self.__fkespecialidades
		
		@fkespecialidades.setter
		def fkespecialidades(self, fkespecialidades):
				self.__fkespecialidades = fkespecialidades
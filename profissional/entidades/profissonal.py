
class Profissional():
		def __init__(self, nome_profissional, cpf_profissional, num_registro_classe, cidades, orgao_emissor, especialidades):
				self.__nome_profissional = nome_profissional
				self.__cpf_profissional = cpf_profissional
				self.__num_registro_classe = num_registro_classe
				self.__cidades = cidades
				self.__orgao_emissor = orgao_emissor
				self.__especialidades = especialidades
				
		@property
		def nome_profissional(self):
				return self.__nome_profissional
		@nome_profissional.setter
		def nome_profissional(self, nome_profissional):
				self.__nome_profissional = nome_profissional
				
		@property
		def cpf_profissional(self):
				return self.__cpf_profissional
		@cpf_profissional.setter
		def cpf_profissional(self, cpf_profissional):
				self.__cpf_profissional = cpf_profissional

		@property
		def num_registro_classe(self):
				return self.__num_registro_classe
		@num_registro_classe.setter
		def num_registro_classe(self, num_registro_classe):
				self.__num_registro_classe = num_registro_classe
				
		@property
		def cidades(self):
				return self.__cidades
		@cidades.setter
		def cidades(self, cidades):
				self.__cidades = cidades

		@property
		def orgao_emissor(self):
				return self.__orgao_emissor
		@orgao_emissor.setter
		def orgao_emissor(self, orgao_emissor):
				self.__orgao_emissor = orgao_emissor

		@property
		def especialidades(self):
				return self.__especialidades
		@especialidades.setter
		def especialidades(self, especialidades):
				self.__especialidades = especialidades
			
		
		
				
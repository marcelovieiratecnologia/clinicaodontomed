
class Cidade():
		def __init__(self, nome_cidade,uf):
				self.__nome_cidade = nome_cidade
				self.__uf = uf
		
		@property
		def nome_cidade(self):
				return self.__nome_cidade
		
		@nome_cidade.setter
		def nome_cidade(self, nome_cidade):
				self.__nome_cidade = nome_cidade
				
		
		@property
		def uf(self):
				return self.__uf
		
		@uf.setter
		def uf(self, uf):
				self.__uf = uf


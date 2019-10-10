from django.db import connection
from ..models import Profissionais, Especialidades
from ..services import especialidades_service


def listar_especialidades_profissional(id):
		# Lista quais os profissionais da especialidade que escolhi
		# profespe = Profissionais.objects.filter(especialidades__id=2)
		# print('Profissionais da especialidade', profespe)
		
		# Lista as especialidades do profissional que escolhi
		especialidades_profissional = Especialidades.objects.filter(profissionais__id=id)
		return especialidades_profissional


def listar_profissional():
		#return Profissionais.objects.all()
		profissionais = Profissionais.objects.select_related('orgao_emissor').all()  #foreingn KEY
		#profissionais = Profissionais.objects.prefetch_related('especialidades').all()
		return profissionais
		
def listar_profissional_id(id):
		profissional = Profissionais.objects.get(id=id)
		for i in profissional.especialidades.all():
				print(i.especialidade)
		# print(connection.queries)
		# print(len(connection.queries))
		# print(profissional)
		return profissional
		#return Profissionais.objects.get(id=id)


def cadastrar_profissional(profissional):
		profissional_bd = Profissionais.objects.create(nome_profissional=profissional.nome_profissional, cpf_profissional=profissional.cpf_profissional,
																									 num_registro_classe=profissional.num_registro_classe,cidades=profissional.cidades,
																									 orgao_emissor=profissional.orgao_emissor)
		profissional_bd.save()
		for i in profissional.especialidades:
				# print(profissional.especialidades)
				especialidade = especialidades_service.listar_especialidades_id()
				# print('esppppp:: ', especialidade)
				# profissional = profissional_bd.nome_profissional
				# print('Dados-Esp-Prof', especialidade, profissional)
				profissional_bd.especialidades.add(especialidade)
				# print(profissional_bd)


def editar_profissional(profissional, profissional_nova):
		profissional.nome_profissional = profissional_nova.nome_profissional
		profissional.cpf_profissional = profissional_nova.cpf_profissional
		profissional.num_registro_classe = profissional_nova.num_registro_classe
		profissional.cidades = profissional_nova.cidades
		profissional.orgao_emissor = profissional_nova.orgao_emissor
		# print(profissional_nova.especialidades)
		profissional.especialidades.set(profissional_nova.especialidades)
		profissional.save(force_update=True)
		
def remover_profissional(profissional_bd):
		profissional_bd.delete()
		
		

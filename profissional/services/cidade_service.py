from ..models import Cidades


def listar_cidade():
		return Cidades.objects.all()

def listar_cidade_id(id):
		return Cidades.objects.get(id=id)

def cadastrar_cidade(cidade):
		cidade_bd = Cidades.objects.create(nome_cidade=cidade.nome_cidade, uf=cidade.uf)
		cidade_bd.save()

def editar_cidade(cidade_bd, cidade_nova):
		cidade_bd.nome_cidade = cidade_nova.nome_cidade
		cidade_bd.uf = cidade_nova.uf
		cidade_bd.save(force_update=True)

def remover_cidade(cidade_bd):
		cidade_bd.delete()
		




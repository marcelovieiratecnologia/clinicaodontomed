from ..models import Especialidades

def listar_especialidade():
		return Especialidades.objects.all()

def listar_especialidades_id(id):
		return Especialidades.objects.get(id=id)

def cadastrar_especialidade(especialidade):
		especialidade_bd =  Especialidades.objects.create(especialidade=especialidade.especialidade)
		especialidade_bd.save

def remover_especialidade(especialidade_bd):
		especialidade_bd.delete()
		
def editar_especialidade(especialidade_bd, especialidade_nova):
		especialidade_bd.especialidade = especialidade_nova.especialidade
		especialidade_bd.save(force_update=True)
		


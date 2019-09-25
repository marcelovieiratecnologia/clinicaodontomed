from ..models import Especialidades

def listar_especialidade():
		return Especialidades.objects.all()

def listar_especialidades_id(id):
		return Especialidades.objects.get(id=id)

def cadastrar_especialidade():
		return Especialidades.objects.all()


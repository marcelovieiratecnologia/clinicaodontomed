from django.shortcuts import render, redirect,render_to_response
from ..forms.profissional_forms import ProfissionaisForm
from ..entidades.profissonal import *
from ..services import profissional_service
# Create your views here.

def index(request):
		return render_to_response()

# @@@@@@@@@ Profissional @@@@@@@@@
def listar_profissional(request):
		profissionais = profissional_service.listar_profissional()
		return render(request, 'profissional/listar_profissional.html', {'profissionais': profissionais})

def cadastrar_profissional(request):
		if request.method == "POST":
				form_profissional = ProfissionaisForm(request.POST)
				if form_profissional.is_valid():
						nome_profissional = form_profissional.cleaned_data['nome_profissional']
						cpf_profissional = form_profissional.cleaned_data['cpf_profissional']
						num_registro_classe = form_profissional.cleaned_data['num_registro_classe']
						cidades = form_profissional.cleaned_data['cidades']
						orgao_emissor = form_profissional.cleaned_data['orgao_emissor']
						especialidades = form_profissional.cleaned_data['especialidades']
						form_profissional_nova = Profissional(nome_profissional=nome_profissional,cpf_profissional=cpf_profissional,
																									num_registro_classe=num_registro_classe,cidades=cidades,orgao_emissor=orgao_emissor,
																									especialidades=especialidades)
						profissional_service.cadastrar_profissional(form_profissional_nova)
						return redirect('listar_profissional')
		else:
				form_profissional = ProfissionaisForm()
				return render(request, 'profissional/form_profissional.html', {'form_profissional': form_profissional})


def editar_profissional(request, id):
		profissional_antigo = profissional_service.listar_profissional_id(id)
		form_profissional = ProfissionaisForm(request.POST or None, instance=profissional_antigo)
		if form_profissional.is_valid():
				nome_profissional = form_profissional.cleaned_data['nome_profissional']
				cpf_profissional = form_profissional.cleaned_data['cpf_profissional']
				num_registro_classe = form_profissional.cleaned_data['num_registro_classe']
				cidades = form_profissional.cleaned_data['cidades']
				orgao_emissor = form_profissional.cleaned_data['orgao_emissor']
				especialidades = form_profissional.cleaned_data['especialidades']
				profissional_nova = Profissional(nome_profissional=nome_profissional, cpf_profissional=cpf_profissional,num_registro_classe=num_registro_classe,
																				 cidades=cidades,orgao_emissor=orgao_emissor,especialidades=especialidades)
				profissional_service.editar_profissional(profissional_antigo, profissional_nova)
				return redirect('listar_profissional')
		return render(request, 'profissional/form_profissional.html', {'form_profissional': form_profissional})

def remover_profissional(request,id):
		profissional_bd = profissional_service.listar_profissional_id(id)
		if request.method=="POST":
				profissional_service.remover_profissional(profissional_bd)
				return redirect('listar_profissional')
		return render(request, 'profissional/confirma_exclusao.html', {'profissional': profissional_bd})



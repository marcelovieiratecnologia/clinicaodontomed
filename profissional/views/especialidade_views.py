from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,render_to_response
from ..forms.especialidade_forms import EspecialidadesForm
from ..entidades.especialidade import Especialidade
from ..services import especialidades_service

@login_required()
def listar_especialidade(request):
		especialidades = especialidades_service.listar_especialidade()
		return render(request, 'especialidade/listar_especialidade.html', {'especialidades': especialidades})

@login_required()
def cadastrar_especialidade(request):
		if request.method == "POST":
				form_especialidade = EspecialidadesForm(request.POST)
				if form_especialidade.is_valid():
						especialidade = form_especialidade.cleaned_data['especialidade']
						form_especialidade_nova = Especialidade(especialidade=especialidade)
						especialidades_service.cadastrar_especialidade(form_especialidade_nova)
						return redirect('listar_especialidade')
		else:
				form_especialidade = EspecialidadesForm()
				return render(request, 'especialidade/form_especialidade.html', {'form_especialidade': form_especialidade})

@login_required()
def editar_especialidade(request, id):
		especialidade_bd = especialidades_service.listar_especialidades_id(id)
		form_especialidade = EspecialidadesForm(request.POST or None, instance=especialidade_bd)
		if form_especialidade.is_valid():
				especialidade = form_especialidade.cleaned_data['especialidade']
				especialidade_nova = Especialidade(especialidade=especialidade)
				especialidades_service.editar_especialidade(especialidade_bd, especialidade_nova)
				return redirect('listar_especialidade')
		return render(request, 'especialidade/form_especialidade.html', {'form_especialidade': form_especialidade})

@login_required()
def remover_especialidade(request,id):
		especialidade_bd = especialidades_service.listar_especialidades_id(id)
		if request.method=="POST":
				especialidades_service.remover_especialidade(especialidade_bd)
				return redirect('listar_especialidade')
		return render(request, 'especialidade/confirma_exclusao.html', {'especialidade': especialidade_bd})


# # @@@@@@@@@ Cidade @@@@@@@@@
# def listar_cidade(request):
# 		cidades = cidade_service.listar_cidade()
# 		return render(request, 'cidade/listar_cidade.html', {'cidades': cidades})
#
#
# def cadastrar_cidade(request):
# 		if request.method == "POST":
# 				form_cidade = CidadesForm(request.POST)
# 				if form_cidade.is_valid():
# 						nome_cidade = form_cidade.cleaned_data['nome_cidade']
# 						uf = form_cidade.cleaned_data['uf']
# 						form_cidade_nova = Cidade(nome_cidade=nome_cidade,uf=uf)
# 						cidade_service.cadastrar_cidade(form_cidade_nova)
# 						return redirect('listar_cidade')
# 		else:
# 				form_cidade = CidadesForm()
# 				return render(request, 'cidade/form_cidade.html', {'form_cidade': form_cidade})
#
# def editar_cidade(request, id):
# 		cidade_bd = cidade_service.listar_cidade_id(id)
# 		form_cidade = CidadesForm(request.POST or None, instance=cidade_bd)
# 		if form_cidade.is_valid():
# 				nome_cidade = form_cidade.cleaned_data['nome_cidade']
# 				uf = form_cidade.cleaned_data['uf']
# 				cidade_nova= Cidade(nome_cidade=nome_cidade,uf=uf)
# 				cidade_service.editar_cidade(cidade_bd, cidade_nova)
# 				return redirect('listar_cidade')
# 		return render(request, 'cidade/form_cidade.html', {'form_cidade': form_cidade})
#
# def remover_cidade(request, id):
# 		cidade_bd = cidade_service.listar_cidade_id(id)
# 		if request.method=='POST':
# 				cidade_service.remover_cidade(cidade_bd)
# 				return redirect('listar_cidade')
# 		return render(request, 'cidade/confirma_exclusao.html',{'cidade': cidade_bd})
#
#

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,render_to_response
from ..entidades.cidade import Cidade
from ..services import cidade_service
from ..forms.cidade_forms import CidadesForm, RawCidadesForm

@login_required()
def listar_cidade(request):
		cidades = cidade_service.listar_cidade()
		return render(request, 'cidade/listar_cidade.html', {'cidades': cidades})

@login_required()
def cadastrar_cidade(request):

		# my_form = RawCidadesForm(request.POST)
		# context = {
		# 		"form": my_form
		# }
		if request.method == "POST":
				form_cidade = RawCidadesForm(request.POST)

				if form_cidade.is_valid():
						nome_cidade = form_cidade.cleaned_data['nome_cidade']
						uf = form_cidade.cleaned_data['uf']
						form_cidade_nova = Cidade(nome_cidade=nome_cidade, uf=uf)
						cidade_service.cadastrar_cidade(form_cidade_nova)
						return redirect('listar_cidade')
		else:
				form_cidade = RawCidadesForm()
				return render(request, 'cidade/form_cidade.html', {'form_cidade': form_cidade})


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

# def editar_cidade(request, id):
# 		cidade_bd = cidade_service.listar_cidade_id(id)
#
# 		form_cidade = RawCidadesForm(request.POST or None)
# 		if form_cidade.is_valid():
# 				nome_cidade = form_cidade.cleaned_data['nome_cidade']
# 				uf = form_cidade.cleaned_data['uf']
# 				cidade_nova= Cidade(nome_cidade=nome_cidade,uf=uf)
# 				cidade_service.editar_cidade(cidade_bd, cidade_nova)
# 				return redirect('listar_cidade')
# 		return render(request, 'cidade/form_cidade.html', {'form_cidade': form_cidade})

@login_required()
def editar_cidade(request, id):

		cidade_bd = cidade_service.listar_cidade_id(id)
		form_cidade = CidadesForm(request.POST or None, instance=cidade_bd)
		if form_cidade.is_valid():
				nome_cidade = form_cidade.cleaned_data['nome_cidade']
				uf = form_cidade.cleaned_data['uf']
				cidade_nova= Cidade(nome_cidade=nome_cidade,uf=uf)
				cidade_service.editar_cidade(cidade_bd, cidade_nova)
				return redirect('listar_cidade')
		return render(request, 'cidade/form_cidade.html', {'form_cidade': form_cidade})

@login_required()
def remover_cidade(request, id):
		cidade_bd = cidade_service.listar_cidade_id(id)
		if request.method=='POST':
				cidade_service.remover_cidade(cidade_bd)
				return redirect('listar_cidade')
		return render(request, 'cidade/confirma_exclusao.html',{'cidade': cidade_bd})

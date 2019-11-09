from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

def index(request):
		if request.method == "POST":
				username = request.POST["username"]
				password = request.POST["password"]
				usuario = authenticate(request, username=username, password=password)
				if usuario is not None:
						login(request, usuario)
						return redirect('charts')
				else:
						messages.error(request, 'Usuário ou Senha incorretos')
						return redirect ('index') # voltar para a tela para que logue-se novamente
		else:
				form_login = AuthenticationForm()
				return render(request, 'home/index.html', {'form_login':form_login})

		
		
def teste(request):
		return render(request, 'teste/teste.html') # criando uma página para teste

def marcelo(request):
		# constroi um dicionario para passar ao template seu contexto
		# note que a chave 'msgnegrito' representa o {{ msgnegrito no template }}
		dicionario_contexto = {'msgnegrito': "Testando o fonte em negrito..."}
		return render(request, 'teste/marcelo.html', dicionario_contexto) # estou criando mais uma outra página de teste dentro do diretorio teste mesmo


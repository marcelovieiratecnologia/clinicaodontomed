from django.shortcuts import render
from django.http import HttpResponse

def index(request):
		return render(request, 'home/index.html')

def teste(request):
		return render(request, 'teste/teste.html') # criando uma página para teste

def marcelo(request):
		# constroi um dicionario para passar ao template seu contexto
		# note que a chave 'msgnegrito' representa o {{ msgnegrito no template }}
		dicionario_contexto = {'msgnegrito': "Testando o fonte em negrito..."}
		return render(request, 'teste/marcelo.html', dicionario_contexto) # estou criando mais uma outra página de teste dentro do diretorio teste mesmo


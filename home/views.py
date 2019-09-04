from django.shortcuts import render

def index(request):
		return render(request, 'home/index.html')

def teste(request):
		return render(request, 'teste/teste.html') # criando uma página para teste

def marcelo(request):
		return render(request, 'teste/marcelo.html') # estou criando mais uma outra página de teste dentro do diretorio teste mesmo


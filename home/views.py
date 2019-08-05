from django.shortcuts import render

def index(request):
		return render(request, 'home/index.html')

def teste(request):
		return render(request, 'teste/teste.html')

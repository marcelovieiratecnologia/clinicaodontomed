from django.shortcuts import render, get_object_or_404, render_to_response

# Create your views here.

def index(request):
		return render_to_response()


def listar_entrada_saida(request):
		return render(request, 'caixa/listar_entrada_saida.html')





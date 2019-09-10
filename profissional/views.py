from django.shortcuts import render, render_to_response
from .forms import ProfissionaisForm
# Create your views here.

def index(request):
		return render_to_response()

def cadastrar_profissional(request):
		form_profissional = ProfissionaisForm()
		return render(request, 'profissional/form_profissional.html', {'form_profissional':form_profissional})

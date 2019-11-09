from django.urls import path
from .views import *


urlpatterns = [
	path('', index, name='index'), # serve de Página Home e Logar Usuário no Sistema
	path('home/', index, name='index'), # serve de Página Home e Logar Usuário no Sistema
	# lê meu html dentro do template/teste/teste.html , na URLs principal do meu projeto eu dou um include na home.urls e é aqui que aponto para minha html teste e marcelo
	path('teste/', teste, name='teste'),
	path('marcelo/', marcelo, name='marcelo'),
]





# Dessa maneira preciso que esteja importado da seguinte maneira
# from . import views
# urlpatterns = [
# 	path('', index, name='index'),
# 	path('teste/', teste, name='teste'),
# 	path('marcelo/', marcelo, name='marcelo'),
# ]
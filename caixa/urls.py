from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
		path('listar_entrada_saida/',listar_entrada_saida, name='listar_entrada_saida'), # nesse primeiro o que eu escrever é o que rferencia ao link se deixar vazio no link sera apenas localhost:8000/caixa, nome do Método DEF da minha VIEW , Nome para a Rota(é o que aparece na URL)
]

from django.contrib import admin
from django.urls import path
from .views import *

'''
1- Rota que será envocada no link se deixar vazio no link sera apenas localhost:8000/caixa,
2- Nome do Método DEF da minha VIEW ,
3- NAME= É Nome para a Rota que no caso uso por exemplo no link do MENU do html... exemplo href="{% url 'listar_entrada_saida' %}"
'''

urlpatterns = [
		path('listar_entrada_saida/',listar_entrada_saida, name='listar_entrada_saida'),
		path('cadastrar_entrada_saida/',cadastrar_entrada_saida, name='cadastrar_entrada_saida'),
		path('editar_entrada_saida/<int:id>', editar_entrada_saida, name='editar_entrada_saida'), # <int:id> isso quer dizer que estou passando o parametro no qual meu metodo da view precisa
		path('remover_entrada_saida/<int:id>', remover_entrada_saida, name='remover_entrada_saida'), # <int:id> isso quer dizer que estou passando o parametro no qual meu metodo da view precisa
		path('listar_entrada_saida_data/', listar_entrada_saida_data, name='listar_entrada_saida_data'),
		path('listar_entrada_saida_anomes/', listar_entrada_saida_anomes, name='listar_entrada_saida_anomes'),
]

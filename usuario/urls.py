from django.contrib import admin
from django.urls import path
from .views import *


'''
1- Rota que será envocada no link se deixar vazio no link sera apenas localhost:8000/caixa,
2- Nome do Método DEF da minha VIEW ,
3- NAME= É Nome para a Rota que no caso uso por exemplo no link do MENU do html... exemplo href="{% url 'listar_entrada_saida' %}"
'''

urlpatterns = [
		path('usuario/',avatar, name='avatar'),
]

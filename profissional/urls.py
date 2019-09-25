from django.urls import path
from .views.profissional_views import *
from .views.cidade_views import *
from .views.especialidade_views import *


urlpatterns = [
		path('listar_profissional/', listar_profissional, name='listar_profissional'),
		path('cadastrar_profissional/', cadastrar_profissional, name='cadastrar_profissional'),
		path('editar_profissional/<int:id>', editar_profissional, name='editar_profissional'),
		path('remover_profissional/<int:id>', remover_profissional, name='remover_profissional'),
		path('cadastrar_cidade/', cadastrar_cidade, name='cadastrar_cidade'),
		path('listar_cidade/', listar_cidade, name='listar_cidade'),
		path('editar_cidade/<int:id>', editar_cidade, name='editar_cidade'),
		path('remover_cidade/<int:id>', remover_cidade, name='remover_cidade'),
		path('listar_especialidade/', listar_especialidade, name='listar_especialidade'),
		path('cadastrar_especialidade/', cadastrar_especialidade, name='cadastrar_especialidade'),
]




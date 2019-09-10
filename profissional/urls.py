from django.urls import path
from .views import *

urlpatterns = [
		path('cadastrar_profissional/', cadastrar_profissional, name='cadastrar_profissional'),
]




from django.urls import path
from .views import *


urlpatterns = [
	path('', index, name='index'),
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
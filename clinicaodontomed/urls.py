"""clinicaodontomed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [ # onde aponto meu APP e suas URLS que vai ser lida qdo eu digitar no browser
    path('admin/', admin.site.urls), # página do admin
    path('', include('home.urls')), # pág principal
    path('home/', include('home.urls')), # abre também a pág principal
    path('home/',include('home.urls')), # Apenas para teste , fiz dentro do Home(views - urls) os apontamentos e rotas, mas a página está em template/teste/
    path('caixa/', include('caixa.urls')),
]




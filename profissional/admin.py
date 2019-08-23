from django.contrib import admin
from .models import Profissionais, Especialidades

# Register your models here.



# Registrar o Model Junto ao Admin
admin.site.register(Profissionais)
admin.site.register(Especialidades)

from django.contrib import admin
from .models import Profissionais, Especialidades

# Register your models here.
class ProfissionaisAdmin(admin.ModelAdmin):
		#pass
		list_display = ['nome_profissional','cpf_profissional']


class EspecialidadesAdmin(admin.ModelAdmin):
		list_display = ['especialidade']


# Registrar o Model Junto ao Admin
admin.site.register(Profissionais, ProfissionaisAdmin)
admin.site.register(Especialidades, EspecialidadesAdmin)

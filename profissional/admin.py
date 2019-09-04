from django.contrib import admin
from .models import Profissionais, Especialidades, Cidades, OrgaoEmissor

# Register your models here.
class ProfissionaisAdmin(admin.ModelAdmin):
		#pass
		list_display = ['nome_profissional','cpf_profissional','num_registro_classe','orgao_emissor','cidades']


class EspecialidadesAdmin(admin.ModelAdmin):
		list_display = ['especialidade']


class CidadesAdmin(admin.ModelAdmin):
		list_display = ['nome_cidade', 'uf']


class OrgaoEmissorAdmin(admin.ModelAdmin):
		#pass
		list_display = ['ds_orgao_emissor','sg_orgao_emissor', '__str__']
		
		
# Registrar o Model Junto ao Admin
admin.site.register(Profissionais, ProfissionaisAdmin)
admin.site.register(Especialidades, EspecialidadesAdmin)
admin.site.register(Cidades, CidadesAdmin)
admin.site.register(OrgaoEmissor,OrgaoEmissorAdmin)
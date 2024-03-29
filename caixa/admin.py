from django.contrib import admin
from .models import EntradaSaida

from datetime import date

# Register your models here.
class EntradaSaidaAdmin(admin.ModelAdmin):
		#pass
		
		fields = [
								('tp_entrada'),
								('dt_movimentacao'),
								(
									#('profissional'), tirei para usar a FK
									('fkprofissional'),
									('fkespecialidades')
								),
								(
									('paciente')
								),
								(
									('motivo')
								),
								('tp_convenio','tp_pagamento','qt_parcelas','tp_porcentagem'),
								('tp_credito'),
								('valor_entr_saida'),
								('observacao')
							]
		search_fields = ['tp_entrada']
		list_filter = ['tp_entrada','dt_movimentacao']
		list_display = ['tp_entrada','dt_movimentacao','fkprofissional','fkespecialidades','paciente','motivo','tp_convenio','tp_pagamento','tp_credito','valor','desconto','total']
		list_display_links = ['tp_entrada','dt_movimentacao']
		#list_editable = ['motivo'] @@ Posso aqui colocar os campos que quero que fique editavél no Grid mesmo sem ter que entrar em modo de edição
		date_hierarchy = 'dt_movimentacao' #@@@ Ficou como se fosse um filtro em cima do Grid
		# save_on_top = True # Colocando os botões no topo da página tb
		radio_fields = {'tp_entrada': admin.HORIZONTAL} # assim o tp_entrada agora aparece não mais em um combobox mas sim como um radiobutton
		#prepopulated_fields = {'dt_movimentacao': date.today()} # .... tentando já preé preencher com a data do dia , tentar fazer isso.
		show_full_result_count = True # Mostra um Contador da pesquisa, quantidade que achou na pesquisa
		
		# forma de se chamar um js aqui no admin
		# class Media:
		# 		js = 'js/admin.js'
		# print(Media.js)

		# def queryset(self, request, queryset):
		# 		try:
		# 				qs = EntradaSaida


admin.site.site_header = 'Área Administrativa Clínica OdontoMed'
admin.site.index_title = 'Bem vindo a Área Administratica da Clinica OdontoMed'
# Exemplo para registrar um modelo junto ao admin
admin.site.register(EntradaSaida, EntradaSaidaAdmin)








from django.db import models
from localflavor.br.br_states import STATE_CHOICES


# Create your models here.

# class Estados(models.Model):
# 		ds_uf = models.CharField(verbose_name='Estados', max_length=42, blank=False, null=False)
# 		uf = models.CharField(verbose_name='UF', max_length=2, blank=False, null=False)
#
# 		class Meta:
# 				db_table = 'tb_om_estados'
# 				verbose_name='Estado'
# 				verbose_name_plural = 'Estados'
#
# 		def __str__(self):
# 				return self.uf

class OrgaoEmissor(models.Model):
		ds_orgao_emissor = models.CharField(verbose_name='Orgão Emissor', max_length=64, blank=False, null=False)
		sg_orgao_emissor = models.CharField(verbose_name='Sigla', max_length=15, blank=False, null=False)
		
		class Meta:
				db_table = 'tb_om_orgao_emissor'
				verbose_name = 'Orgão Emissor'
		# verbose_name_plural = ''
		
		def __str__(self):
				return self.sg_orgao_emissor + ' - ' + self.ds_orgao_emissor


class Especialidades(models.Model):
		# id_especialidade = models.IntegerField(primary_key=True, auto_created=True)
		especialidade = models.CharField(verbose_name='Especialidade', max_length=25, blank=False, null=False)
		
		class Meta:
				db_table = 'tb_om_especialidades'
				verbose_name = 'Especialidade'
				verbose_name_plural = 'Especialidades'
		
		def __str__(self):
				return self.especialidade


class Profissionais(models.Model):
		# id_profissional = models.IntegerField(primary_key=True, auto_created=True)
		nome_profissional = models.CharField(verbose_name='Nome do Profissional', max_length=60, blank=False, null=False)
		cpf_profissional = models.CharField(verbose_name='Número do CPF', max_length=14, blank=True,
																				null=True)  # validators=[validate_CNPJ])
		num_registro_classe = models.IntegerField(verbose_name='Reg Conselho da Classe (CRM/CRO/CORE...)', blank=True,
																							null=True)
		uf = models.CharField('UF', max_length=2, choices=STATE_CHOICES)
		# uf = models.ForeignKey("Estados", verbose_name='UF', related_name='qry_estados', blank=True, null=True, on_delete=models.CASCADE)  # Optei por usar o  STATE_CHOICES e não Uma tabela de UF : pip install django-localflavor
		
		orgao_emissor = models.ForeignKey("OrgaoEmissor",
																			verbose_name='Orgão Emissor',
																			related_name='qry_orgao_emissor',
																			blank=True,
																			null=True,
																			on_delete=models.CASCADE)
		especialidade = models.ManyToManyField('Especialidades',
																					 verbose_name='Especialidades',
																					 related_name='qry_especialidade')  # , on_delete=models.CASCADE)
		
		class Meta:
				db_table = 'tb_om_profissionais'
				verbose_name = 'Profissional'  # 'Entrada/Saída'
				verbose_name_plural = 'Profissionais'
		
		def __str__(self):
				return self.nome_profissional

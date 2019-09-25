from django.db import models
from localflavor.br.br_states import STATE_CHOICES
from django.db.models.signals import m2m_changed

# from joinfield.joinfield import JoinField

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


class Cidades(models.Model):
		nome_cidade = models.CharField('cidade',max_length=100)
		uf = models.CharField('UF', max_length=2, choices=STATE_CHOICES)
		
		class Meta:
				db_table = 'tb_om_cidades'
				ordering = ('nome_cidade',)
				verbose_name='Cidade'
				verbose_name_plural = 'Cidades'

		def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
				self.nome_cidade = self.nome_cidade.upper()
				self.uf = self.uf.upper()
				super(Cidades, self).save_base()

		def __str__(self):
				return self.nome_cidade + ' - ' + self.uf


class OrgaoEmissor(models.Model):
		ds_orgao_emissor = models.CharField(verbose_name='Orgão Emissor', max_length=64, blank=False, null=False)
		sg_orgao_emissor = models.CharField(verbose_name='Sigla', max_length=15, blank=False, null=False)
		
		class Meta:
				db_table = 'tb_om_orgao_emissor'
				verbose_name = 'Orgão Emissor'
				verbose_name_plural = 'Orgãos Emissores'
		
		def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
				self.ds_orgao_emissor = self.ds_orgao_emissor.upper()
				self.sg_orgao_emissor = self.sg_orgao_emissor.upper()
				super(OrgaoEmissor, self).save()
		
		def __str__(self):
				campo_concat = self.sg_orgao_emissor + ' - ' + self.ds_orgao_emissor #Um jeito que achei de criar um campo concatenado e levar ele junto para o admin fora os campos da tabela que já existem
				return campo_concat


class Especialidades(models.Model):
		# id_especialidade = models.IntegerField(primary_key=True, auto_created=True)
		especialidade = models.CharField(verbose_name='Especialidade', max_length=25, blank=False, null=False)
		
		class Meta:
				db_table = 'tb_om_especialidades'
				verbose_name = 'Especialidade'
				verbose_name_plural = 'Especialidades'
		
		def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
				self.especialidade = self.especialidade.upper()
				super(Especialidades, self).save()
				
		def __str__(self):
				return self.especialidade

#
# class ProfissionalEspecialidades(models.Model):
# 		profissionais_id = models.IntegerField(verbose_name='profissionais_id')
# 		especialidades_id = models.IntegerField(verbose_name='especialidades_id')
#
# 		class Meta:
# 				db_table = 'tb_om_profissionais_especialidade_detail'
# 				verbose_name = "Profissional Especialidades"
# 				# verbose_name_plural = "ss"
#

# 		def __str__(self):
# 				pass
#

class Profissionais(models.Model):
		# id_profissional = models.IntegerField(primary_key=True, auto_created=True)
		nome_profissional = models.CharField(verbose_name='Nome do Profissional', max_length=60, blank=False, null=False)
		cpf_profissional = models.CharField(verbose_name='Número do CPF', max_length=14, blank=True,null=True)  # validators=[validate_CNPJ])
		num_registro_classe = models.IntegerField(verbose_name='Num Conselho', blank=True,null=True)
		#uf = models.CharField('UF', max_length=2, choices=STATE_CHOICES)
		# uf = models.ForeignKey("Estados", verbose_name='UF', related_name='qry_estados', blank=True, null=True, on_delete=models.CASCADE)  # Optei por usar o  STATE_CHOICES e não Uma tabela de UF : pip install django-localflavor
		cidades = models.ForeignKey('Cidades', verbose_name='cidade', related_name='qry_cidades', null=True,on_delete=models.CASCADE)
		orgao_emissor = models.ForeignKey("OrgaoEmissor",
																			verbose_name='Orgão Emissor',
																			related_name='qry_orgao_emissores',
																			blank=True,
																			null=True,
																			on_delete=models.CASCADE)
		# especialidade = models.ManyToManyField('Especialidades',verbose_name='Especialidades',related_name='qry_profissionais')  # , on_delete=models.CASCADE)
		especialidades = models.ManyToManyField(Especialidades)
		#espec = JoinField(Especialidades, to_field = 'especialidade', on_delete=models.CASCADE, null=True) @@ testando essa Biblioteca joinfield , mas ele acabou desfazendo da minha tabela NxN , deixei queto por enquanto
		#especialidade_id = JoinField(Especialidades, on_delete=models.DO_NOTHING,db_column='especialidade_id', to_field='id')
		
		
		class Meta:
				db_table = 'tb_om_profissionais'
				verbose_name = 'Profissional'  # 'Entrada/Saída'
				verbose_name_plural = 'Profissionais'

		def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
				self.nome_profissional = self.nome_profissional.upper()
				super(Profissionais, self).save()
		
		def __str__(self):
				return self.nome_profissional

# def pre_save_especialidade_receiver(sender, instance, action, **kwargs):
# 		if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
# 				# especialidades = instance.especialidades.all()
# 				instance.save()
#
# m2m_changed.connect(pre_save_especialidade_receiver, sender=Profissionais.especialdiades.through)
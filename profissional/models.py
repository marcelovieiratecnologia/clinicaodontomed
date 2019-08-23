from django.db import models

# Create your models here.

class Especialidades(models.Model):
		#id_especialidade = models.IntegerField(primary_key=True, auto_created=True)
		especialidade = models.CharField(verbose_name='Especialidade', max_length=25, blank=False, null=False)
		
		
		class Meta:
				db_table='tb_om_especialidades'
				verbose_name = 'Especialidade'
				verbose_name_plural = 'Especialidades'
		
		def __str__(self):
				return self.especialidade


class Profissionais(models.Model):
		#id_profissional = models.IntegerField(primary_key=True, auto_created=True)
		nome_profissional = models.CharField(verbose_name='Nome do Profissional', max_length=60 , blank=False, null=False)
		cpf_profissional = models.CharField(verbose_name='Número do CPF', max_length=14, blank=True, null=True)  #validators=[validate_CNPJ])
		especialidade = models.ManyToManyField("Especialidades")
		
		class Meta:
				db_table='tb_om_profissionais'
				verbose_name = 'Profissional'#'Entrada/Saída'
				verbose_name_plural = 'Profissionais'

		def __str__(self):
				return self.nome_profissional
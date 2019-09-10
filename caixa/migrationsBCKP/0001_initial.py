# Generated by Django 2.2.3 on 2019-07-15 19:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaSaida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_movimentacao', models.DateField(blank=True, null=True)),
                ('profissional', models.CharField(max_length=150, verbose_name='Profissional')),
                ('paciente', models.CharField(max_length=150, verbose_name='Paciente')),
                ('qt_parcelas', models.IntegerField(default=0)),
                ('valor_entr_saida', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('tp_entrada', models.CharField(choices=[('ENTRADA', 'Entrada'), ('SAIDA', 'Saida')], max_length=10, verbose_name='Tipos de Entrada')),
                ('tp_convenio', models.CharField(choices=[('INTERODONTO', 'InterOdonto'), ('ODONTOPREV', 'OdontoPrev'), ('BRADESCO', 'Bradesco'), ('PARTICULAR', 'Particular')], max_length=30, verbose_name='Tipos de Convênios')),
                ('tp_pagamento', models.CharField(choices=[('CREDITO', 'Credito'), ('DEBITO', 'Debito'), ('DINHEIRO', 'Dinheiro')], max_length=30, verbose_name='Tipos de Pagamentos')),
                ('tp_credito', models.CharField(choices=[('APRAZO', 'APrazo')], max_length=20, verbose_name='Tipos de Créditos')),
                ('tp_porcentagem', models.CharField(choices=[('VALOR1', '0%'), ('VALOR2', '2,68%'), ('VALOR3', '7,07%'), ('VALOR4', '8,51%')], max_length=20, verbose_name='Tipos de Porcentagens')),
            ],
            options={
                'ordering': ['dt_movimentacao'],
            },
        ),
    ]

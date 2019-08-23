# Generated by Django 2.2.3 on 2019-08-20 16:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0026_auto_20190820_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradasaida',
            name='dt_movimentacao',
            field=models.DateField(default=datetime.datetime(2019, 8, 20, 13, 3, 53, 197388)),
        ),
        migrations.AlterField(
            model_name='entradasaida',
            name='fkprofissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profissionais', to='profissional.Profissionais', verbose_name='Profissional/Especialidade'),
        ),
    ]

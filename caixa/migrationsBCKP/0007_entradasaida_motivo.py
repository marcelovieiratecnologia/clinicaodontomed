# Generated by Django 2.2.3 on 2019-07-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0006_entradasaida_observacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='entradasaida',
            name='motivo',
            field=models.CharField(default='', max_length=150, verbose_name='Motivo para a Saída/Entrada'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.3 on 2019-08-31 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0032_auto_20190830_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradasaida',
            name='fkespecialidades',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profissional.Especialidades', verbose_name='Especialidades'),
        ),
    ]

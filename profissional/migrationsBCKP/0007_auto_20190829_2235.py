# Generated by Django 2.2.3 on 2019-08-30 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profissional', '0006_auto_20190827_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profissional',
            old_name='especialidade',
            new_name='especialidade_detail',
        ),
        migrations.AlterField(
            model_name='profissional',
            name='num_registro_classe',
            field=models.IntegerField(blank=True, null=True, verbose_name='Num Conselho'),
        ),
    ]

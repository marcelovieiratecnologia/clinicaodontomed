# Generated by Django 2.2.3 on 2019-08-22 00:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0027_auto_20190820_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradasaida',
            name='dt_movimentacao',
            field=models.DateField(default=datetime.datetime(2019, 8, 21, 21, 53, 23, 196949)),
        ),
    ]

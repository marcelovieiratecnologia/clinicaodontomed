# Generated by Django 2.2.3 on 2019-08-30 02:32

from django.db import migrations
import django.db.models.deletion
import joinfield.joinfield


class Migration(migrations.Migration):

    dependencies = [
        ('profissional', '0007_auto_20190829_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='profissional',
            name='espec',
            field=joinfield.joinfield.JoinField(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='profissional.Especialidades', to_field='especialidade'),
        ),
    ]
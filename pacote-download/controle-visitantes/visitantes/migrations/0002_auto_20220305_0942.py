# Generated by Django 3.0 on 2022-03-05 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitante',
            old_name='horario_autorizado',
            new_name='horario_autorizacao',
        ),
    ]
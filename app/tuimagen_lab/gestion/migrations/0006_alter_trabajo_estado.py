# Generated by Django 4.2.13 on 2024-06-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_alter_trabajo_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='estado',
            field=models.CharField(choices=[('EN_PROCESO', 'En proceso'), ('TERMINADO', 'Terminado')], default='EN_PROCESO', max_length=20),
        ),
    ]
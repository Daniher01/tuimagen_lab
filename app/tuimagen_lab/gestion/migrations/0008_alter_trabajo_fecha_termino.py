# Generated by Django 4.2.13 on 2024-06-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_trabajo_fecha_termino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='fecha_termino',
            field=models.DateField(null=True),
        ),
    ]
# Generated by Django 4.2.13 on 2024-06-10 22:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0006_alter_trabajo_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='fecha_termino',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
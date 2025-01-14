# Generated by Django 4.2.13 on 2024-06-11 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trabajos', '0002_alter_trabajo_fecha_termino'),
    ]

    operations = [
        migrations.CreateModel(
            name='EscaneoIntraoral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_escaneo', models.CharField(choices=[('superior', 'Superior'), ('inferior', 'Inferior'), ('ambos', 'Ambos'), ('hemiarcada', 'Hemiarcada')], max_length=20)),
                ('lugar_escaneo', models.CharField(max_length=255)),
                ('trabajo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trabajos.trabajo')),
            ],
        ),
    ]

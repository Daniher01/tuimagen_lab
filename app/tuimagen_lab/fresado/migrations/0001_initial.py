# Generated by Django 4.2.13 on 2024-06-11 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trabajos', '0002_alter_trabajo_fecha_termino'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrabajoFresado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_maquillaje', models.BooleanField(default=False)),
                ('trabajo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trabajos.trabajo')),
            ],
        ),
        migrations.CreateModel(
            name='Pieza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_pieza', models.CharField(choices=[('tipo1', 'Tipo 1'), ('tipo2', 'Tipo 2')], max_length=50)),
                ('material', models.CharField(choices=[('feldespato', 'Feldespato'), ('disilicato', 'Disilicato')], max_length=20)),
                ('bloque', models.CharField(max_length=255)),
                ('trabajo_fresado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='piezas', to='fresado.trabajofresado')),
            ],
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-20 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pastelero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_pasaporte', models.CharField(max_length=50)),
                ('pais_origen', models.CharField(max_length=50)),
                ('experiencia', models.FloatField(default=5)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empleado.empleados')),
            ],
        ),
    ]

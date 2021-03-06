# Generated by Django 3.2.9 on 2021-11-21 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Horno', '0001_initial'),
        ('Elaboracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.FloatField()),
                ('fechahora_inicio', models.DateTimeField()),
                ('fechahora_final', models.DateTimeField()),
                ('elaboracion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Elaboracion.elaboracion')),
                ('horno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Horno.horno')),
            ],
        ),
    ]

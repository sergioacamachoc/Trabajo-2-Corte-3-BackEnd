# Generated by Django 3.2.6 on 2021-11-23 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Solicitud', '0002_auto_20211120_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud',
            old_name='name',
            new_name='nameSolicitud',
        ),
    ]

# Generated by Django 2.2.4 on 2019-09-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hilo',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
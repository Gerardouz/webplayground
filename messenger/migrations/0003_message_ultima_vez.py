# Generated by Django 2.2.4 on 2019-09-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_hilo_fecha_actualizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='ultima_vez',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
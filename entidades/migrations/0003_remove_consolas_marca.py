# Generated by Django 5.0.6 on 2024-07-18 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0002_consolas_alter_juegos_de_mesa_cant_jugadores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consolas',
            name='marca',
        ),
    ]

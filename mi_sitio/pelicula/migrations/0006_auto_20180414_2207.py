# Generated by Django 2.0.3 on 2018-04-14 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelicula', '0005_pelicula_alquilada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='estreno',
            field=models.DateField(help_text='Ej: Dia/Mes/Año', null=True),
        ),
    ]

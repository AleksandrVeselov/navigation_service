# Generated by Django 4.2.5 on 2023-09-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0002_alter_gasstation_latitude_alter_gasstation_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='gas_stations',
            field=models.ManyToManyField(to='navigation.gasstation', verbose_name='Заправки маршрута'),
        ),
    ]

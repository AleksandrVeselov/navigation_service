# Generated by Django 4.2.5 on 2023-09-19 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0003_route_gas_stations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routegasstation',
            name='route',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='navigation.route', verbose_name='Маршрут'),
        ),
    ]
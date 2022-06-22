# Generated by Django 4.0.5 on 2022-06-22 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0003_remove_staff_position_staff_region_staff_station_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='region',
            field=models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='roads.region', verbose_name='Region'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-22 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0002_road_road_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='position',
        ),
        migrations.AddField(
            model_name='staff',
            name='region',
            field=models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='roads.region', verbose_name='Region'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='station',
            field=models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='roads.stations', verbose_name='Station'),
        ),
        migrations.AlterField(
            model_name='route',
            name='region_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roads.region', verbose_name='Region'),
        ),
    ]

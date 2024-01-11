# Generated by Django 4.2.9 on 2024-01-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_remove_tournament_locationlat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='location',
        ),
        migrations.AddField(
            model_name='tournament',
            name='locationLat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='locationLon',
            field=models.FloatField(null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-17 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='art_height',
            field=models.FloatField(default=200),
        ),
        migrations.AlterField(
            model_name='size',
            name='art_width',
            field=models.FloatField(default=200),
        ),
    ]
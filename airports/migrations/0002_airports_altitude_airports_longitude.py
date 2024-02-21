# Generated by Django 5.0.2 on 2024-02-21 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='airports',
            name='altitude',
            field=models.FloatField(default=123, verbose_name='Высота'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airports',
            name='longitude',
            field=models.FloatField(default=32, verbose_name='Долгота'),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2 on 2023-01-18 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bucketorderapp', '0002_auto_20230118_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courier',
            options={'verbose_name': 'Курьер', 'verbose_name_plural': 'Курьеры'},
        ),
        migrations.AlterModelOptions(
            name='flower',
            options={'verbose_name': 'Цветок', 'verbose_name_plural': 'Цветы'},
        ),
    ]
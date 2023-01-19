# Generated by Django 3.2 on 2023-01-19 06:20

from django.db import migrations, models


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
        migrations.AddField(
            model_name='bouquet',
            name='image',
            field=models.ImageField(blank=True, upload_to='bouquet_images/'),
        ),
    ]

# Generated by Django 3.2 on 2023-01-18 10:45

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('bucketorderapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='adress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='time',
            new_name='delievry_date',
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region=None, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='order',
            name='specialist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='bucketorderapp.specialist', verbose_name='Специалист'),
        ),
    ]

# Generated by Django 4.2.9 on 2024-01-12 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baankapp', '0004_customer_materials_provided'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.BooleanField(choices=[('M', 'Male'), ('F', 'Female')], default=False, max_length=1),
        ),
    ]

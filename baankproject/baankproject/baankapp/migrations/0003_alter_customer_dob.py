# Generated by Django 4.2.9 on 2024-01-12 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baankapp', '0002_remove_customer_materials_provided_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='DOB',
            field=models.CharField(max_length=100),
        ),
    ]

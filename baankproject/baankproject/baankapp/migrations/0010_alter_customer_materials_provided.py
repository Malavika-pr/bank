# Generated by Django 4.2.9 on 2024-01-12 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baankapp', '0009_alter_customer_account_type_alter_customer_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='materials_provided',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
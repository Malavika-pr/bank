# Generated by Django 4.2.9 on 2024-01-12 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baankapp', '0008_alter_customer_materials_provided'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='account_type',
            field=models.CharField(choices=[('Savings', 'Savings Account'), ('Current', 'Current Account')], default=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='customer',
            name='materials_provided',
            field=models.CharField(choices=[('credit_card', 'Credit card'), ('debit_card', 'Debit card'), ('cheque_book', 'Cheque book')], default=False, max_length=255),
        ),
    ]
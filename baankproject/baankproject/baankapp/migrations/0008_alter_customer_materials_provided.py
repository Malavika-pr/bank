# Generated by Django 4.2.9 on 2024-01-12 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baankapp', '0007_alter_customer_account_type_alter_customer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='materials_provided',
            field=models.CharField(choices=[('credit_card', 'Credit card'), ('debit_card', 'Debit card'), ('cheque_book', 'Cheque book')], default=False, max_length=120),
        ),
    ]
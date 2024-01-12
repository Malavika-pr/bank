from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=50, default=False)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    DOB = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=5, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default=False)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    account_type = models.CharField(max_length=20,
                                    choices=[('Savings', 'Savings Account'), ('Current', 'Current Account')],
                                    default=False)

    def __str__(self):
        return self.name

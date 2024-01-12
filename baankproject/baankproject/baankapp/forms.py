from django import forms
from .models import Customer, Material


class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'DOB', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'account_type']

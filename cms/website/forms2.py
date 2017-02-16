from django import forms

from website.models import User

import hashlib


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
        labels = {
            'emal': 'Email:',
            'password': 'Password:',
            'first_name': 'First name:',
            'last_name': 'Last name:'
        }
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_password(self):
        password = hashlib.sha512(self.cleaned_data['password'].encode())\
                          .hexdigest()
        return password

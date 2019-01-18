from django import forms
from django.contrib.auth.models import User

from .models import Person


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('about', )

    def clean_about(self):
        return self.cleaned_data['about'] or ''

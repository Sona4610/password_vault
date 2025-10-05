from django import forms
from .models import Credential

class CredentialForm(forms.ModelForm):
    class Meta:
        model = Credential
        fields = ['app_name', 'username', 'password', 'url']


from django import forms
from server.models import server

class ServerForm(forms.ModelForm):
    class Meta:
        model = server
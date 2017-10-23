from django import forms
from .models import *


class messageForm(forms.ModelForm):
    mesaj= forms.CharField(widget=forms.Textarea(attrs={'class':'messageInput'}),label=None)


from django import forms
from .models import *


class messageForm(forms.ModelForm):
    yazan = forms.CharField(max_length=400)
    mesaj= forms.CharField(widget=forms.Textarea())


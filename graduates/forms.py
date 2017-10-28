from django import forms
from .models import *


class messageForm(forms.Form):
    mesaj = forms.CharField(widget=forms.Textarea(attrs={'class':'messageInput'}),label='Mesajınızı Yazın:')





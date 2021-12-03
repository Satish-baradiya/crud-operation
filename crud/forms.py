from django import forms
from django.db import models
from django.forms import fields
from .models import Data


class DataForm(forms.ModelForm):
    
    class Meta:
        model = Data
        fields ="__all__"

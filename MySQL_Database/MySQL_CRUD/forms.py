from django import forms
from .models import RegisterFrom

class MyRegisterForm(forms.ModelForm):
    class Meta:
        model=RegisterFrom
        fields=["name","age","address","contact","email"]
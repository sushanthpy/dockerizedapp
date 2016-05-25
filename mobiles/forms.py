"""
Forms for the mobiles app.
"""
from django import forms
from mobiles.models import Mobile


class MobileForm(forms.ModelForm):
    """Form for the Car model."""
    class Meta:
        model = Mobile
        fields = '__all__'

"""
Forms for the mobiles app.
"""
from django import forms
from mobiles.models import Mobile


class MobileForm(forms.ModelForm):
    """Form for the Car model."""
    class Meta(object):
        model = Mobile
        fields = '__all__'

from dataclasses import field
from django import forms


class contactForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=250)
    massage = forms.CharField(widget=forms.Textarea)

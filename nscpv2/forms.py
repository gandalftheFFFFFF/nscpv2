__author__ = 'niels'

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', })
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', })
    )
    cc = forms.BooleanField(
        label = 'Receive copy?',
        required=False,
    )
    subject = forms.CharField(
        label='Subject',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', })
    )
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', }))
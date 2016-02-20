from django import forms


class SearchForm(forms.Form):
    terms = forms.CharField(
        label='Search',
        max_length=200,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Search for projects',
                'required': 'true',
            }
        ),
    )
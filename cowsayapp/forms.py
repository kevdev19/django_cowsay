from django import forms

from cowsayapp.models import InputHistory


class InputForm(forms.Form):
    capture_text = forms.CharField(max_length=100)

from django import forms


class InputForm(forms.Form):
    capture_text = forms.CharField(max_length=100)

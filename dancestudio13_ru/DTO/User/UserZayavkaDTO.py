from django import forms

class UserZayavkaDTO(forms.Form):
    name = forms.CharField(max_length=256, required=True)
    phone = forms.CharField(max_length=256, required=True)
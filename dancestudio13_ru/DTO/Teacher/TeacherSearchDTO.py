from email.policy import default
from django import forms

class TeacherSearchDTO(forms.Form):
    offset = forms.IntegerField(required=False)
    limit = forms.IntegerField(max_value=18, required=False)
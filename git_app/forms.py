from django import forms
from git_app.models import UserName

class user(forms.ModelForm):
    class Meta():
        model=UserName
        fields='__all__'

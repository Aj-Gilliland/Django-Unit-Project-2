from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class adminDeleteForm(forms.Form):
    type = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    index = forms.IntegerField()

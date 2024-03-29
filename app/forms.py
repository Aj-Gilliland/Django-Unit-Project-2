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

class reportForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    prompt = forms.CharField(label='Leave your bugs here', widget=forms.Textarea(attrs={'class': 'form-control'}))

class pfpChangeForm(forms.Form):
    picture = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}), label='Select Profile Picture', required=True)

class messageForm(forms.Form):
    message = forms.CharField(max_length=254, required=True)
    report_id = forms.CharField(max_length=254, widget=forms.HiddenInput())

class escalateMessageForm(forms.Form):
    message_id = forms.CharField(max_length=254, widget=forms.HiddenInput())
    report_id = forms.CharField(max_length=254, widget=forms.HiddenInput())
from django import forms
from .models import Like, WebsiteModel
from django.contrib.auth.models import User


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(label="Enter your User Name")
    password = forms.CharField(label="Enter Password")


class WebsiteForm(forms.ModelForm):
    class Meta:
        model = WebsiteModel
        fields = ['url', 'user']
        total_likes = forms.IntegerField(
            required=False, widget=forms.HiddenInput())
        total_dislikes = forms.IntegerField(
            required=False, widget=forms.HiddenInput())

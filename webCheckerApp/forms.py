from django import forms
from .models import WebsiteModel,User,Like


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = WebsiteModel
        fields = '__all__'

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = '__all__'

class LoginForm(forms.Form):
    email = forms.EmailField(label="Enter your Email")
    password = forms.CharField(label="Enter Password")
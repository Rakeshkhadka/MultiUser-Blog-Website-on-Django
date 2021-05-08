from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


from .models import Posts


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields ='__all__'

        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
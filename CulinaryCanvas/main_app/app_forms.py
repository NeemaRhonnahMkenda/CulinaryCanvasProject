from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from main_app.models import Recipe


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        exclude = ['user']

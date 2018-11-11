from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

UserModel = get_user_model()

class RegisterForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

class EditProfileForm(UserChangeForm):

    class Meta:
        model = UserModel
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        ]

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username']

    def save(self, commit=True):
        username = self.cleaned_data['username']
        self.instance.username = username
        self.instance.save()
        return self.instance


class UserRegisterForm(ModelForm):
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    error_messages = {
        "password_mismatch": "The two password fields didn’t match.",
        "username_exists": "User with this username already exists."
    }

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                self.error_messages["username_exists"],
                code="username_exists",
            )
        return username

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )

    def save(self, commit=True):
        password = self.cleaned_data['password1']
        instance = super(UserRegisterForm, self).save(commit)
        instance.set_password(password)
        instance.save()
        return instance

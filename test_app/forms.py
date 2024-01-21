from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import UrlUser


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Имя пользователя')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())
    email = forms.EmailField(label='E-mail')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UrlForm(forms.ModelForm):
    url_name = forms.URLField(label="Введите ссылку", widget=forms.widgets.URLInput())

    class Meta:
        model = UrlUser
        fields = ('url_name',)

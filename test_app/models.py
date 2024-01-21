from django.contrib.auth.models import User
from django.db import models


class UrlUser(models.Model):
    url_name = models.CharField(max_length=150, verbose_name='Длинный урл')
    short_url = models.CharField(max_length=150, verbose_name='Короткий урл')
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')

    @classmethod
    def create(cls, url_name, short_url, username):
        obj = cls(url_name=url_name, short_url=short_url, username=username)
        return obj

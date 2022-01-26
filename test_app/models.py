from django.contrib.auth.models import User
from django.db import models


# Create your models here.


# class ShortUrl(models.Model):
#     short_url = models.URLField()
#     username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
#
#
# class UrlUser(models.Model):
#     url_name = models.URLField(verbose_name='Длинный урл')
#     username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')

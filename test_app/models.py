from django.contrib.auth.models import User
from django.db import models


class UrlUser(models.Model):
    url_name = models.CharField(max_length=150, verbose_name='Длинный урл')
    short_url = models.CharField(max_length=150, verbose_name='Короткий урл')
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')

    @classmethod
    def create(cls, url_name, short_url, username):
        stas = cls(url_name=url_name, short_url=short_url, username=username)
        return stas

def generacion(request):
    z = UrlUser.objects.all()
    x = []
    for i in range(len(z)):
        s = pyshorteners.Shortener().tinyurl.short(z[i].url_name)
        x.append(s)
        print(s)
        talk = UrlUser.create(s)
        talk.save()
        print(talk)
    #    w = UrlUser.create(short_url=s)

    stas = UrlUser.objects.all()
    context = {'x': x, 'stas':stas}
    return render(request, 'test_app/all_short_url.html', context)
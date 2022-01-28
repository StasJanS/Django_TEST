from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
import pyshorteners as pyshorteners
# Create your views here.
from .forms import UserLoginForm, UserRegisterForm, UrlForm
from .models import UrlUser


def index(request):
    if request.method == 'POST':
        storm = UrlForm(request.POST)
        if storm.is_valid():
            storm.save()
            redirect('all_short_url')
    else:
        storm = UrlForm()
    context = {'storm': storm}

    return render(request, 'test_app/index.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'test_app/login.html', context)


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'test_app/register.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')


def all_short_url(request):
    z = UrlUser.objects.filter(username=request.user)
    context = {'z': z}
    return render(request, 'test_app/all_short_url.html', context)


def del_file(request):
    del_z = UrlUser.objects.filter(username=request.user).delete()
    context = {'del_z': del_z}
    return render(request, 'test_app/all_short_url.html', context)


def generacion(request):
    z = UrlUser.objects.all()
    x = []
    for i in range(len(z)):
        s = pyshorteners.Shortener().tinyurl.short(z[i].url_name)
        x.append(s)
        print(s)
    #    w = UrlUser.create(short_url=s)
    stas = UrlUser.objects.all()
    context = {'x': x, 'stas':stas}
    return render(request, 'test_app/all_short_url.html', context)

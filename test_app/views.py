from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
import pyshorteners as pyshorteners
from .forms import UserLoginForm, UserRegisterForm, UrlForm
from .models import UrlUser


def index(request):
    talk = ""
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            talk = pyshorteners.Shortener().tinyurl.short(form.cleaned_data['url_name'])
            obj_url = UrlUser.create(url_name=form.cleaned_data['url_name'], short_url=talk, username=request.user)
            obj_url.save()
            redirect('all_short_url')
    else:
        form = UrlForm()
    context = {'form': form, 'talk': talk}
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
    user_urls = UrlUser.objects.filter(username=request.user)
    return render(request, 'test_app/all_short_url.html', {'user_urls': user_urls})


def del_file(request):
    UrlUser.objects.filter(username=request.user).delete()
    return render(request, 'test_app/all_short_url.html')


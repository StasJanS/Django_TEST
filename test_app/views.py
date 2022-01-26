from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
import pyshorteners as pyshorteners
# Create your views here.
from .forms import UserLoginForm, UserRegisterForm


def index(request):
    # if request.method == 'POST':
    #     storm = UrlShUrl(request.POST)
    #     if storm.is_valid():
    #         ShortUrl.objects.create(short_url=pyshorteners.Shortener().tinyurl.short(storm))
    #         print(storm)
    #         storm.save()
    #         # s = pyshorteners.Shortener()
    #         # ShortUrl.objects.create(url_name=s.tinyurl.short(storm))
    #         redirect('index')
    # else:
    #     storm = UrlShUrl()
    # context = {'storm': storm}
    return render(request, 'test_app/index.html')


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
    return render(request, 'test_app/all_short_url.html')

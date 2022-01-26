import pyshorteners as pyshorteners

link = input('Введите ссылку которую желаете сократить: ')
s = pyshorteners.Shortener()
print(s.tinyurl.short(link))


def index_one(request):
    auto = Car.objects.all()
    form = GetPost()
    if request.method == 'POST':
        form = GetPost(request.POST)
        if form.is_valid():
            form.save()
    context = {'auto': auto, 'menu': menu, 'form': form}
    return render(request, 'one/index.html', context)
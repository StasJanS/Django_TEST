import pyshorteners as pyshorteners

link = input('Введите ссылку которую желаете сократить: ')
s = pyshorteners.Shortener()
print(s.tinyurl.short(link))


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()
    return HttpResponseRedirect("/")
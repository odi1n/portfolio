from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Перейти в <a href='/admin'>Админ-панель</a>")
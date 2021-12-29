from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from ..forms import LoginForm
from ..models import CustomUser


def user_login(request):
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'registration/login.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                if CustomUser.objects.filter(username=cd['username']).exists() is False:
                    form.errors["username"] = {"Проверьте логин"}
                form.errors["password"] = {"Проверьте пароль"}
                return render(request, "registration/login.html", {"form": form})

    return render(request, 'registration/login.html', {'form': form})
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login

from ..forms import SignupForm
from ..models import CustomUser


class SignupView(View):
    model = CustomUser
    template_name = "registration/signup.html"

    def get(self, *args, **kwargs):
        if self.request.user == AnonymousUser():
            user_form = SignupForm()
            return render(self.request, 'registration/signup.html', {'user_form': user_form})
        else:
            return redirect('/')

    def post(self, *args, **kwargs):
        user_form = SignupForm(self.request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.username = user_form.data['username']
            user.set_password(user_form.data['password'])
            user.save()
            login(self.request, user)
            return redirect('/')
        return render(self.request, 'registration/signup.html', {'user_form': user_form})

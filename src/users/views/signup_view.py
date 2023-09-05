from typing import Any, Union

from django.contrib.auth import login
from django.contrib.auth.models import AnonymousUser
from django.http import (
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect, render
from django.views import View

from ..forms import SignupForm
from ..models import CustomUser


class SignupView(View):
    model = CustomUser
    template_name = "registration/signup.html"

    def get(
        self, *args: Any, **kwargs: Any
    ) -> Union[HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect]:
        if self.request.user == AnonymousUser():
            return render(self.request, self.template_name, {"user_form": SignupForm()})
        return redirect("/")

    def post(
        self, *args: Any, **kwargs: Any
    ) -> Union[HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect]:
        user_form = SignupForm(self.request.POST)
        if user_form.is_valid() is False:
            return render(self.request, self.template_name, {"user_form": user_form})

        user = user_form.save()
        user.username = user_form.data["username"]
        user.set_password(user_form.data["password"])
        user.save()
        login(self.request, user)
        return redirect("/")

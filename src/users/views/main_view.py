from typing import Any, Union

from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from ..forms import ProfileForm
from ..models import CustomUser


class MainView(View):
    template_name = "profile.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        post = get_object_or_404(CustomUser, pk=request.user.id)
        profile_form = ProfileForm(instance=post)
        return render(self.request, self.template_name, {"forms": profile_form})

    def post(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> Union[HttpResponsePermanentRedirect, HttpResponseRedirect]:
        forms = ProfileForm(request.POST)
        if forms.is_valid():
            user = CustomUser.objects.filter(id=request.user.id).first()
            user.first_name = forms.cleaned_data["first_name"]
            user.last_name = forms.cleaned_data["last_name"]
            user.middle_name = forms.cleaned_data["middle_name"]
            user.sex = forms.cleaned_data["sex"]
            user.age = forms.cleaned_data["age"]
            user.save()
        return redirect("profile")

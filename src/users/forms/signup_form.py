from django import forms

from ..models import CustomUser


class SignupForm(forms.ModelForm):
    username = forms.CharField(
        label="Логин",
        required=True,
        min_length=5,
        max_length=20,
        widget=forms.TextInput(attrs={"placeholder": "Логин", "class": "form-control"}),
    )
    password = forms.CharField(
        label="Пароль",
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
            }
        ),
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
            }
        ),
    )

    class Meta:
        model = CustomUser
        fields = ("username",)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd["password2"]

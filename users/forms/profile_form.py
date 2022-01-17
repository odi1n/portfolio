from django import forms

from ..models import CustomUser


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя",
                                 required=True,
                                 min_length=2,
                                 max_length=20,
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'Иван',
                                     'class': 'form-control'
                                 }))
    last_name = forms.CharField(label="Фамилия",
                                required=True,
                                min_length=2,
                                max_length=20,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Иванович',
                                    'class': 'form-control'
                                }))
    middle_name = forms.CharField(label="Отчество",
                                  required=True,
                                  min_length=2,
                                  max_length=20,
                                  widget=forms.TextInput(attrs={
                                      'placeholder': 'Иванов',
                                      'class': 'form-control'
                                  }))

    class Meta:
        model = CustomUser
        fields = ('last_name', 'first_name', 'middle_name')

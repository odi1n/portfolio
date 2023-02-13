from django import forms

from ..models import CustomUser
from ..models.type import SexType


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
    sex = forms.CharField(label="Пол",
                          widget=forms.Select(attrs={
                              'class': 'form-control'
                          }, choices=SexType.choices))
    age = forms.CharField(label="Возраст",
                          widget=forms.NumberInput(attrs={
                              'class': 'form-control',
                              'type': 'number'
                          }))

    class Meta:
        model = CustomUser
        fields = ('last_name', 'first_name', 'middle_name', 'sex', 'age')

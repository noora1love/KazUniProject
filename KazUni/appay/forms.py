from django import forms
from .models import ModelPays


class ModelPaysForm(forms.ModelForm):
    class Meta:
        model = ModelPays
        fields = ('title','typeofoperation','typeofpay','organization','bankcard','countrparty','dateofstart','dateofend', 'comments')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'title',
                'type': 'text',
                'placeholder': 'Введите Название'
            }),
            'typeofoperation': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'title',
                'type': 'text',
                'placeholder': 'Введите Название'
            }),
            'typeofpay': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'title',
                'type': 'text',
                'placeholder': 'Введите Название'
            }),
            'organization': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'title',
                'type': 'text',
                'placeholder': 'Введите Название'
            }),
            'bankcard': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'title',
                'type': 'text',
                'placeholder': 'Введите Название'
            }),
            'countrparty': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'title',
                'type': 'text',
                'placeholder': 'Введите Название'
            }),
            'dateofstart': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'title',
                'type': 'text',
                'placeholder': 'Введите Название'
            }),
            'comments': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'title',
                'type': 'text',
                'placeholder': 'Введите Название'
            }),
        }

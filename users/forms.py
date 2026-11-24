from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
import re


class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=False, help_text='Необязательное поле. Введите ваш номер телефона.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return phone



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'tg_name', 'avatar', 'country')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError('Этот email уже занят другим пользователем.')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not re.fullmatch(r'\+?\d{7,15}', phone.replace(' ', '')):
            raise forms.ValidationError('Введите номер в формате +79991234567.')
        return phone


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField(
    label='',
		required=True,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
  )
  username = forms.CharField(
    label='',
		required=True, 
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Login'})
  )
  first_name = forms.CharField(
    label='',
		required=True,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Имя'})
  )
  last_name = forms.CharField(
    label='',
		required=True,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Фамилию'})
  )
  address = forms.CharField(
    label='',
		required=True,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Адрес'})
  )
  phone_number = forms.CharField(
    label='',
		required=True,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'})
  )
  password1 = forms.CharField(
    label='',
    required=True, 
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
  )
  password2 = forms.CharField(
    label='',
		required=True, 
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'})
  )

  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'address', 'phone_number']

  def save(self, commit=True):
    user = super().save(commit=False)
    user.email = self.cleaned_data['email']
    user.first_name = self.cleaned_data['first_name']
    user.last_name = self.cleaned_data['last_name']
    if commit:
      user.save()
      profile, created = Profile.objects.get_or_create(
        user=user,
        defaults={
          'first_name': self.cleaned_data['first_name'],
          'last_name': self.cleaned_data['last_name'],
          'address': self.cleaned_data['address'],
          'phone_number': self.cleaned_data['phone_number']
        }
      )
    return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Login'})
    )
    first_name = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Имя'})
    )
    last_name = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Фамилию'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    address = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Адрес'})
    )
    phone_number = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'})
    )

    class Meta:
        model = Profile
        fields = ['address', 'phone_number']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Изменить фото',
        required=False,
        widget=forms.FileInput,
    )

    class Meta:
        model = Profile
        fields = ['img']

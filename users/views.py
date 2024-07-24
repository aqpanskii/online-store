from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Пользователь {username} был успешно создан!')
			return redirect('home-page')
	else: 
		form = UserRegisterForm()
	return render(
		request, 
		'users/registration.html', 
		{
			'title': 'Регистрация',
			'form': form
		}
		)

@login_required
def profile(request):
	if request.method == "POST":
		profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
		updateUserForm = UserUpdateForm(request.POST, instance=request.user)
		updateProfileForm = ProfileUpdateForm(request.POST, instance=request.user.profile)

		if profileForm.is_valid() and updateUserForm.is_valid() and updateProfileForm.is_valid():
			updateUserForm.save()
			updateProfileForm.save()
			profileForm.save()
			messages.success(request, f'Ваш аккаунт был успешно обновлен!')
			return redirect('profile')
	else:
		profileForm = ProfileImageForm(instance=request.user.profile)
		updateUserForm = UserUpdateForm(instance=request.user)
		updateProfileForm = ProfileUpdateForm(instance=request.user.profile)

	data = {
		'profileForm': profileForm,
		'updateUserForm': updateUserForm,
		'updateProfileForm': updateProfileForm
	}
	return render(request, 'users/profile.html', data)

@login_required
def settings(request):
	if request.method == "POST":
		profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
		updateUserForm = UserUpdateForm(request.POST, instance=request.user)
		updateProfileForm = ProfileUpdateForm(request.POST, instance=request.user.profile)

		if profileForm.is_valid() and updateUserForm.is_valid() and updateProfileForm.is_valid():
			updateUserForm.save()
			updateProfileForm.save()
			profileForm.save()
			messages.success(request, f'Ваш аккаунт был успешно обновлен!')
			return redirect('profile')
	else:
		profileForm = ProfileImageForm(instance=request.user.profile)
		updateUserForm = UserUpdateForm(instance=request.user)
		updateProfileForm = ProfileUpdateForm(instance=request.user.profile)

	data = {
		'profileForm': profileForm,
		'updateUserForm': updateUserForm,
		'updateProfileForm': updateProfileForm
	}
	return render(request, 'users/settings.html', data)
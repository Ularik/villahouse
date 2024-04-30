from django.contrib.auth import get_user_model, logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm
User = get_user_model()
from pprint import pprint


def user_register_view(request):
    if request.method == 'POST':
        pprint(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            print(form.cleaned_data)
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)
            login(request, user)
            return redirect('index')
        else:
            print(form.errors)

    form = UserRegisterForm()

    return render(request, 'user/add_user.html', context={'form': form})


def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user:
                login(request, user)
                return redirect('index')
    form = UserLoginForm()

    return render(request, 'user/login.html', context={'form': form})


@login_required(login_url='/user/login/')
def user_logout_view(request):
    logout(request)
    return redirect('index')


def user_profile_view(request):
    # if not request.user.is_authenticated:
    #     return redirect('register')

    user = User.objects.filter(pk=request.user.id).first()
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
        return redirect('profile')
    form = UserUpdateForm(instance=user)

    return render(request, 'user/profile.html', context={"user": user, "form": form})
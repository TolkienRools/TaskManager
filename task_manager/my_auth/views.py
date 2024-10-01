from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm

class LoginView(View):
    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, 'my_auth/login.html', {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard/list/')
        return render(request, 'my_auth/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('my_auth:login')

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'my_auth/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/dashboard/list/')  # Замените 'home' на ваше целевое представление
        return render(request, 'my_auth/register.html', {'form': form})

# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()       # foydalanuvchini bazaga yozadi
            login(request, user)     # avtomatik kiritadi
            return redirect('bosh')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        # AuthenticationForm — username va parolni tekshiradi
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()   # tekshirilgan foydalanuvchini oladi
            login(request, user)     # sessionga yozadi
            return redirect('bosh')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    # Chiqish faqat POST orqali — xavfsizlik uchun
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return redirect('bosh')
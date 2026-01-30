from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Student


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        roll_no = request.POST.get('roll_no')
        branch = request.POST.get('branch')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        Student.objects.create(
            user=user,
            roll_no=roll_no,
            branch=branch
        )

        messages.success(request, "Registration successful. Please login.")
        return redirect('login')

    return render(request, 'accounts/register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)

            return redirect('exam_list')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')

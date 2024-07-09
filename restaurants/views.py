from restaurants.models import Restaurant, Food #引入model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def menu(request): #新增
    restaurant_list = Restaurant.objects.all()
    food_list = Food.objects.all()
    return render(request, 'menu.html',locals())

def home(request):
    return render(request , 'home.html',locals())

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('menu')  # 重定向到menu
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')  # 重定向到主页或其他页面
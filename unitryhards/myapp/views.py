from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = '/login'

# Hello View
def hello_view(request):
    return HttpResponse("Hello, welcome to UniTryhards!")

# Sign Up View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user without authentication
            login(request, user)  # Log the user in directly after creation
            return redirect('hello')  # Redirect to the 'hello' page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log in the user after successful authentication
            return redirect('hello')  # Redirect to the 'hello' page after successful login
        else:
            return HttpResponse("Invalid login credentials")  # Display error message for invalid login
    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('hello')  # Redirect to the 'hello' page after logging out

@login_required
def profile_view(request):
    return render(request, 'profile.html')
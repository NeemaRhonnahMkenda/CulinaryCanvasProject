from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from main_app.app_forms import CreateUserForm, RecipeForm
from main_app.models import Recipe


# Create your views here.
def home(request):
    return render(request, 'index.html', {'user': request.user})


def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for  {user} !')
            return redirect('login')

    else:
        form = CreateUserForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Log the user in
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def profile(request):
    return render(request, 'profile.html', {'user': request.user})


def signout(request):
    logout(request)
    return redirect('home')


def category(request):
    recipes = Recipe.objects.all()  # Retrieve all recipes from the database
    return render(request, 'category.html', {'user': request.user, 'recipes': recipes})


@login_required(login_url='login')
def blogPostEntry(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            # Set the user before saving the form
            form.instance.user = request.user
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'blogPostEntry.html', {'form': form, 'user': request.user})
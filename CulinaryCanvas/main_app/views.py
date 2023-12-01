from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from main_app.app_forms import CreateUserForm, RecipeForm, SearchForm
from main_app.models import Recipe


# Create your views here.
def home(request):
    all_recipes = Recipe.objects.all()
    return render(request, 'index.html', {'user': request.user, 'all_recipes': all_recipes})


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
    user_recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'profile.html', {'user': request.user, 'user_recipes': user_recipes})


def delete_post(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id, user=request.user)
    recipe.delete()
    messages.warning(request, "Post is permanently deleted!")
    return redirect('profile')


def signout(request):
    logout(request)
    return redirect('home')


def category(request):
    recipes = Recipe.objects.all()  # Retrieve all recipes from the database
    latest_recipes = Recipe.objects.order_by('-created_at')[:4]
    unique_categories = Recipe.objects.values_list('category', flat=True).distinct()
    return render(request, 'category.html', {'user': request.user, 'recipes': recipes, 'latest_recipes': latest_recipes,
                                             'unique_categories': unique_categories})


@login_required(login_url='login')
def blogPostEntry(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'blogPostEntry.html', {'form': form, 'user': request.user})


def blogSingle(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    latest_recipes = Recipe.objects.order_by('-created_at')[:4]
    return render(request, 'blog-single.html',
                  {'user': request.user, 'recipe': recipe, 'latest_recipes': latest_recipes})


def edit_recipes(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, "Post Updated Successfully!")
            return redirect('profile')  # Redirect to the user's profile or any other appropriate page
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'edit_recipes.html', {'form': form, 'recipe': recipe})


def search_view(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        # Split the query into individual words
        search_words = query.split()

        # Create a Q object to combine queries for each word
        q_objects = Q()

        # Add a condition for each word in the search query
        for word in search_words:
            q_objects |= (
                    Q(recipe_title__icontains=word) |
                    Q(recipe_description__icontains=word) |
                    Q(category__icontains=word)
            )

        # Use the Q object in the filter to get recipes containing any of the words
        results = Recipe.objects.filter(q_objects)

    return render(request, 'search.html', {'form': form, 'results': results})

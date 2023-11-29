from django.contrib import admin

from main_app.models import Recipe


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_title', 'category', 'created_at', 'user')
    search_fields = ('recipe_title', 'user__username')  # Enable searching by recipe title and username
    list_filter = ('category', 'created_at', 'user')  # Enable filtering by category, timestamp, and user

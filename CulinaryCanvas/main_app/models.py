import os.path
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def unique_img_name(instance, filename):
    name = uuid.uuid4()
    print(name)
    ext = filename.split(".")
    full_name = f"{name}.{ext}"

    return os.path.join('Recipes_images', full_name)


class Recipe(models.Model):
    BAKED = 'Baked'
    BOILED = 'Boiled'
    FRIED = 'Fried'

    CATEGORY_CHOICES = [
        (BAKED, 'Baked'),
        (BOILED, 'Boiled'),
        (FRIED, 'Fried'),
    ]

    recipe_title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=BAKED)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to=unique_img_name, null=True, default='Recipes_images/default.jpeg')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe_title

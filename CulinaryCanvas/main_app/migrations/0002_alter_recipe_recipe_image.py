# Generated by Django 4.2.7 on 2023-11-29 10:54

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="recipe_image",
            field=models.ImageField(
                null=True, upload_to=main_app.models.unique_img_name
            ),
        ),
    ]
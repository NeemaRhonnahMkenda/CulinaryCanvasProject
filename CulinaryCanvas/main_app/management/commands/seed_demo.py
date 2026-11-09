"""
python manage.py seed_demo

Fills an empty database with original demo recipes so the live site isn't blank.
Safe to run more than once: recipes that already exist (by title) are skipped.
The demo author account has no usable password, so nobody can log in as it.
"""
import json
from pathlib import Path

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from main_app.models import Recipe

SEED = Path(__file__).resolve().parents[2] / "seed" / "recipes.json"


def _find_photo(hint: str):
    """Find an existing photo in media/Recipes_images whose name contains the hint."""
    if not hint:
        return None
    folder = Path(settings.MEDIA_ROOT) / "Recipes_images"
    for f in sorted(folder.glob("*")):
        if hint in f.name and f.is_file():
            return f
    return None


def _ext(data: bytes) -> str:
    if data[:3] == b"\xff\xd8\xff":
        return "jpg"
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return "png"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    return "jpg"


class Command(BaseCommand):
    help = "Add original demo recipes (idempotent)."

    def handle(self, *args, **opts):
        author, created = User.objects.get_or_create(
            username="culinarycanvas",
            defaults={"first_name": "Culinary", "last_name": "Canvas", "email": ""},
        )
        if created:
            author.set_unusable_password()
            author.save()

        added = 0
        for r in json.loads(SEED.read_text(encoding="utf-8")):
            if Recipe.objects.filter(recipe_title=r["title"]).exists():
                continue
            recipe = Recipe(
                recipe_title=r["title"],
                category=r["category"],
                recipe_description=r["description"],
                user=author,
            )
            photo = _find_photo(r.get("photo", ""))
            if photo:
                data = photo.read_bytes()
                # Saved through the model's upload_to, so it gets a proper name and extension.
                recipe.recipe_image.save(f"{r['photo']}.{_ext(data)}", ContentFile(data), save=False)
            recipe.save()
            added += 1

        self.stdout.write(self.style.SUCCESS(f"Seeded {added} recipe(s)."))

"""
URL configuration for CulinaryCanvas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import re

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView

from main_app import views

# Each page answers with or without a trailing slash, and links are generated without one.
# This matters when the portfolio (Next.js, which strips trailing slashes) proxies this app:
# Django's usual "add a slash" redirect would bounce back and forth with Next forever.
app_patterns = [
    re_path(r"^signup/?$", views.signup, name="signup"),
    re_path(r"^login/?$", views.login_view, name="login"),
    re_path(r"^profile/?$", views.profile, name="profile"),
    re_path(r"^signout/?$", views.signout, name="signout"),
    re_path(r"^category/?$", views.category, name="category"),
    re_path(r"^blogPostEntry/?$", views.blogPostEntry, name="blogPostEntry"),
    re_path(r"^blogSingle/(?P<recipe_id>[0-9]+)/?$", views.blogSingle, name="blogSingle"),
    re_path(r"^edit_recipes/(?P<recipe_id>[0-9]+)/?$", views.edit_recipes, name="edit_recipes"),
    re_path(r"^search/?$", views.search_view, name="search"),
    re_path(r"^delete_post/(?P<recipe_id>[0-9]+)/?$", views.delete_post, name="delete_post"),
    # Admin keeps Django's normal slashes; use it on the app's own address, not through the portfolio.
    path("admin/", admin.site.urls),
]

if settings.URL_PREFIX:
    prefix = re.escape(settings.URL_PREFIX)
    urlpatterns = [
        path("", RedirectView.as_view(url="/" + settings.URL_PREFIX)),
        re_path(rf"^{prefix}/?$", views.home, name="home"),
        re_path(rf"^{prefix}/", include(app_patterns)),
    ]
else:
    urlpatterns = [re_path(r"^$", views.home, name="home"), *app_patterns]

# Uploaded photos in development (on PythonAnywhere a static mapping serves /media/).
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

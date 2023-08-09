"""
URL configuration for animals project.

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
from django.contrib import admin
from django.urls import path
from info.views import (
    display_all_animals,
    display_all_families,
    display_one_animal,
    display_animal_per_family,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("animals/", display_all_animals, name="animals"),
    path("families/", display_all_families, name="families"),
    path("animal/<int:animal_id>/", display_one_animal, name="animal_id"),
    path(
        "animal_in_family/<int:family_id>/",
        display_animal_per_family,
        name="familY_id",
    ),
]

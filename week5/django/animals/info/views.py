from django.shortcuts import render
from django.http import HttpResponse

# from .models import Animals
from .data import animals, families

# Create your views here.


def display_all_animals(request):
    data = ""
    for animal in animals:
        data += f"Name: {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}, Height:{animal['height']}, Speed: {animal['speed']}<br>"
    return HttpResponse(data)


def display_all_families(request):
    family_names = [family["name"] for family in families]
    data = ", ".join(family_names)
    return HttpResponse(data)


def display_one_animal(request, animal_id: int):
    try:
        animal = next(animal for animal in animals if animal["id"] == animal_id)
        data = f"Name: {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}, Height: {animal['height']}, Speed: {animal['speed']}"
        return HttpResponse(data)
    except StopIteration:
        return HttpResponse("Animal not found")


def display_animal_per_family(request, family_id: int):
    animals_in_family = [animal for animal in animals if animal["family"] == family_id]
    data = ""
    for animal in animals_in_family:
        data += f"Name: {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}, Height: {animal['height']}, Speed: {animal['speed']}<br>"
    return HttpResponse(data)

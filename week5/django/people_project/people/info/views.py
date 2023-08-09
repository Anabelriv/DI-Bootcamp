from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
name = "Bob Smith"
age = 35
country = "USA"

people = ["bob", "martha", "fabio", "john"]

all_people = [
    {"id": 1, "name": "Bob Smith", "age": 35, "country": "USA"},
    {"id": 2, "name": "Martha Smith", "age": 60, "country": "USA"},
    {"id": 3, "name": "Fabio Alberto", "age": 18, "country": "Italy"},
    {"id": 4, "name": "Dietrich Stein", "age": 85, "country": "Germany"},
]


def display_person(request):
    person_info = f"Name: {name}\nAge: {age}\nCountry: {country}"
    return HttpResponse(person_info)


def display_people(request):
    sorted_people = sorted(people, key=lambda name: name.lower())
    formatted_people = "\n".join(person.capitalize() for person in sorted_people)
    return HttpResponse(formatted_people)


def display_all_people(request):
    sorted_people = sorted(all_people, key=lambda person: person["age"])
    formatted_people = "\n".join(
        f"Name: {person['name']}, Age: {person['age']}, Country: {person['country']}"
        for person in sorted_people
    )
    return HttpResponse(formatted_people)
